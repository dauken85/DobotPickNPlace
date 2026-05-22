# Session 4 — Robot-Guided Pick and Place

## Learning Objectives
- Connect the vision pipeline to the robot arm
- Execute automated pick-and-place from segmentation results
- Analyze failures and understand system limitations

## Duration: ~3 hours

## Required Materials
- [ ] All previous components working: camera, model, calibration
- [ ] `pick_logic.py` and `dobot_pick.py` scripts on each PC
- [ ] Dobot Magician E6 homed and suction tested
- [ ] Geometric shape objects in workspace
- [ ] Place mat or defined drop zone
- [ ] Emergency stop tested

## Agenda

### Part 1: Recap and Safety Review (15 min)
1. Recap the full pipeline: capture → segment → calibrate → pick
2. Safety refresher:
   - Emergency stop location
   - Hands clear of workspace during operation
   - Teacher must approve first automated pick at each station
3. Today's goal: make the robot pick objects guided by the camera

### Part 2: Teacher Verifies Each Station (30 min)
1. Teacher visits each station:
   - Run inference on a test image → verify mask quality
   - Check calibration value → verify with known measurement
   - Run a manual robot test move → verify safe motion
   - Test suction cup manually → verify it can hold the objects
2. Fix any issues before students begin automated picks

### Part 3: First Supervised Picks (30 min)
1. Place a single object in clear space
2. Run the pipeline step by step:
   - Move robot to saved image-acquisition pose from Session 1
   - Capture image
   - Run segmentation
   - Compute pick point (centroid in mm)
   - Send coordinates to robot
   - Robot moves, descends, activates suction, lifts, moves to drop zone, releases
3. **Teacher present for each group's first pick attempt**
4. **Student tasks:**
   - Observe the pick point on the image overlay
   - Compare where the robot goes vs where the object is
   - Record: success or failure, and why

### Break (15 min)

### Part 4: Independent Picking (30 min)
1. Students run picks independently
2. Start with single objects, then add complexity:
   - Two objects: pick the closest one
   - Three objects: pick in a specific order (e.g., largest first)
   - Objects near the edge of the workspace
3. **Student task:** Log a pick results table:

| Pick # | Object Class | Confidence | Position (mm) | Result | Notes |
|--------|-------------|------------|---------------|--------|-------|
| 1 | circle | 0.92 | (250, 180) | Success | — |
| 2 | square | 0.78 | (310, 90) | Miss | Off by ~8 mm |

### Part 5: Mixed Clutter Challenge (30 min)
1. Each group arranges a challenging scene:
   - 5+ objects, some touching, some overlapping
   - Different object types mixed together
2. Run the full pipeline and attempt to pick all objects
3. Discuss:
   - Which objects were picked successfully?
   - Which were missed or mis-identified?
   - Did overlapping objects cause problems?
   - Would a different pick order have worked better?

### Part 6: Final Demo (15 min)
1. Each group demonstrates their best pick sequence
2. Groups can choose their arrangement
3. Time for 2 minutes per group

### Part 7: Discussion and Wrap-up (15 min)
1. Collect pick success rates from all groups
2. Discussion questions:
   - What was the biggest source of error?
   - What would you change to improve reliability?
   - How would this differ in a real factory?
   - What happens when a new object type appears?
   - How would you handle 3D objects (not flat)?
3. Summary: what students learned across all 4 sessions
4. If applicable: preview of optional Session 5

## Teacher Notes
- The pick routine should have conservative speed limits
- Set the robot approach height well above the object, then descend slowly
- Pre-define a safe drop zone away from the pick area
- If `image_acquisition_pose.json` is missing or invalid, re-jog and re-save before continuing
- If the robot misses badly (>20 mm), recalibrate before continuing
- If a group's model fails consistently, switch to the backup model
- Keep spare objects in case some get damaged or lost
- Consider recording video of successful picks for the company

## Key Concept to Emphasize
> A working demo that fails sometimes is more educational than a perfect demo that hides the complexity. Understanding *why* things fail is the most valuable engineering skill.
