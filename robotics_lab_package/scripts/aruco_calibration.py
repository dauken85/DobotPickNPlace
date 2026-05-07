"""
aruco_calibration.py — Simple pixel-to-mm calibration using an ArUco marker.

This script detects an ArUco marker of known physical size in a camera image
and computes a mm-per-pixel scaling factor. This works for a fixed top-down
camera viewing a flat workspace.

Students should:
  1. Measure the printed ArUco marker with a ruler/caliper
  2. Enter the measured size where marked (# TODO)
  3. Run this script and record the mm_per_pixel value
  4. Verify by placing an object at a known distance

Usage:
    python aruco_calibration.py                  # Use Basler camera
    python aruco_calibration.py --simulate       # Use webcam
    python aruco_calibration.py --image FILE     # Use a saved image
"""

import argparse
import math

import cv2
import numpy as np

try:
    from pypylon import pylon
except ImportError:
    pylon = None

# ============================================================================
# TODO: Enter your measured ArUco marker size in millimeters
# Measure the marker with a ruler or caliper (the black square, edge to edge)
# ============================================================================
MARKER_SIZE_MM = 50.0  # <-- CHANGE THIS to your actual marker size in mm
# ============================================================================

# ArUco dictionary to use (must match your printed markers)
ARUCO_DICT_TYPE = cv2.aruco.DICT_5X5_50


def capture_from_basler():
    """Capture a single frame from the Basler camera."""
    if pylon is None:
        raise RuntimeError("pypylon not installed")
    tl_factory = pylon.TlFactory.GetInstance()
    devices = tl_factory.EnumerateDevices()
    if len(devices) == 0:
        raise RuntimeError("No Basler camera found")
    camera = pylon.InstantCamera(tl_factory.CreateDevice(devices[0]))
    camera.Open()
    camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    converter = pylon.ImageFormatConverter()
    converter.OutputPixelFormat = pylon.PixelType_BGR8packed
    grab_result = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
    image = converter.Convert(grab_result)
    frame = image.GetArray()
    grab_result.Release()
    camera.StopGrabbing()
    camera.Close()
    return frame


def capture_from_webcam():
    """Capture a single frame from a webcam."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Cannot open webcam")
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise RuntimeError("Failed to read from webcam")
    return frame


def detect_aruco(image):
    """Detect ArUco markers and return corners and IDs."""
    aruco_dict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT_TYPE)
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
    corners, ids, rejected = detector.detectMarkers(image)
    return corners, ids


def compute_marker_width_pixels(corners):
    """Compute the average side length of the first detected marker in pixels."""
    pts = corners[0][0]  # Shape: (4, 2) — four corner points

    # Compute the length of all four sides
    side_lengths = []
    for i in range(4):
        p1 = pts[i]
        p2 = pts[(i + 1) % 4]
        length = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        side_lengths.append(length)

    avg_side = sum(side_lengths) / len(side_lengths)
    return avg_side, side_lengths


def run_calibration(image):
    """Run the full calibration process on a single image."""
    print(f"Image size: {image.shape[1]} x {image.shape[0]} pixels")
    print(f"Marker size (entered): {MARKER_SIZE_MM} mm")
    print()

    # Detect ArUco markers
    corners, ids = detect_aruco(image)

    if ids is None or len(ids) == 0:
        print("ERROR: No ArUco marker detected!")
        print("Troubleshooting:")
        print("  - Is the marker flat and fully visible in the image?")
        print("  - Is the lighting sufficient (not too dark, no glare)?")
        print("  - Is the correct ArUco dictionary selected (DICT_4X4_50)?")
        return None

    print(f"Detected {len(ids)} marker(s). Using marker ID: {ids[0][0]}")

    # Compute marker width in pixels
    avg_side_px, side_lengths = compute_marker_width_pixels(corners)
    print(f"Marker side lengths (pixels): {[f'{s:.1f}' for s in side_lengths]}")
    print(f"Average marker width: {avg_side_px:.1f} pixels")
    print()

    # ========================================================================
    # CORE CALIBRATION FORMULA
    # ========================================================================
    mm_per_pixel = MARKER_SIZE_MM / avg_side_px
    pixels_per_mm = avg_side_px / MARKER_SIZE_MM
    # ========================================================================

    print("=" * 50)
    print(f"  mm per pixel:     {mm_per_pixel:.4f}")
    print(f"  pixels per mm:    {pixels_per_mm:.2f}")
    print("=" * 50)
    print()

    # Draw the result on the image
    display = image.copy()
    cv2.aruco.drawDetectedMarkers(display, corners, ids)

    # Draw marker center
    center = corners[0][0].mean(axis=0).astype(int)
    cv2.circle(display, tuple(center), 8, (0, 0, 255), -1)
    cv2.putText(
        display, f"mm/px = {mm_per_pixel:.4f}",
        (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2,
    )

    cv2.imshow("ArUco Calibration", cv2.resize(display, (640, 480)))
    print("Press any key to close the preview...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return mm_per_pixel


def main():
    parser = argparse.ArgumentParser(description="ArUco pixel-to-mm calibration")
    parser.add_argument("--image", type=str, help="Path to a saved image")
    parser.add_argument(
        "--simulate", action="store_true", help="Use webcam instead of Basler"
    )
    args = parser.parse_args()

    # Capture or load image
    if args.image:
        print(f"Loading image: {args.image}")
        image = cv2.imread(args.image)
        if image is None:
            print(f"ERROR: Cannot read image: {args.image}")
            return
    elif args.simulate:
        print("Capturing from webcam...")
        image = capture_from_webcam()
    else:
        print("Capturing from Basler camera...")
        image = capture_from_basler()

    result = run_calibration(image)
    if result is not None:
        print(f"\nCalibration complete. Use mm_per_pixel = {result:.4f}")
        print("Enter this value in your inference and pick scripts.")


if __name__ == "__main__":
    main()
