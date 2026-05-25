# Student Handout — Session X: Work object calibration

## What You Will Do in this Session
1. Calibrate the work object for the robot
2. Draw segmentation masks around each object
3. Train an AI model to recognize your objects
4. Evaluate how well the model works

## Why using a work object coordinate fram
The work object (coordinate frame) is used so the robot knows how to translate what the camera sees (ArUco marker pose) into its own motion system. By createing the work object at the same location as the coorcinate system for the ArUco marker, the relation between the camera frame and TCP frame can be linked.



## Your Tasks

### Task 1: Identify the ArUco marker coordinate system
1. Captures an image and detects the ArUco marker corners
2. Use the following seetings on the joint values
	J1 
	J2
	J3
	J4
	J5
	J6
2. Move the papper so the  ArUco marker coordinate system is in the bottom left corner. Make sure you se the hole marker.


### Task 2: Create a work object
1. Attach the sharp pine to the robot vacium cup, either in the Dobot studio or using the buttoms at the robot
2. In DOBOT STUDIEO Pro, set the robot in continus mode
3. In DOBOT studio, select **Parameter settings** -> **User coordiate systems**
4. Select the **CameraFr** and press update using Three points settings
5. Jog or manually drag the robot to the exact corner/origin of the ArUco marker coordinate system origo and update the first position
6. Jog the robot straight out along the positive **x** direction to the  ArUco marker coordinate system origo and update the second position
7. Jog the robot over into the positive Y-axis direction of the ArUco marker coordinate system origo and update the theird position. Start from the second **x** position (unlike ABB)
8. Click Calculate and then Save or OK. The robot calculates the new axes and applies the offset.
9. Set the robot in TCP mode
    


### Task x: Pack down the robot
1. Use the following seetings on the joint values
	J1    0 
	J2  125
	J3 - 92
	J4 - 90
	J5  135
	J6 -  4
