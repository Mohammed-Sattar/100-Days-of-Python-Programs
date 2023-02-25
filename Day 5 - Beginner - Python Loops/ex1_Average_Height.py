# Day 5 - Exercise 1 - Average Height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

count = sum = 0
for single_student in student_heights:
    sum += single_student
    count += 1

print(f"{round(sum/count)}")