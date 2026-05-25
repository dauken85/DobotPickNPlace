# Student Handout — Session 1: Image Capture

## What You Will Do in this Session
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
1. Open Pylon viewer, connect the Basler camera
2. Activate the camera and capture an image or start a video feed.
3. You should see a live preview from the camera
4. Verify the workspace is visible and well-lit

### Task 2: Arrange Objects
1. Place 3–5 geometric shapes on the workspace
2. Make sure they are clearly visible (not blending into the background)
3. Check the camera view — can you see all objects?

### Task 3: Capture Images
1. Go to 1. Image Capture section in Jupiter notebook.
2. Go over and run the sections one by one.
3. At "Image Harvesting"; Capture at least **20 images** with different arrangements:
   - [ ] Single object, centered
   - [ ] Single object, off-center
   - [ ] Two objects, separated
   - [ ] Three objects, close together
   - [ ] Five objects, mixed clutter
   - [ ] Objects touching each other
   - [ ] Different orientations (rotated)
4. Continue and run the rest of the sections in Session 1.

## Discussion Questions
- What makes a "good" training image?
- Why do we need many different arrangements?
- What would happen if all images looked the same?
