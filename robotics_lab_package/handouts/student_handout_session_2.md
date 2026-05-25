# Student Handout — Session 2: Annotation and Training

## What You Will Do in this Session
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
3. Upload all your good images from Session 1

### Task 2: Define Your Classes
Use these exact class names:
- `square`
- `rectangle`
- `circle`
- `triangle`
- `hexagon`
- `ellipse`

**Important:** Do not add extra classes unless the teacher says so.

### Task 3: Annotate
1. Use the "Find objects with AI" when annotating for automatic image detection.
2. Select the class name from the list or enter it before pressing "Find Objects".
3. If it detects to many or to few, modify the confidence threshold.
4. Click save.
5. Repeat this for all images.


### Task 4: Train Your Model
1. Go to **Dataset** → **Train Model** -> **Custom Training**
2. Use 10% for validation and 10% for testing.
3. Use the default preprocessing and augmentation settings
4. Click **Train** and select the segmentation model
5. Training takes about 15–20 minutes


### Task 6: Record Your API Key
1. Click the settings cog in the left hand side menu -> API keys
2. Go to Jupiter and enter it under **2. Model training (session 2)**
3. Go to Projects in the left hand side menu
4. Select your project.
5. Under the model name it says: ID: <model-id>/<model version>
    Example: markers-uorw8/2
6. Enter the model-id under **2. Model training (session 2)**
7. Enter the version under **2. Model training (session 2)**

8. Run the section and inspect the output:
   - What class was detected?
   - What is the confidence score?
   - Where is the mask in the image?