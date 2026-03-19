# Timetable Conflict Detection System

A simple Python project that helps detect timetable conflicts in a school or college schedule.

This program allows the user to enter timetable details such as teacher, subject, section, classroom, day, and period, and then checks for possible conflicts.

## Features

* Add multiple timetable entries
* Store timetable data using Python dictionaries and lists
* Detect **teacher conflicts**
* Detect **classroom conflicts**
* Detect **section conflicts**
* Display all conflicts clearly

## Conflict Types Checked

### 1. Teacher Conflict

Checks whether the same teacher is assigned to different sections at the same day and period.

### 2. Classroom Conflict

Checks whether the same classroom is assigned to more than one section at the same day and period.

### 3. Section Conflict

Checks whether the same section has different subjects scheduled at the same day and period.

## Technologies Used

* Python

## How It Works

1. The user enters timetable details.
2. Each entry is stored in a list as a dictionary.
3. The program compares timetable entries.
4. If two entries have the same day and period, it checks for:

   * teacher conflict
   * classroom conflict
   * section conflict
5. Finally, it displays whether conflicts are found or not.

## Sample Input

```python
Teacher: Ravi
Subject: Maths
Section: A
Classroom: 101
Day: Monday
Period: 1

Teacher: Ravi
Subject: Physics
Section: B
Classroom: 102
Day: Monday
Period: 1
```

## Sample Output

```python
There are 1 conflicts in timetable
List of conflicts:
Same teacher: Ravi found in sections A and B at period 1 on Monday
```

## Learning Outcome

Through this project, I practiced:

* Python lists
* Python dictionaries
* nested loops
* conditional statements
* conflict checking logic
* solving a real-world scheduling problem

## Future Improvements

* Add a graphical user interface
* Save timetable data in a file
* Improve conflict reporting
* Add automatic timetable generation
