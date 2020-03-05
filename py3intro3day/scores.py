#!/usr/bin/python3

with open("DATA/testscores.dat","r") as rfile:
    student_dict = {item.split(':')[0] : item.split(':')[1].strip() for item in rfile.readlines()}

grading = (['F']*75) + (['D']*8) + (['C']*6) + (['B']*6) + (['A']*6)
for student in student_dict:
    print(f"{student} {student_dict[student]} {grading[int(student_dict[student])]}")