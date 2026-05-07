# Student Handout — Session 3: Inference and Calibration

## What You Will Do Today
1. Run your trained model on images and inspect the results
2. Learn why the robot needs calibration to understand camera images
3. Perform a simple calibration using an ArUco marker
4. Convert object positions from pixels to millimeters

## The Core Problem

The camera sees **pixels** (e.g., "the circle center is at pixel 800, 450").
The robot works in **millimeters** (e.g., "move to 250 mm, 150 mm").

Today you will figure out the conversion between these two worlds.

## Your Tasks

### Task 1: Run Inference on Saved Images
1. Open `run_inference.py`
2. Enter your Roboflow API key and model version where marked
3. Run: `python run_inference.py --image path/to/your/image.jpg`
4. Inspect the output:
   - What class was detected?
   - What is the confidence score?
   - Where is the mask in the image?

5. **Try this:** Change the confidence threshold on the line marked `# TODO: adjust threshold`
   - Set it to `0.3` — what happens?
   - Set it to `0.95` — what happens?
   - Choose a good threshold: _______

### Task 2: Understand the Calibration Concept
Look at the camera image. Answer these questions:
- The image is _______ pixels wide and _______ pixels tall
- The workspace is approximately _______ mm wide (measure with a ruler)
- So roughly, 1 pixel ≈ _______ mm (divide workspace width by image width)

This rough estimate shows the idea. Now let's do it precisely.

### Task 3: ArUco Calibration
1. Place the ArUco marker flat on the workspace
2. **Measure the marker** with a ruler or caliper: _______ mm
3. Open `aruco_calibration.py`
4. Find the line marked `# TODO: enter your measured marker size`
5. Enter your measurement
6. Run: `python aruco_calibration.py`
7. Record the results:
   - Marker width in pixels: _______
   - Marker size in mm: _______
   - **mm per pixel: _______**

### Task 4: Verify Your Calibration
1. Place an object at a known position (measure from a reference point)
2. Capture an image and find the object's pixel position
3. Convert to mm using your calibration value
4. Compare to the actual measured position

| | Pixel Position | Computed mm | Measured mm | Error |
|---|---|---|---|---|
| X | | | | |
| Y | | | | |

Is the error acceptable for a suction cup? (hint: ±5–10 mm is usually fine)

### Task 5: Combine Inference + Calibration
1. Run inference on a new image
2. The script shows the detected object center in pixels
3. Apply your calibration to convert to mm
4. These mm values will become the robot's pick target in Session 4

### Task 6: Live Inference (If Time Permits)
1. Run: `python run_inference.py --live`
2. Move objects around and watch the detection update
3. Does the model still work well on live images?

## Key Formulas

```
mm_per_pixel = marker_size_mm / marker_width_pixels

object_x_mm = object_x_pixels × mm_per_pixel
object_y_mm = object_y_pixels × mm_per_pixel

robot_x = object_x_mm + workspace_offset_x
robot_y = object_y_mm + workspace_offset_y
```

## Discussion Questions
- Why do we need a fixed camera position for this to work?
- What would happen if the camera was tilted instead of top-down?
- What if the objects were tall (like a bottle) — would the centroid still be correct?
- Is this method good enough for a factory? What would need to change?

## Notes Space
_Use this area to write down observations:_

