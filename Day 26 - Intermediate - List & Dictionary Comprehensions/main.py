import pandas

# [new_item for item in list]

students = {
    "student": ['John', 'Jim', 'James', 'Tom', 'Tim', 'Jane', 'Bob', 'Bill'],
    "score": [67, 89, 54, 7, 17, 92, 66, 98]
    }


student_data_frame = pandas.DataFrame(students)
print(student_data_frame)


print("\n\n")
for (index, row) in student_data_frame.iterrows():
    # print(row)
    print(row.student)