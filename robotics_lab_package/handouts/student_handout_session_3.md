# Student Handout — Session 3: Inference and Calibration

## What You Will Do in this Session
1. Run your trained model on images and inspect the results

## The Core Problem
In this session we will test the image detection capability.

## Your Tasks

### Task 1: Setup Inference
1. Go to **3. Inference (session 3)**
2. Run the first section, it just loads the Roboflow project.
3. Run the second section which will register the functions that we will use in the next step.

### Task 2: Run Inference on Saved Images
4. Section three will run the inference on a pre-saved image, so run it.
5. Hopefully it will show an image with all parts detected and correctly labled.
6. In the next section you can change the level of inference. If you just run it it will try with 0.2, 0.5 and 0.8 as confidence thresholds.
7. **Try this:** Change the confidence threshold on the line marked `# TODO: adjust threshold`
   - Set it to `0.3` — what happens?
   - Set it to `0.95` — what happens?
   - Choose a good threshold: _______