# SKF Robotics Lab — Copilot Instructions

## Project Context
This is an **educational robotics lab package** for vision-guided pick-and-place. It targets the **Dobot Magician E6** robot with a **Basler ACE2** industrial camera. The audience is students learning robot-vision integration.

## Hardware Stack
| Component | Interface |
|-----------|-----------|
| Dobot Magician E6 | TCP/IP socket, port 29999 (dashboard) + port 30003 (real-time) |
| Basler ACE2 camera | pypylon SDK |
| Suction gripper | Digital I/O via Dobot API |

## Key Conventions
- All robot commands are **ASCII strings, semicolon-terminated**; always parse response code before proceeding
- Workspace limits are defined as constants at the top of each script — never hardcode raw coordinate values inline
- Camera calibration data is in `camera_matrix.npy` and `dist_coeffs.npy`; homography is in `homography_matrix.json`
- Pixel → robot coordinates: undistort first, then apply homography
- **Safety first**: always check robot alarm state before issuing motion; implement soft workspace envelope checks

## Script Responsibilities
- `capture_images.py` — Basler frame capture and saving
- `aruco_calibration.py` — Homography computation and saving
- `run_inference.py` — Roboflow model inference
- `pick_logic.py` — Mask → pick point (centroid extraction)
- `dobot_pick.py` — Full pick-and-place execution

## Student-Facing Code
- Keep APIs simple and well-commented for student use
- Avoid complex abstractions — explicit step-by-step code is preferred
- Always include `try/except` with clear error messages around hardware calls
- Print robot state transitions for educational visibility

## Do Not
- Do not hardcode IP addresses — use a `config.py` or `.env`
- Do not omit alarm checks before motion sequences
- Do not use `time.sleep` for robot synchronization — use position feedback polling
