# Student Handout — Session 4: Work object calibration

## What You Will Do in this Session
1. Calibrate the work object for the robot
2. Draw segmentation masks around each object
3. Train an AI model to recognize your objects
4. Evaluate how well the model works

## Why using a work object coordinate fram
The work object (coordinate frame) is used so the robot knows how to translate what the camera sees (ArUco marker pose) into its own motion system. By createing the work object at the same location as the coorcinate system for the ArUco marker, the relation between the camera frame and TCP frame can be linked.

## Your Tasks

### Task 1: ArUco Calibration
1. Place the ArUco marker flat on the workspace

### Task 2: Create a work object
1. Attach the sharp pine to the robot vacium cup, either in the Dobot studio or using the buttoms on the robot.
2. In DOBOT studio, set the robot in online mode
3. In DOBOT studio, select **Settings** -> **User coordiate system**
4. Select the **Camera** coordinate system and press update using Three points settings. If **Camera** does not exist add a new system named **Camera**.
5. Jog or manually drag the robot to the exact bottom left corner/origin of the ArUco marker coordinate system origo and update the first position
6. Jog the robot straight out along the positive X-axis direction and adjust Y position if needed, compare with lines on paper. Update the second position
7. Jog the robot over into the positive Y-axis direction, adjust X position if neede and update the third position. Start from the second X position (unlike ABB)
8. Click Confirm and then Save. The robot calculates the new axes and applies the offset.

### TASK 2: Base position
1. Open the Jog menu
2. Jog to the following coordinates in the **Camera** coordinate system.
	X    0
    Y    0
    Z  250
    RX 180
    RY   0
    RZ  90
4. Set the robot in TCP mode.