# Preparation Checklist — Vision-Guided Robotic Picking Lab

Complete this checklist before the first session. Each station needs its own setup.

## Hardware Setup (Per Station × 3)

### Robot
- [ ] Dobot Magician E6 assembled and powered on
- [ ] Suction cup end-effector installed and air supply connected
- [ ] Robot homed successfully
- [ ] Emergency stop working and accessible
- [ ] Robot workspace limits programmed (conservative safe zone)
- [ ] Robot base position documented (X, Y, Z in robot frame)
- [ ] Manual test move executed successfully
- [ ] Suction cup picks up a test objects reliably

### Camera
- [ ] Basler ACE2 mounted in top-down position on robot
- [ ] Camera connected to PC (USB3 or GigE)
- [ ] Basler Pylon software installed for initial verification
- [ ] `pypylon` Python package installed
- [ ] Test image captured successfully
- [ ] Full workspace visible in camera frame
- [ ] Lighting is consistent and diffuse (minimal shadows)

### PC
- [ ] Python 3.8+ installed
- [ ] Required packages installed (see below)
- [ ] Internet access verified (for Roboflow)
- [ ] All lab scripts copied to the PC
- [ ] Scripts tested end-to-end by teacher

### Objects
- [ ] Geometric shapes sourced: squares, rectangles, circles, triangles
- [ ] Objects are flat (suctionable)
- [ ] Objects are opaque (not transparent or reflective)
- [ ] Objects contrast well with the background
- [ ] At least 10 objects per station
- [ ] Drop zone defined (tray or marked area)

## Software Setup (Per PC)

### Python Packages
```bash
pip install pypylon opencv-python numpy roboflow
pip install opencv-contrib-python  # For ArUco detection
```

### Scripts Verified
- [ ] `capture_images.py` — captures and saves images from Basler camera
- [ ] `aruco_calibration.py` — detects ArUco and computes mm/pixel
- [ ] `run_inference.py` — runs Roboflow model on an image
- [ ] `pick_logic.py` — converts mask to pick coordinates
- [ ] `dobot_pick.py` — sends pick-and-place commands to Dobot E6

### Roboflow
- [ ] Organization created in Roboflow
- [ ] One project per group created (Instance Segmentation type)
- [ ] Each group has login credentials or shared access
- [ ] API key noted for each project

### Calibration Materials
- [ ] ArUco markers printed (dictionary: `DICT_4X4_50`, ID: 0)
- [ ] Marker physical size measured with calipers: _______ mm × _______ mm
- [ ] Marker is flat and not warped
- [ ] Backup mm_per_pixel value recorded per station (from prior testing)

## Pre-Lab Testing (Teacher Must Complete)

### Per Station End-to-End Test
- [ ] Capture image → run inference → get mask → compute pick point → execute pick
- [ ] Document the working calibration value
- [ ] Document the workspace-to-robot offset (X, Y)
- [ ] Confirm pick accuracy is within ±10 mm
- [ ] Record any station-specific quirks or adjustments

### Backup Materials
- [ ] Backup trained model available in Roboflow (in case student training fails)
- [ ] Backup image dataset available (in case capture fails)
- [ ] Spare objects available
- [ ] Spare ArUco markers printed

## Day-of Checklist

### Before Students Arrive
- [ ] All robots powered on and homed
- [ ] All cameras connected and streaming
- [ ] All PCs logged in with scripts accessible
- [ ] Lighting set up at each station
- [ ] Emergency stops tested
- [ ] Student handouts printed (one per student)
- [ ] ArUco markers at each station
- [ ] Objects arranged at each station
- [ ] Projector/screen ready for teacher demos
