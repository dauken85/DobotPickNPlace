# Teacher Guide — Vision-Guided Robotic Picking Lab

## 1. Lab Philosophy

This lab is designed for participants with limited programming and robotics experience. The teacher prepares all infrastructure code; students interact with the pipeline through small, guided edits and parameter adjustments. The goal is conceptual understanding of the full perception-to-action pipeline, not software development skill.

## 2. Format

- **4 core sessions**, each approximately 3 hours
- **3 robot stations**, each with its own Dobot E6, Basler ACE2, and PC
- **2 students per station**, alternating vision-lead and robot-lead roles
- **1 optional session** for improvement and discussion

## 3. Role Alternation

| Session | Student A | Student B |
|---------|-----------|-----------|
| 1 | Camera lead (captures images) | Robot lead (learns safety, workspace) |
| 2 | Annotation lead | Quality checker |
| 3 | Inference lead | Calibration lead |
| 4 | Swap from Session 1 roles | Swap from Session 1 roles |

## 4. What You Prepare vs What Students Do

### Teacher prepares (before the lab):
- Camera connection and capture script working on each PC
- Basler camera mounted top-down above workspace
- Consistent lighting at each station
- Roboflow organization and project structure
- ArUco calibration script with clearly marked editable sections
- Inference script connected to Roboflow API
- Pick-point computation from segmentation mask
- Dobot E6 pick-and-place routine with safety limits
- Known-safe robot workspace boundaries
- A backup trained model (in case student training fails)
- A backup calibration (known pixel-to-mm value)
- Printed ArUco markers of known size

### Students do:
- Capture images of objects in the workspace
- Upload and annotate images in Roboflow
- Train a segmentation model and compare versions
- Run inference and inspect results
- Measure and enter ArUco marker size, compute pixel-to-mm ratio
- Adjust confidence thresholds and pick-area limits
- Select target objects and trigger picks
- Debug failed picks and discuss improvements

## 5. Object Set

Use simple geometric shapes:
- Squares (e.g., wooden blocks)
- Rectangles (e.g., erasers, small boxes)
- Circles (e.g., plastic discs, coasters)
- Triangles (e.g., 3D-printed or cut foam)

Requirements:
- Flat enough for suction cup pickup
- Not transparent or highly reflective
- Distinct from the background surface
- 3–5 classes maximum
- Multiple instances of each class

## 6. Calibration Approach

This lab uses a **simplified planar calibration**:
1. Place an ArUco marker of known physical size in the workspace
2. Detect the marker corners in the image
3. Compute pixels-per-mm from the known marker width
4. Apply that scale to convert object centroids from pixels to mm
5. Add a fixed offset to map workspace mm to robot base coordinates

**Limitations to communicate to students:**
- Only valid for a fixed camera height and angle
- Only valid for objects on the same plane as the marker
- Tall objects will have positioning error
- This is NOT full hand-eye calibration

## 7. Safety Rules

- Robot must not move until the workspace is clear of hands
- Emergency stop must be accessible and tested before each session
- Maximum robot speed should be limited in the program
- Suction cup must be tested manually before automated picks
- Students must not modify robot motion limits
- Teacher must verify each station's first automated pick attempt

## 8. Timing Guide

### Session 1 (3 hours)
| Time | Activity |
|------|----------|
| 0:00–0:30 | Welcome, pipeline overview, safety briefing |
| 0:30–0:45 | Teacher demo: full pick from segmented object |
| 0:45–1:15 | Station setup: camera connection, robot power-on, workspace arrangement |
| 1:15–1:30 | Break |
| 1:30–2:15 | Image capture: students photograph objects in varied arrangements |
| 2:15–2:45 | Review captured images, discuss quality, lighting, angles |
| 2:45–3:00 | Wrap-up: what makes a good training dataset |

### Session 2 (3 hours)
| Time | Activity |
|------|----------|
| 0:00–0:15 | Recap pipeline, introduce Roboflow |
| 0:15–0:45 | Upload images, create classes, discuss naming |
| 0:45–1:30 | Annotate segmentation masks |
| 1:30–1:45 | Break |
| 1:45–2:15 | Start model training, discuss train/val split |
| 2:15–2:45 | Compare model versions, review metrics |
| 2:45–3:00 | Wrap-up: what affects model quality |

### Session 3 (3 hours)
| Time | Activity |
|------|----------|
| 0:00–0:15 | Recap, introduce inference and calibration |
| 0:15–0:45 | Run inference on saved images, inspect masks |
| 0:45–1:15 | ArUco calibration exercise |
| 1:15–1:30 | Break |
| 1:30–2:00 | Apply calibration to convert mask centroids to mm |
| 2:00–2:30 | Switch to live camera inference |
| 2:30–2:45 | Threshold tuning: confidence, area, class filters |
| 2:45–3:00 | Wrap-up: what can go wrong in inference |

### Session 4 (3 hours)
| Time | Activity |
|------|----------|
| 0:00–0:15 | Recap, teacher verifies each station's calibration |
| 0:15–0:45 | First supervised pick attempts (teacher present) |
| 0:45–1:15 | Students run picks independently, log successes/failures |
| 1:15–1:30 | Break |
| 1:30–2:15 | Mixed clutter picking: multiple objects, varied layouts |
| 2:15–2:45 | Final demo: each group shows best pick sequence |
| 2:45–3:00 | Discussion: failure analysis, industrial requirements |

## 9. Assessment Suggestions

If assessment is needed, evaluate:
1. Dataset quality (variety, consistency, correct labels)
2. Model performance (mAP, visual inspection)
3. Calibration accuracy (measured vs actual position)
4. Pick success rate
5. Ability to explain the pipeline and diagnose failures

## 10. Common Student Questions

| Question | Answer |
|----------|--------|
| Why not just use color detection? | Works for simple cases, but segmentation handles overlap, varied lighting, and similar colors better |
| Why is calibration needed? | The camera sees pixels; the robot moves in mm. We need a mapping between the two. |
| Why does the robot miss sometimes? | Calibration error, object height, mask inaccuracy, or suction cup alignment |
| Can we use this in a factory? | The concept is the same, but industrial systems need better calibration, error handling, and speed |
| Why top-down camera only? | Simplifies calibration to a 2D scaling problem instead of full 3D pose estimation |
