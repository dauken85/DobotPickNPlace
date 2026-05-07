# Student Handout — Session 2: Annotation and Training

## What You Will Do Today
1. Upload your images to Roboflow
2. Draw segmentation masks around each object
3. Train an AI model to recognize your objects
4. Evaluate how well the model works

## Why Annotation Matters

The AI model learns **only** from the examples you give it. If you label objects sloppily, the model will segment objects sloppily. Your annotations are the ground truth.

## Your Tasks

### Task 1: Upload Images
1. Log into Roboflow at [app.roboflow.com](https://app.roboflow.com)
2. Open your group's project
3. Upload all your images from Session 1
4. Verify the upload count matches your images

### Task 2: Define Your Classes
Use these exact class names:
- `square`
- `rectangle`
- `circle`
- `triangle`

**Important:** Do not add extra classes unless the teacher says so.

### Task 3: Annotate
1. Select the **polygon annotation** tool (not bounding box!)
2. For each object in each image:
   - Click around the object boundary to create a tight polygon
   - Select the correct class name
   - Make sure the polygon follows the actual edge of the object
3. Annotation tips:
   - **Good:** Polygon tightly follows the object edge
   - **Bad:** Loose polygon with lots of empty space around the object
   - **Bad:** Polygon cuts through the object
   - Use more points for curved shapes (circles)
   - Use fewer points for straight edges (squares)

### Task 4: Train Your Model
1. Go to **Generate** → Create a new version
2. Use the default preprocessing and augmentation settings
3. Click **Train** and select the segmentation model
4. Training takes about 15–30 minutes — use this time for the discussion below

### Task 5: Evaluate
Once training is complete:
1. Go to the **Visualize** tab
2. Look at predictions on your test images
3. Fill in this table:

| Image | Objects Present | Objects Found | Correct? | Notes |
|-------|----------------|---------------|----------|-------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

### Task 6: Record Your API Key
Your model's API key: ________________________________
Your model version: ________________________________

(You will need these in Session 3)

## Discussion Questions (While Training)
- What would happen if we only had 10 images?
- What if we mislabeled circles as squares?
- How does the model know which part of the image is "background"?
- What is overfitting, and why does it matter?

## Notes Space
_Use this area to write down observations:_

