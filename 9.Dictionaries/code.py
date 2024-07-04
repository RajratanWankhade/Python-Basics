student_attendance = {"Rolf":96, "Bob": 90, "Anne":100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

attendance_values = student_attendance.values()
print(sum(attendance_values)/len(attendance_values))    

print("............Destructing_Variables..............")

x = 5, 11 #it can be a tuple
x, y = 5, 11 # short for assigning two variables
print(x,y)


print(list(student_attendance.items()))