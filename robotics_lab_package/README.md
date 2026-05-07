# Vision-Guided Robotic Picking Lab

## Overview

A multi-session, hands-on robotics lab where participants learn to segment objects using a trained model and pick them with a robot arm.

**Pipeline:** Capture images → Annotate in Roboflow → Train segmentation model → Run inference → Calibrate camera-to-robot → Execute pick-and-place

## Equipment Per Station (×3)

- Dobot Magician E6 with suction cup
- Basler ACE2 industrial camera (top-down mount)
- PC with Python, internet access, and Roboflow account
- Mixed geometric shapes (squares, rectangles, circles, triangles)

## Participants

- 2 students per station, 3 stations, 6 students total
- Limited programming background assumed

## Lab Structure

| Session | Topic | Duration |
|---------|-------|----------|
| 1 | System overview, safety, image capture | ~3 hours |
| 2 | Annotation and model training in Roboflow | ~3 hours |
| 3 | Inference and ArUco calibration | ~3 hours |
| 4 | Robot-guided pick-and-place | ~3 hours |
| 5 (optional) | Improvement and engineering discussion | ~2 hours |

## Package Contents

```
robotics_lab_package/
├── README.md                          # This file
├── teacher_guide.md                   # Full teacher reference
├── preparation_checklist.md           # Pre-lab setup checklist
├── fallback_plan.md                   # Recovery procedures
├── sessions/
│   ├── session_1_capture.md           # Session 1 agenda
│   ├── session_2_annotation.md        # Session 2 agenda
│   ├── session_3_inference_calib.md   # Session 3 agenda
│   └── session_4_pick_and_place.md    # Session 4 agenda
├── handouts/
│   ├── student_handout_session_1.md   # Student-facing handout
│   ├── student_handout_session_2.md
│   ├── student_handout_session_3.md
│   └── student_handout_session_4.md
├── scripts/
│   ├── capture_images.py             # Basler image capture
│   ├── aruco_calibration.py          # ArUco pixel-to-mm calibration
│   ├── run_inference.py              # Roboflow model inference
│   ├── pick_logic.py                 # Mask → pick point conversion
│   └── dobot_pick.py                 # Dobot E6 pick-and-place
└── notebooks/
    └── lab_full_pipeline.ipynb       # Interactive Jupyter notebook
```
