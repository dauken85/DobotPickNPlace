# Session 1 — System Overview, Safety, and Image Capture

## Learning Objectives
- Understand the full vision-to-pick pipeline
- Learn robot safety procedures
- Capture a high-quality image dataset for model training

## Duration: ~3 hours

## Required Materials
- [ ] Dobot Magician E6 powered on and homed
- [ ] Basler ACE2 camera connected and verified
- [ ] PC with Python environment and `pypylon` installed
- [ ] Geometric shape objects (squares, rectangles, circles, triangles)
- [ ] Consistent lighting setup
- [ ] `capture_images.py` script tested and working
- [ ] USB drive or shared folder for image backup

## Agenda

### Part 1: Welcome and Pipeline Overview (30 min)
1. Introduce the lab goal: "Teach a robot to see objects and pick them"
2. Walk through the pipeline diagram:
   - Camera captures image
   - Model segments objects in the image
   - Calibration converts pixel locations to physical coordinates
   - Robot moves to the object and picks it with suction
3. Explain what students will do in each session

### Part 2: Teacher Demo (15 min)
1. Run a live demo of the complete pipeline (using teacher's pre-trained model)
2. Show: camera view → segmentation overlay → pick point → robot picks object
3. Let students observe from a safe distance

### Part 3: Safety Briefing (15 min)
1. Emergency stop location and procedure
2. Keep hands clear of robot workspace during operation
3. Never modify robot speed or workspace limits
4. Always tell your partner before starting robot motion
5. Report any unusual robot behavior immediately
6. **Each student must acknowledge safety rules before proceeding**

### Part 4: Station Setup (30 min)
1. Each group powers on their robot and verifies homing
2. Connect Basler camera and run a test capture
3. Arrange the workspace: flat surface, controlled background
4. Position lighting to minimize shadows and reflections
5. Place a few objects and verify they are visible in the camera

### Break (15 min)

### Part 5: Image Capture (45 min)
1. Open `capture_images.py`
2. Teacher explains the script: what it does, what students can change
3. Students capture images with varied object arrangements:
   - Single objects centered
   - Multiple objects spread out
   - Objects close together (touching/overlapping)
   - Different orientations
   - At least 30–50 images per group
4. Save images in organized folders

### Part 6: Dataset Review (30 min)
1. Review captured images as a group
2. Discuss:
   - Are all objects clearly visible?
   - Is the lighting consistent?
   - Are there enough varied arrangements?
   - Which images would be hard for a model to interpret?
3. Delete unusable images, note areas for improvement

### Part 7: Wrap-up (15 min)
1. Recap: what makes a good training dataset
2. Preview Session 2: annotation and training
3. Backup all images to shared storage

## Teacher Notes
- If camera connection fails, have backup images ready on each PC
- Aim for 50–100 usable images per group
- Encourage students to think about edge cases: overlapping objects, shadows, partial occlusion
- If a group finishes early, have them capture additional challenging arrangements

## Key Concept to Emphasize
> The quality of your dataset directly determines the quality of your model. Garbage in, garbage out.
> Focus on the details or metrics that are important for sorting or identifying the correct objects. IE color is less important when sorting shapes, but shadows are critical to eliminate. 