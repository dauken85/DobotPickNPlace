# Student Handout — Session 1: Image Capture

## What You Will Do Today
1. See a live demo of a robot picking objects guided by a camera
2. Learn how to work safely around the robot
3. Capture images of objects that will be used to train an AI model

## The Big Picture

```
Camera  →  AI Model  →  "Object is here"  →  Robot picks it
(image)   (segmentation)  (coordinates)        (motion)
```

Today we focus on the **first step**: getting good images for the AI to learn from.

## Safety Rules
- **NEVER** put your hands in the robot workspace while it is moving
- Know where the **emergency stop** button is
- Always tell your partner before starting robot motion
- If anything looks wrong, **press the emergency stop**

## Your Tasks

### Task 1: Test the Camera
1. Open a terminal on your PC
2. Run: `python capture_images.py --test`
3. You should see a live preview from the camera
4. Verify the workspace is visible and well-lit

### Task 2: Arrange Objects
1. Place 3–5 geometric shapes on the workspace
2. Make sure they are clearly visible (not blending into the background)
3. Check the camera view — can you see all objects?

### Task 2B: Save Camera Robot Pose (Important)
1. In Dobot software, jog manually to the camera image-acquisition position
2. Keep the robot still at that position
3. Run: `python save_image_pose.py --output image_acquisition_pose.json`
4. Confirm `image_acquisition_pose.json` exists
5. Keep this file for Session 4 (robot returns to this pose before each snapshot)

### Task 3: Capture Images
1. Run: `python capture_images.py --save`
2. Each press of **SPACE** saves one image
3. Capture at least **50 images** with different arrangements:
   - [ ] Single object, centered
   - [ ] Single object, off-center
   - [ ] Two objects, separated
   - [ ] Three objects, close together
   - [ ] Five objects, mixed clutter
   - [ ] Objects touching each other
   - [ ] Different orientations (rotated)
4. Press **Q** to quit when done

### Task 4: Review Your Dataset
1. Open the image folder and browse through your captures
2. Delete any blurry, dark, or unusable images
3. Count your usable images: _______ (aim for 50+)

## Discussion Questions
- What makes a "good" training image?
- Why do we need many different arrangements?
- What would happen if all images looked the same?

## Notes Space
_Use this area to write down observations:_

