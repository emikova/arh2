class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, email, pay):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, email, pay = emp_str.split('-')
        return cls(first, last, email, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Corey", "Scafer", "abc@gmail.com", 50000)
emp_2 = Employee("Ana", "Joy", "ana@gmail.com", 40000)
emp_3 = Employee("Jane", "Doe", "janedoe@gmail.com", 60000)

import datetime
my_date = datetime.date(2016,7,12)
print(Employee.is_workday(my_date))























#Employee.set_raise_amt(1.05)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)

#emp_str_1 = 'John-Doe-johndoe@gmail.com-7000'
#emp_str_2 = 'Steve-Smith-steve@gmail.com-30000'
#emp_str_3 = 'Ian-Malkovich-milkovich@gmal.com-50000'

#new_emp_1 = Employee.from_string(emp_str_1)
#print(new_emp_1.pay)

#new_emp_2 = Employee.from_string(emp_str_2)
#print(new_emp_2.email)