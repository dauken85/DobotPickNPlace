# Fallback Plan — Vision-Guided Robotic Picking Lab

## Principle
Every failure mode should have a 2-minute recovery plan. The lab should never stall completely at any station.

---

## Failure: Camera Won't Connect

**Symptoms:** `pypylon` throws connection error, no image displayed

**Immediate fix:**
1. Check USB cable (reseat both ends)
2. Verify in Basler Pylon Viewer that the camera is visible
3. Restart the Python script

**If still broken:**
- Use a set of **pre-captured images** stored on the PC at `backup/images/`
- Students can still proceed with annotation, training, and inference on saved images
- Mark the station for teacher repair during the break

---

## Failure: Roboflow Training Fails or Takes Too Long

**Symptoms:** Training stuck, error messages, model not converging

**Immediate fix:**
1. Check internet connection
2. Verify dataset has at least 30 annotated images
3. Try restarting the training run

**If still broken:**
- Switch to the **backup pre-trained model** already in the Roboflow project
- Students can still run inference and complete Sessions 3–4
- Discuss why training might fail (too few images, bad annotations, class imbalance)

---

## Failure: Inference Returns No Detections

**Symptoms:** Model returns empty results, no masks drawn

**Immediate fix:**
1. Lower the confidence threshold to 0.1 to see if there are low-confidence detections
2. Check that the image is being sent correctly (correct file path, right format)
3. Verify API key and model version

**If still broken:**
- Switch to the backup model
- Use pre-saved inference results at `backup/inference_results/`
- Skip live inference and demonstrate from saved examples

---

## Failure: ArUco Marker Not Detected

**Symptoms:** Calibration script says "No marker found"

**Immediate fix:**
1. Check marker is flat and fully visible in the camera frame
2. Ensure correct ArUco dictionary in the script (`DICT_4X4_50`)
3. Check lighting — too dark or too much glare on the marker
4. Try a different marker ID

**If still broken:**
- Use the **backup calibration value** documented during preparation
- Teacher enters the known `mm_per_pixel` value manually
- Students can still understand the concept even with a teacher-provided value

---

## Failure: Robot Won't Connect or Move

**Symptoms:** Connection timeout, robot not responding, error on move command

**Immediate fix:**
1. Check robot is powered on and homed
2. Verify network/USB connection
3. Check emergency stop is not engaged
4. Restart the robot controller

**If still broken:**
- **Do not** let students troubleshoot robot hardware
- Teacher takes over that station
- Other groups continue; this group works on vision-only tasks
- If the robot cannot be recovered, demonstrate using another station's robot during wrap-up

---

## Failure: Robot Picks in Wrong Location

**Symptoms:** Robot moves but misses the object by >15 mm

**Immediate fix:**
1. Re-run ArUco calibration
2. Verify the workspace offset values
3. Place an object at a known position and check the pixel→mm→robot conversion step by step
4. Adjust offset values if needed

**If still broken:**
- Teacher manually enters corrected offset values
- Run a 3-point calibration: place object at 3 known positions, compute average correction
- Accept ~10 mm error — suction cups are forgiving

---

## Failure: Suction Cup Won't Pick Object

**Symptoms:** Robot reaches the object but doesn't pick it up

**Immediate fix:**
1. Check air supply is connected
2. Verify suction is activated in the script
3. Test suction manually (cover cup with finger — should feel suction)
4. Check if the object surface is too rough, porous, or too small

**If still broken:**
- Switch to objects with smoother, flatter surfaces
- Lower the approach height so the cup makes better contact
- If suction is mechanically broken, demonstrate the vision pipeline without physical picking

---

## Failure: PC or Software Crash

**Symptoms:** Script errors, PC freeze, environment issues

**Immediate fix:**
1. Restart the Python script
2. Check for common errors: missing package, wrong Python version, file path errors
3. Reinstall the problematic package

**If still broken:**
- Switch to a working backup PC (if available)
- Pair this group with another group temporarily
- Teacher demonstrates the failed step while the group observes

---

## General Fallback Philosophy

| Situation | Action |
|-----------|--------|
| One station broken | Other groups continue; teacher repairs during break |
| Critical demo failure | Use pre-recorded video of a successful run |
| Model performs poorly | Switch to backup model |
| Calibration way off | Use teacher-measured value |
| Multiple failures | Focus on the stations that work; combine groups if needed |

The lab should be designed so that **no single failure prevents learning**. If a hardware component fails, the software components can still be demonstrated, and vice versa.
