# Student Handout — Session 7: Robot Pick and Place

## What You Will Do in this Session
1. Connect your vision pipeline to the robot arm
2. Pick objects using camera-guided coordinates

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
- Tell your partner before pressing "Run"

## Your Tasks

### Task 1: Robot Configuration
1. The first section contains calibration information.
2. It should be correct so we just have to run it.

### Task 2: Connect the Robot
1. Verify in Dobot Studio that the robot is enabled and mode is set to TCP.
2. Run section 2.
3. The output should show **Robot mode 5** and **Robot ready** at the end.

### Task 3: Connect the Robot
1. When it is ok run section 3 (step 3a)
2. In section 3b take notice of the VERIFY_Z value, it should NOT be negative. Negative means below the workplane.
3. Run section 3b.
4. Run section 3c and the TCP should point out where the 0.0 coordinate is, i.e. Above the bottom left corner of the ArUco.


### Task 4: Capture, Infer, Pick
1. Before running step 4 verify that the setting of all offsets in the jupiter notebook are 0.0.
2. The X_OFFSET = 0.0, etc. represents the tip of the TCP pointer.
3. But we start with 0.0 just to verify that it is working.
4. Run step 5.
5. The robot should:
    - move to above the marker
    - start to suck
    - move to the drop off position
    - stop sucking
    - move to the neutral position
6. Now, adjust the Z_OFFSET so we actually pick up the marker. The Z_OFFSET has to be lowered (into negative numbers) to adjust for using the suction tool without the TCP pointer.
7. You might have to tune the X and Y offsets to make up for measurement errors (lenses).
