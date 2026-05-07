"""
pick_logic.py — Convert segmentation mask to a pick point.

This module takes inference results (detected objects with masks) and:
  1. Computes the centroid of each detected mask
  2. Converts pixel coordinates to millimeters using calibration
  3. Applies workspace offset to get robot-frame coordinates
  4. Selects the best object to pick

Students should:
  - Enter their calibration value (mm_per_pixel) where marked
  - Enter the workspace offset where marked
  - Understand how the centroid is computed
  - Try adjusting the minimum area filter

Usage (standalone):
    python pick_logic.py --image path/to/image.jpg

Typically called from the main pipeline or notebook.
"""

import argparse

import cv2
import numpy as np

# ============================================================================
# TODO: Enter your calibration value from aruco_calibration.py
# ============================================================================
MM_PER_PIXEL = 0.0  # <-- CHANGE THIS to your calibrated value (e.g., 0.26)
# ============================================================================

# ============================================================================
# TODO: Enter the workspace offset (mm)
# This is the position of the image origin (top-left corner of camera view)
# relative to the robot base frame. The teacher will help measure this.
# ============================================================================
WORKSPACE_OFFSET_X_MM = 0.0  # <-- CHANGE THIS (mm from robot base to image left)
WORKSPACE_OFFSET_Y_MM = 0.0  # <-- CHANGE THIS (mm from robot base to image top)
# ============================================================================

# ============================================================================
# TODO: Adjust minimum area filter (in pixels)
# Detections smaller than this are ignored (likely noise)
# ============================================================================
MIN_AREA_PIXELS = 500  # <-- TRY CHANGING THIS
# ============================================================================

# Fixed pick height above the workspace (mm) — set by teacher
PICK_HEIGHT_MM = 5.0  # Height to descend to for suction pickup


def compute_centroid(mask_points):
    """Compute the centroid of a polygon mask.

    Args:
        mask_points: list of {"x": float, "y": float} dicts from Roboflow

    Returns:
        (cx, cy) in pixels, or None if mask is too small
    """
    pts = np.array([(p["x"], p["y"]) for p in mask_points], dtype=np.float32)
    area = cv2.contourArea(pts.astype(np.int32))

    if area < MIN_AREA_PIXELS:
        return None

    M = cv2.moments(pts.astype(np.int32))
    if M["m00"] == 0:
        return None

    cx = M["m10"] / M["m00"]
    cy = M["m01"] / M["m00"]
    return (cx, cy)


def pixel_to_mm(cx_px, cy_px):
    """Convert pixel coordinates to mm using calibration.

    Args:
        cx_px: x coordinate in pixels
        cy_px: y coordinate in pixels

    Returns:
        (x_mm, y_mm) in workspace millimeters
    """
    if MM_PER_PIXEL <= 0:
        raise ValueError(
            "MM_PER_PIXEL is not set! Run aruco_calibration.py first "
            "and enter the value in pick_logic.py."
        )

    x_mm = cx_px * MM_PER_PIXEL
    y_mm = cy_px * MM_PER_PIXEL
    return (x_mm, y_mm)


def mm_to_robot_frame(x_mm, y_mm):
    """Convert workspace mm to robot base frame coordinates.

    Args:
        x_mm: x in workspace mm
        y_mm: y in workspace mm

    Returns:
        (robot_x, robot_y, robot_z) in robot frame mm
    """
    robot_x = x_mm + WORKSPACE_OFFSET_X_MM
    robot_y = y_mm + WORKSPACE_OFFSET_Y_MM
    robot_z = PICK_HEIGHT_MM
    return (robot_x, robot_y, robot_z)


def select_best_pick(detections):
    """Select the best object to pick from a list of detections.

    Strategy: pick the object with the highest confidence score.

    Args:
        detections: list of dicts with "class", "confidence", "points"

    Returns:
        dict with pick info, or None if nothing is pickable
    """
    candidates = []

    for det in detections:
        if "points" not in det:
            continue

        centroid = compute_centroid(det["points"])
        if centroid is None:
            continue  # Too small or invalid mask

        cx_px, cy_px = centroid
        x_mm, y_mm = pixel_to_mm(cx_px, cy_px)
        robot_x, robot_y, robot_z = mm_to_robot_frame(x_mm, y_mm)

        candidates.append({
            "class": det["class"],
            "confidence": det["confidence"],
            "centroid_px": (cx_px, cy_px),
            "position_mm": (x_mm, y_mm),
            "robot_target": (robot_x, robot_y, robot_z),
        })

    if not candidates:
        return None

    # Pick the highest confidence detection
    best = max(candidates, key=lambda c: c["confidence"])
    return best


def process_inference_result(result_json):
    """Process a full inference result and return pick targets.

    Args:
        result_json: the JSON response from Roboflow prediction

    Returns:
        list of pick candidates, sorted by confidence (highest first)
    """
    detections = result_json.get("predictions", [])
    print(f"Processing {len(detections)} detection(s)...")

    candidates = []
    for det in detections:
        if "points" not in det:
            continue

        centroid = compute_centroid(det["points"])
        if centroid is None:
            print(f"  Skipped {det['class']}: mask too small")
            continue

        cx_px, cy_px = centroid
        x_mm, y_mm = pixel_to_mm(cx_px, cy_px)
        robot_x, robot_y, robot_z = mm_to_robot_frame(x_mm, y_mm)

        candidate = {
            "class": det["class"],
            "confidence": det["confidence"],
            "centroid_px": (round(cx_px, 1), round(cy_px, 1)),
            "position_mm": (round(x_mm, 1), round(y_mm, 1)),
            "robot_target": (round(robot_x, 1), round(robot_y, 1), round(robot_z, 1)),
        }
        candidates.append(candidate)
        print(
            f"  {candidate['class']}: conf={candidate['confidence']:.2f}, "
            f"px=({cx_px:.0f},{cy_px:.0f}), "
            f"mm=({x_mm:.1f},{y_mm:.1f}), "
            f"robot=({robot_x:.1f},{robot_y:.1f},{robot_z:.1f})"
        )

    candidates.sort(key=lambda c: c["confidence"], reverse=True)
    return candidates


if __name__ == "__main__":
    # Standalone test with example data
    print("pick_logic.py — standalone test")
    print(f"MM_PER_PIXEL = {MM_PER_PIXEL}")
    print(f"WORKSPACE_OFFSET = ({WORKSPACE_OFFSET_X_MM}, {WORKSPACE_OFFSET_Y_MM})")
    print()

    if MM_PER_PIXEL <= 0:
        print("Set MM_PER_PIXEL before running. Use aruco_calibration.py to find it.")
    else:
        # Example: test with a dummy detection
        test_points = [
            {"x": 400, "y": 300},
            {"x": 450, "y": 300},
            {"x": 450, "y": 350},
            {"x": 400, "y": 350},
        ]
        centroid = compute_centroid(test_points)
        if centroid:
            x_mm, y_mm = pixel_to_mm(*centroid)
            rx, ry, rz = mm_to_robot_frame(x_mm, y_mm)
            print(f"Test centroid (px): {centroid}")
            print(f"Test position (mm): ({x_mm:.1f}, {y_mm:.1f})")
            print(f"Test robot target:  ({rx:.1f}, {ry:.1f}, {rz:.1f})")
