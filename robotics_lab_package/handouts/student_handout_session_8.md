# Student Handout — Session 8: Full pipeline

## What You Will Do in this Session
1. Run the complete pipeline

## The Full Pipeline

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
- Hands **completely clear** of workspace during robot motion.
- Tell your partner before pressing "Run".

## Your Tasks

### Task 1: Run the Full Pipeline
1. Place **one** object in the workspace
2. Run the full pipeline section

### Task 2: Automated Pipeline
1. Go to the next section, **Automated pipeline**
2. Place **several** object in the workspace
3. Find the line **for i in range(1):** And replace **1** with the number of objects.
4. Run the Automated pipeline section

### Task 3: Final Demo
1. Set up your best arrangement
2. Demo your system to the teachers
3. Be prepared to explain:
   - How your pipeline works
   - What your success rate is
   - What the biggest source of error was


### Task 4: Information About Packing Down the Robot
1. Use the following seetings on the joint values
	J1    0 
	J2  125
	J3 - 92
	J4 - 90
	J5  135
	J6 -  4
