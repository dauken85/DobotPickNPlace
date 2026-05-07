# Session 3 — Inference and ArUco Calibration

## Learning Objectives
- Run a trained segmentation model on images and interpret the output
- Understand the concept of pixel-to-mm conversion
- Perform a simple calibration using an ArUco marker
- Convert object positions from image pixels to physical millimeters

## Duration: ~3 hours

## Required Materials
- [ ] Trained Roboflow model (from Session 2 or backup)
- [ ] Roboflow API key for each group
- [ ] `run_inference.py` script on each PC
- [ ] `aruco_calibration.py` script on each PC
- [ ] Printed ArUco markers (known physical size, e.g., 50 mm × 50 mm)
- [ ] Ruler or caliper to verify marker size
- [ ] Camera mounted in fixed top-down position

## Agenda

### Part 1: Recap and Introduction (15 min)
1. Recap: we have a trained model that can segment objects
2. Today's question: "The model tells us where objects are in the *image*. But the robot doesn't understand pixels — it works in millimeters. How do we bridge the gap?"
3. Introduce the two goals: inference and calibration

### Part 2: Inference on Saved Images (30 min)
1. Open `run_inference.py`
2. Teacher explains:
   - How the script sends an image to the Roboflow API
   - What comes back: class name, confidence score, mask polygon
3. Students run inference on 5–10 saved images
4. Inspect results:
   - Are all objects detected?
   - Are confidence scores reasonable?
   - Do mask boundaries look accurate?
5. **Student task:** Change the confidence threshold and observe the effect

### Part 3: Understanding the Calibration Problem (15 min)
1. Teacher draws on whiteboard or shows diagram:
   - Camera sees a grid of pixels (e.g., 1920×1080)
   - An object center might be at pixel (800, 450)
   - The robot arm needs a position like (250 mm, 150 mm) relative to its base
   - We need: **how many mm does one pixel represent?**
2. Discuss: when is this simple scaling valid?
   - Fixed camera position
   - Flat workspace
   - Objects on the same plane
   - Top-down view

### Break (15 min)

### Part 4: ArUco Calibration Exercise (45 min)
1. Place the printed ArUco marker in the robot workspace
2. Open `aruco_calibration.py`
3. Teacher explains the script structure:
   - Captures an image
   - Detects the ArUco marker corners
   - Computes the marker width in pixels
   - **Students must enter the known physical marker size (in mm)**
   - Script computes: `mm_per_pixel = marker_size_mm / marker_width_pixels`
4. **Student tasks:**
   - Measure the printed marker with a ruler
   - Enter the measured size into the script (clearly marked `# TODO` line)
   - Run the script and record the `mm_per_pixel` value
   - Verify: place an object at a known distance, check if the conversion is correct
5. Discuss sources of error:
   - Marker not perfectly flat
   - Camera lens distortion at edges
   - Measurement inaccuracy

### Part 5: Apply Calibration to Inference Results (30 min)
1. Combine inference + calibration:
   - Run the model on a new image
   - Find the mask centroid (center of detected object) in pixels
   - Convert to mm using the calibration value
   - Add the workspace offset to get robot-frame coordinates
2. **Student task:** Verify the computed position by placing an object at a known location
3. Discuss: how accurate does this need to be for suction picking?
   - Suction cups are forgiving (±5–10 mm is often fine)
   - Finger grippers need much better accuracy

### Part 6: Live Camera Inference (15 min)
1. Switch from saved images to live camera captures
2. Run inference on freshly captured images
3. Observe how results vary with lighting, object position, and clutter

### Part 7: Wrap-up (15 min)
1. Each group reports their `mm_per_pixel` value and verification result
2. Discussion: why do different stations get slightly different values?
3. Preview Session 4: connecting the vision output to the robot

## Teacher Notes
- Print ArUco markers at an exact known size (verify with calipers before lab)
- Use ArUco dictionary `DICT_4X4_50` or `DICT_6X6_250` for reliable detection
- The calibration script should auto-detect the marker; students only enter the size and verify
- Have a backup `mm_per_pixel` value for each station in case detection fails
- The workspace-to-robot offset should be pre-measured by the teacher
- If a group's model performs poorly, let them use the backup pre-trained model

## Key Concept to Emphasize
> Calibration is the bridge between what the camera sees and where the robot moves. Without it, the robot is blind — it has data but no understanding of the physical world.
