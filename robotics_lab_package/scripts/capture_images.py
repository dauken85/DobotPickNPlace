"""
capture_images.py — Basler ACE2 image capture for the robotics lab.

Usage:
    python capture_images.py --test       # Live preview only
    python capture_images.py --save       # Preview + save on SPACE press
    python capture_images.py --output DIR # Save to a specific directory

Controls:
    SPACE  — Save current frame
    Q      — Quit
"""

import argparse
import os
import time

import cv2

try:
    from pypylon import pylon
except ImportError:
    print("ERROR: pypylon is not installed. Run: pip install pypylon")
    print("If you don't have a Basler camera, use --simulate to test with a webcam.")
    raise


def create_output_dir(path: str) -> str:
    """Create the output directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)
    return path


def connect_basler_camera():
    """Connect to the first available Basler camera."""
    tl_factory = pylon.TlFactory.GetInstance()
    devices = tl_factory.EnumerateDevices()

    if len(devices) == 0:
        raise RuntimeError(
            "No Basler camera found. Check USB/GigE connection and drivers."
        )

    camera = pylon.InstantCamera(tl_factory.CreateDevice(devices[0]))
    camera.Open()

    # Configure for continuous acquisition
    camera.AcquisitionMode.SetValue("Continuous")

    # Use a converter to get OpenCV-compatible BGR images
    converter = pylon.ImageFormatConverter()
    converter.OutputPixelFormat = pylon.PixelType_BGR8packed
    converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    print(f"Connected to: {camera.GetDeviceInfo().GetModelName()}")
    print(f"Resolution: {camera.Width.Value} x {camera.Height.Value}")

    return camera, converter


def connect_webcam(index: int = 0):
    """Fallback: connect to a USB webcam for testing without a Basler camera."""
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open webcam at index {index}")
    print(f"Connected to webcam (index {index})")
    return cap


def run_capture(output_dir: str, save_enabled: bool, simulate: bool = False):
    """Main capture loop."""
    output_dir = create_output_dir(output_dir)
    frame_count = 0
    saved_count = 0

    if simulate:
        cap = connect_webcam()
    else:
        camera, converter = connect_basler_camera()
        camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

    print("\n--- Image Capture ---")
    if save_enabled:
        print(f"Saving images to: {output_dir}")
        print("Press SPACE to save a frame, Q to quit.")
    else:
        print("Preview mode. Press Q to quit.")

    try:
        while True:
            if simulate:
                ret, frame = cap.read()
                if not ret:
                    print("Failed to read from webcam.")
                    break
            else:
                grab_result = camera.RetrieveResult(
                    5000, pylon.TimeoutHandling_ThrowException
                )
                if not grab_result.GrabSucceeded():
                    print("Grab failed.")
                    continue
                image = converter.Convert(grab_result)
                frame = image.GetArray()
                grab_result.Release()

            frame_count += 1

            # Scale down for display
            display = cv2.resize(frame, (640, 480))
            info_text = f"Frame: {frame_count} | Saved: {saved_count}"
            cv2.putText(
                display, info_text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
            )
            if save_enabled:
                cv2.putText(
                    display, "SPACE=Save  Q=Quit", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 200, 200), 1,
                )

            cv2.imshow("Basler ACE2 - Capture", display)

            key = cv2.waitKey(30) & 0xFF
            if key == ord("q"):
                break
            elif key == ord(" ") and save_enabled:
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                filename = f"img_{timestamp}_{saved_count:04d}.png"
                filepath = os.path.join(output_dir, filename)
                cv2.imwrite(filepath, frame)
                saved_count += 1
                print(f"  Saved: {filename}")

    finally:
        if simulate:
            cap.release()
        else:
            camera.StopGrabbing()
            camera.Close()
        cv2.destroyAllWindows()

    print(f"\nDone. Total frames: {frame_count}, Saved: {saved_count}")


def main():
    parser = argparse.ArgumentParser(description="Basler ACE2 image capture")
    parser.add_argument(
        "--test", action="store_true", help="Preview mode (no saving)"
    )
    parser.add_argument(
        "--save", action="store_true", help="Save mode (SPACE to capture)"
    )
    parser.add_argument(
        "--output", type=str, default="captured_images",
        help="Output directory for saved images",
    )
    parser.add_argument(
        "--simulate", action="store_true",
        help="Use a USB webcam instead of Basler camera (for testing)",
    )
    args = parser.parse_args()

    if not args.test and not args.save:
        print("Specify --test (preview only) or --save (capture mode).")
        print("Example: python capture_images.py --save --output my_images")
        return

    save_enabled = args.save
    run_capture(args.output, save_enabled, simulate=args.simulate)


if __name__ == "__main__":
    main()
