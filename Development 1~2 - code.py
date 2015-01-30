#Euan McElhoney
#27/01/15
#Records - Development exercise 1/2

class StudentResults:
    def __init__(self):
        self.student_name = None
        self.module1_mark = None
        self.module2_mark = None
        self.module3_mark = None
        self.module4_mark = None
        self.total_mark = None
        self.mean_comparison = None
        

records = []

student_number = int(input("please enter the number of students: "))

for count in range(student_number):
    records.append(StudentResults())

for record in records:
    record.student_name = input("Please enter a student's name: ")
    record.module1_mark = int(input("Please enter their module 1 mark: "))
    record.module2_mark = int(input("Please enter their module 2 mark: "))
    record.module3_mark = int(input("Please enter their module 3 mark: "))
    record.module4_mark = int(input("Please enter their module 4 mark: "))
    record.total_mark = record.module1_mark + record.module2_mark + record.module3_mark + record.module4_mark

mean_total = int("0")
for record in records:
    mean_total = mean_total + record.total_mark


mean = mean_total / student_number
mean = round(mean)

for record in records:
    record.mean_comparison = record.total_mark - mean

    
    

print()
print()
print("-" * 81) 
print("| Name | module 1 | module 2 | module 3 | module 4 | total | distance from mean |")
for record in records:
    print("-" * 81)
    print("| {0:^4} | {1:^8} | {2:^8} | {3:^8} | {4:^8} | {5:^5} | {6:^18} |".format(record.student_name, record.module1_mark, record.module2_mark, record.module3_mark, record.module4_mark, record.total_mark, record.mean_comparison))
    
print("-" * 81) 
