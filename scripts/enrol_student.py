import csv
import os
import random

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

courses = []


openFile2 = open( "../Database/Courses.csv", "r")
csvreader = csv.reader(openFile2)

first = True
for row in csvreader:
    if first == True:
        first = False
        continue
    courses.append(row[0].strip())

with open('../Database/enrol_students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["enrol_id","student_id", "course_id"])
    enrol_id=1
    for studentid in range(620000001, 620100001):

        num_courses = random.randint(3,6)
        choices = random.sample(range(0, len(courses)), num_courses)
        course_choices = []
        for choice in choices:
            writer.writerow([enrol_id, studentid, courses[choice]])
            enrol_id+=1