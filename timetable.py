timetable = []

while True:
    teacher = input("Teacher: ")
    subject = input("Subject: ")
    section = input("Section: ")
    classroom = input("Classroom: ")
    day = input("Day: ")
    period = int(input("Period: "))

    entry = {
        "teacher": teacher,
        "subject": subject,
        "section": section,
        "classroom": classroom,
        "day": day,
        "period": period
    }

    timetable.append(entry)

    choice = input("Do you want to add more? (yes/no): ")
    if choice.lower() == "no":
        break

print("\nFinal Timetable:")
for item in timetable:
    print(item)

conflict = []

for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):
        if timetable[i]["day"] == timetable[j]["day"] and timetable[i]["period"] == timetable[j]["period"]:

            # Teacher Conflict
            if timetable[i]["teacher"] == timetable[j]["teacher"] and timetable[i]["section"] != timetable[j]["section"]:
                conflict.append(
                    f"Same teacher: {timetable[i]['teacher']} found in sections {timetable[i]['section']} and {timetable[j]['section']} at period {timetable[i]['period']} on {timetable[i]['day']}"
                )

            # Classroom Conflict
            if timetable[i]["classroom"] == timetable[j]["classroom"]:
                conflict.append(
                    f"Same classroom: Room {timetable[i]['classroom']} is assigned to sections {timetable[i]['section']} and {timetable[j]['section']} at period {timetable[i]['period']} on {timetable[i]['day']}"
                )

            # Section Conflict
            if timetable[i]["section"] == timetable[j]["section"] and timetable[i]["subject"] != timetable[j]["subject"]:
                conflict.append(
                    f"Same section: {timetable[i]['section']} has different subjects {timetable[i]['subject']} and {timetable[j]['subject']} at period {timetable[i]['period']} on {timetable[i]['day']}"
                )

if len(conflict) == 0:
    print("No conflicts in your timetable")
else:
    print(f"There are {len(conflict)} conflicts in timetable")
    print("List of conflicts:")
    for i in conflict:
        print(i)v
