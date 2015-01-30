#Euan McElhoney
#27/01/2015
#Records - Revision exercise 3

class payrecord:
    def __init__(self):
        self.employee_name = None
        self.employee_number = None
        self.hours_worked = None
        self.pay_rate = None

record = payrecord()


record.employee_name = input("Please enter employee's full name: ")
record.employee_number = input("Please enter employee number: ")
record.hours_worked = float(input("Please enter the hours worked: "))
record.pay_rate = float(input("Please enter employee's rate of pay: "))

total_pay = record.hours_worked * record.pay_rate

print("Pay slip  ")
print("Name: {0}".format(record.employee_name))
print("Employee Number: {0}".format(record.employee_number))
print("Hours Worked: {0:.2s.f}".format(record.hours_worked,1))
print("Rate of Pay: £{0}".format(record.pay_rate))

print(total_pay)

    
