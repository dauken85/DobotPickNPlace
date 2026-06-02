# Student Handout — Session 5: ArUco Calibration

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
1. **Measure the marker**: _______ mm
2. Find the line marked `# TODO: enter your measured marker size` in section 2.
3. Enter your measurement
4. Run the section, it will show you the size you specified.


### TASK 3: Base position
1. Open the Jog menu
2. Jog to the following coordinates in the **Camera** coordinate system.
	X    0
    Y    0
    Z  250
    RX 180
    RY   0
    RZ  90
4. Set the robot in TCP mode.
5. Run the capture section and it will show you an image with the ArUco marker.

### Task 4: Verification of your Calibration
1. Place an object on the workspace within the cameras view.
2. Take a ruler and measure the distance from the lower left corner of the ArUco to the center of the marker.
3. At the top of the section find **MANUAL_MEASUREMENT_MM = 130 # <-- CHANGE THIS** enter the correct measurement in mm.
4. Run the verification section to capture an image and find the object's pixel position
5. The program will show an image where it marked the marker and the calculated distance.
6. Is the error between the measured and the calculated acceptable for a suction cup? (hint: ±5–10 mm is usually fine)

