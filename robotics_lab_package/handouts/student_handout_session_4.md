# Student Handout — Session 4: ArUco Calibration

## What You Will Do in this Session
1. Learn why the robot needs calibration to understand camera images
2. Perform a simple calibration using an ArUco marker
3. Convert object positions from pixels to millimeters

## The Core Problem
The camera sees **pixels** (e.g., "the circle center is at pixel 800, 450").
The robot works in **millimeters** (e.g., "move to 250 mm, 150 mm").

In this session you will figure out the conversion between these two worlds.

## Your Tasks

### Task 1: Understand the Calibration Concept
Look at the camera image. Answer these questions:
- The image is _______ pixels wide and _______ pixels tall
- The workspace is approximately _______ mm wide (measure with a ruler)
- So roughly, 1 pixel ≈ _______ mm (divide workspace width by image width)

This rough estimate shows the idea. Now let's do it precisely.

### Task 2: ArUco Calibration
1. Place the ArUco marker flat on the workspace
2. **Measure the marker**: _______ mm
4. Find the line marked `# TODO: enter your measured marker size` in section 2.
5. Enter your measurement
6. Run the section, it will show you the size you specified.

### Task 3: Move Robot to Image Capture Position
1. Captures an image and detects the ArUco marker corners
2. Use the following seetings on the joint values in user coordinate system 0. The 0 coordinate system is mounted in the base of the robot. 
	J1  90
	J2   0
	J3 -50
	J4 -40
	J5  90
	J6 -90 or 270 depending on camera mounting position
3. Now, place the ArUco marker flat on the workspace in the bottom left corner of the camera view. Make sure you se the hole marker.
4. Run the capture section and it will show you an image with the ArUco marker.

### Task 4: Verification of your Calibration
1. Place an object on the workspace within the cameras view.
2. Take a ruler and measure the distance from the lower left corner of the ArUco to the center of the marker.
3. At the top of the section find **MANUAL_MEASUREMENT_MM = 130 # <-- CHANGE THIS** enter the correct measurement in mm.
4. Run the verification section to capture an image and find the object's pixel position
5. The program will show an image where it marked the marker and the calculated distance.
6. Is the error between the measured and the calculated acceptable for a suction cup? (hint: ±5–10 mm is usually fine)

