"""
run_inference.py — Run a Roboflow segmentation model on images.

This script sends an image to your trained Roboflow model and displays
the segmentation results (masks, class names, confidence scores).

Students should:
  1. Enter their Roboflow API key and model info where marked (# TODO)
  2. Run on saved images first to understand the output
  3. Adjust the confidence threshold to see its effect
  4. Optionally run in live mode with --live

Usage:
    python run_inference.py --image path/to/image.jpg
    python run_inference.py --folder path/to/images/
    python run_inference.py --live              # Live camera inference
    python run_inference.py --live --simulate   # Live with webcam
"""

import argparse
import os
import time

import cv2
import numpy as np

try:
    from roboflow import Roboflow
except ImportError:
    print("ERROR: roboflow package not installed. Run: pip install roboflow")
    raise

try:
    from pypylon import pylon
except ImportError:
    pylon = None

# ============================================================================
# TODO: Enter your Roboflow API key and model details
# ============================================================================
ROBOFLOW_API_KEY = "YOUR_API_KEY_HERE"  # <-- CHANGE THIS
ROBOFLOW_PROJECT = "YOUR_PROJECT_NAME"  # <-- CHANGE THIS
ROBOFLOW_MODEL_VERSION = 1              # <-- CHANGE THIS if needed
# ============================================================================

# ============================================================================
# TODO: Adjust the confidence threshold (0.0 to 1.0)
# Higher = fewer but more confident detections
# Lower = more detections but more false positives
# ============================================================================
CONFIDENCE_THRESHOLD = 0.5  # <-- TRY CHANGING THIS (e.g., 0.3 or 0.9)
# ============================================================================


def load_model():
    """Connect to Roboflow and load the model."""
    if ROBOFLOW_API_KEY == "YOUR_API_KEY_HERE":
        raise ValueError(
            "Please enter your Roboflow API key in run_inference.py (line with TODO)"
        )
    rf = Roboflow(api_key=ROBOFLOW_API_KEY)
    project = rf.workspace().project(ROBOFLOW_PROJECT)
    model = project.version(ROBOFLOW_MODEL_VERSION).model
    print(f"Model loaded: {ROBOFLOW_PROJECT} v{ROBOFLOW_MODEL_VERSION}")
    return model


def run_inference_on_image(model, image_path: str):
    """Run segmentation inference on a single image."""
    prediction = model.predict(
        image_path, confidence=int(CONFIDENCE_THRESHOLD * 100)
    )
    return prediction


def draw_results(image, predictions):
    """Draw segmentation masks and labels on the image."""
    display = image.copy()
    results = predictions.json()
    detections = results.get("predictions", [])

    print(f"  Detected {len(detections)} object(s)")

    centroids = []

    for det in detections:
        class_name = det["class"]
        confidence = det["confidence"]
        x_center = det["x"]
        y_center = det["y"]
        width = det["width"]
        height = det["height"]

        # Draw bounding box
        x1 = int(x_center - width / 2)
        y1 = int(y_center - height / 2)
        x2 = int(x_center + width / 2)
        y2 = int(y_center + height / 2)
        cv2.rectangle(display, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Draw segmentation mask if available
        if "points" in det:
            points = det["points"]
            pts = np.array(
                [(int(p["x"]), int(p["y"])) for p in points], dtype=np.int32
            )
            overlay = display.copy()
            cv2.fillPoly(overlay, [pts], (0, 255, 0))
            cv2.addWeighted(overlay, 0.3, display, 0.7, 0, display)
            cv2.polylines(display, [pts], True, (0, 255, 0), 2)

            # Compute centroid from mask polygon
            M = cv2.moments(pts)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
            else:
                cx, cy = int(x_center), int(y_center)
        else:
            cx, cy = int(x_center), int(y_center)

        # Draw centroid
        cv2.circle(display, (cx, cy), 6, (0, 0, 255), -1)

        # Draw label
        label = f"{class_name} {confidence:.2f}"
        cv2.putText(
            display, label, (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2,
        )

        centroids.append({
            "class": class_name,
            "confidence": confidence,
            "centroid_px": (cx, cy),
        })

        print(f"    {class_name}: conf={confidence:.2f}, center=({cx}, {cy}) px")

    return display, centroids


def process_single_image(model, image_path: str):
    """Process a single image: run inference and display results."""
    print(f"\nProcessing: {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        print(f"  ERROR: Cannot read image")
        return None

    predictions = run_inference_on_image(model, image_path)
    display, centroids = draw_results(image, predictions)

    cv2.imshow("Inference Result", display)
    print("  Press any key for next image, Q to quit")
    key = cv2.waitKey(0) & 0xFF
    return key != ord("q"), centroids


def process_folder(model, folder_path: str):
    """Process all images in a folder."""
    extensions = {".jpg", ".jpeg", ".png", ".bmp"}
    image_files = sorted(
        f for f in os.listdir(folder_path)
        if os.path.splitext(f)[1].lower() in extensions
    )

    if not image_files:
        print(f"No images found in {folder_path}")
        return

    print(f"Found {len(image_files)} images in {folder_path}")

    for filename in image_files:
        filepath = os.path.join(folder_path, filename)
        result = process_single_image(model, filepath)
        if result is None or not result[0]:
            break

    cv2.destroyAllWindows()


def run_live(model, simulate: bool = False):
    """Run inference on live camera feed."""
    if simulate:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open webcam")
            return
    else:
        if pylon is None:
            print("pypylon not installed. Use --simulate for webcam.")
            return
        tl_factory = pylon.TlFactory.GetInstance()
        devices = tl_factory.EnumerateDevices()
        if len(devices) == 0:
            print("No Basler camera found")
            return
        camera = pylon.InstantCamera(tl_factory.CreateDevice(devices[0]))
        camera.Open()
        camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed

    temp_path = "_temp_inference_frame.jpg"
    print("\nLive inference. Press Q to quit.")

    try:
        while True:
            if simulate:
                ret, frame = cap.read()
                if not ret:
                    break
            else:
                grab = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
                if not grab.GrabSucceeded():
                    continue
                image = converter.Convert(grab)
                frame = image.GetArray()
                grab.Release()

            # Save temp frame and run inference
            cv2.imwrite(temp_path, frame)
            predictions = run_inference_on_image(model, temp_path)
            display, centroids = draw_results(frame, predictions)

            cv2.imshow("Live Inference", display)
            if cv2.waitKey(100) & 0xFF == ord("q"):
                break

    finally:
        if simulate:
            cap.release()
        else:
            camera.StopGrabbing()
            camera.Close()
        cv2.destroyAllWindows()
        if os.path.exists(temp_path):
            os.remove(temp_path)


def main():
    parser = argparse.ArgumentParser(description="Roboflow segmentation inference")
    parser.add_argument("--image", type=str, help="Path to a single image")
    parser.add_argument("--folder", type=str, help="Path to a folder of images")
    parser.add_argument("--live", action="store_true", help="Live camera inference")
    parser.add_argument("--simulate", action="store_true", help="Use webcam")
    args = parser.parse_args()

    model = load_model()

    if args.live:
        run_live(model, simulate=args.simulate)
    elif args.image:
        process_single_image(model, args.image)
        cv2.destroyAllWindows()
    elif args.folder:
        process_folder(model, args.folder)
    else:
        print("Specify --image, --folder, or --live")
        print("Example: python run_inference.py --image my_image.jpg")


if __name__ == "__main__":
    main()
