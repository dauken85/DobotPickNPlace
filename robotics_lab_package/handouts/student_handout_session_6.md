# Student Handout — Session 4: Robot-Guided Pick and Place

## What You Will Do Today
1. Connect your vision pipeline to the robot arm
2. Pick objects using camera-guided coordinates
3. Test with mixed clutter and analyze failures

## The Full Pipeline (Running Today)

```
Camera captures image
       ↓
Model segments objects
       ↓
Pick point computed (pixel → mm)
       ↓
Robot moves to pick point
       ↓
Suction ON → Lift → Move to drop zone → Suction OFF
```

## Safety Reminder
- Emergency stop is at: _________________________________
- **Teacher must approve your first automated pick**
- Hands **completely clear** of workspace during robot motion
- Tell your partner before pressing "Run"

## Your Tasks

### Task 1: Pre-Flight Check
Before running any automated picks, verify:
- [ ] Camera is connected and capturing
- [ ] Model is loaded and detecting objects
- [ ] Calibration value is entered correctly
- [ ] Robot is homed and suction cup is working
- [ ] Drop zone is clear and defined
- [ ] Emergency stop is within reach

### Task 2: First Pick (Teacher Supervised)
1. Place **one** object in the center of the workspace
2. Run the full pipeline (the teacher will guide you)
3. Observe:
   - Where does the model say the object is?
   - Where does the robot go?
   - Does the suction cup land on the object?
4. Result: Success / Miss / Partial
5. If miss: estimate the error in mm: _______

### Task 3: Independent Picking
Run picks on your own. Log every attempt:

| Pick # | Object | Confidence | Position (mm) | Result | Notes |
|--------|--------|------------|---------------|--------|-------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |

**Success rate:** _______ / 10

### Task 4: Tuning
Try adjusting these parameters (one at a time!) and see the effect:
- **Confidence threshold:** Only pick objects above a certain confidence
  - Current: _______ → Changed to: _______ → Effect: _________________
- **Minimum area:** Ignore very small detections (noise)
  - Current: _______ → Changed to: _______ → Effect: _________________

### Task 5: Mixed Clutter Challenge
1. Place 5+ objects in a challenging arrangement
2. Try to pick all of them, one by one
3. Record:
   - Total objects: _______
   - Successfully picked: _______
   - Missed: _______
   - Misidentified: _______

### Task 6: Final Demo
1. Set up your best arrangement
2. Demo your system to the group
3. Be prepared to explain:
   - How your pipeline works
   - What your success rate was
   - What the biggest source of error was

## Reflection Questions
Answer these after completing the lab:

1. What was the most common reason for failed picks?

2. How accurate was your calibration? Good enough for suction, or not?

3. What would you change to make this system more reliable?

4. Could this system work in a real factory? What would need to be different?

5. What did you learn that surprised you?

## Notes Space
_Use this area to write down observations:_

