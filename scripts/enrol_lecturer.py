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

with open('../Database/enrol_lecturer.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["enrol_id","lecturerid", "course_id"])
    enrol_id=1
    for lecturerid in range(520000001,520000101):

        num_courses = random.randint(1,5)
        choices = random.sample(range(0, len(courses)), num_courses)
        course_choices = []
        for choice in choices:
            writer.writerow([enrol_id,lecturerid, courses[choice]])
            enrol_id+=1