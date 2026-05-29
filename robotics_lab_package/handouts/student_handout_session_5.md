# Student Handout — Session 5: Work object calibration

## What You Will Do in this Session
1. Calibrate the work object for the robot
2. Draw segmentation masks around each object
3. Train an AI model to recognize your objects
4. Evaluate how well the model works

## Why using a work object coordinate fram
The work object (coordinate frame) is used so the robot knows how to translate what the camera sees (ArUco marker pose) into its own motion system. By createing the work object at the same location as the coorcinate system for the ArUco marker, the relation between the camera frame and TCP frame can be linked.

## Your Tasks

### Task 1: Create a work object
1. Attach the sharp pine to the robot vacium cup, either in the Dobot studio or using the buttoms on the robot.
2. In DOBOT studio, set the robot in online mode
3. In DOBOT studio, select **Settings** -> **User coordiate system**
4. Select the **Camera** coordinate system and press update using Three points settings. If **Camera** does not exist add a new system named **Camera**.
5. Jog or manually drag the robot to the exact bottom left corner/origin of the ArUco marker coordinate system origo and update the first position
6. Jog the robot straight out along the positive **x** direction to the  ArUco marker coordinate system origo and update the second position
7. Jog the robot over into the positive Y-axis direction of the ArUco marker coordinate system origo and update the third position. Start from the second **x** position (unlike ABB)
8. Click Confirm and then Save. The robot calculates the new axes and applies the offset.
9. 

### TASK 2: Base position
1. Open the Jog menu
2. Jog to the following joint values.
	J1  90
	J2   0
	J3 -50
	J4 -40
	J5  90
	J6 -90 or 270 depending on camera mounting position
4. Set the robot in TCP mode.
    


### Task x: Information About Packing down the Robot
1. Use the following seetings on the joint values
	J1    0 
	J2  125
	J3 - 92
	J4 - 90
	J5  135
	J6 -  4
