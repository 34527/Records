#Records Class exercises - Revision 1

class StudentMarks:
    def __init__(self):
        self.student_name = None
        self.student_mark = None

student_number = int(input("Please enter the number of students: "))

records = []

for count in range(student_number):
    records.append(StudentMarks())

for record in records:
    record.student_name = input("Please enter the student's name: ")
    record.student_mark = int(input("Please enter the student's test mark: "))


studentname = "Student Name"
mark = "Mark"
print("-" * 27)
print("{0:^14} {1:^10}".format(studentname, mark))
print("-" * 27)
for record in records:
    print("| {0:^10} | {1:^10} |".format(record.student_name, record.student_mark))
    print("-" * 27)
