# Session 2 — Annotation and Model Training

## Learning Objectives
- Understand what segmentation annotation means
- Label objects with polygon masks in Roboflow
- Train a segmentation model and evaluate its quality
- Understand the difference between object segmentation and object detection

## Duration: ~3 hours

## Required Materials
- [ ] Roboflow account (one per group or shared organization)
- [ ] Roboflow project pre-created with correct settings (Instance Segmentation)
- [ ] Captured images from Session 1 (or backup dataset)
- [ ] Internet access on each PC
- [ ] Projector or shared screen for teacher demos

## Agenda

### Part 1: Recap and Introduction (15 min)
1. Quick recap: what we did in Session 1 and why
2. Introduce Roboflow: what it is, what it does
3. Explain the difference between:
   - Classification (what is this?)
   - Object detection (where is it? → bounding box)
   - Instance segmentation (where is it exactly? → pixel mask)
4. Show why segmentation is better for picking: we need the shape, not just a box

### Part 2: Upload and Organize (30 min)
1. Log into Roboflow
2. Upload images from Session 1
3. Review the upload: correct count, image quality preview
4. Discuss class naming:
   - Use simple, consistent names: `square`, `rectangle`, `circle`, `triangle`
   - Never use spaces or special characters in class names
   - All groups should use the same class names

### Part 3: Annotation (45 min)
1. Teacher demo: annotate 2–3 images live
   - Select the smart select tool
   - Trace around the object boundary
   - Assign the correct class
   - Show what a good vs sloppy annotation looks like
2. Students annotate their images
3. Teacher circulates to check annotation quality
4. Tip: tight polygons around the actual object edge, not loose approximations

### Break (15 min)

### Part 4: Train/Validation Split (15 min)
1. Explain what train, validation, and test splits mean
2. Let Roboflow auto-split or manually assign
3. Discuss: why you don't test on training data

### Part 5: Model Training (30 min)
1. Start a training run in Roboflow
2. While waiting, discuss:
   - What does the model learn?
   - What is an epoch?
   - What is overfitting?
   - What would happen with only 5 images?
3. Training typically takes 15–30 minutes in Roboflow

### Part 6: Evaluate Results (30 min)
1. Review model metrics: mAP, precision, recall
2. Teacher explains what each metric means in simple terms:
   - Precision: "When the model says it found a circle, how often is it right?"
   - Recall: "Of all the circles in the images, how many did the model find?"
3. Run predictions on test images in Roboflow
4. Look at:
   - Correct detections
   - Missed objects
   - False positives
   - Poor mask boundaries
5. Discuss what could improve the model

### Part 7: Wrap-up (15 min)
1. Each group presents their model results (2 min each)
2. Compare across groups: who got the best results and why?
3. Note the Roboflow API key — needed for Session 3
4. Preview Session 3: running the model on live images and calibration

## Teacher Notes
- Pre-create Roboflow projects so students don't waste time on setup
- Have a backup pre-annotated dataset in case annotation takes too long
- If training fails or takes too long, use a pre-trained model for the evaluation step
- Annotation quality is the single biggest factor — spend time here
- If a group has fewer than 30 annotated images, supplement with teacher-prepared images

## Key Concept to Emphasize
> A model is only as good as its annotations. Sloppy labels make a sloppy model — tighter, more accurate masks produce better segmentation.
