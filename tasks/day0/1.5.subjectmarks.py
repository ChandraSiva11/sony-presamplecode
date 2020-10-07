stu1 = [40,50,70]
stu2 = [25,34,70]
stu3 = [24,34,20]

students = [stu1,stu2,stu3]
for student in students:
    fail = 0
    for mark in student:
        if (mark < 35):
            fail = 1
    # marks = ', '.join(student)
    if fail == 0:
        print('Subject marks ',student,' -> Prompted')
    else:
        print('Subject marks ',student,' -> Not Prompted')