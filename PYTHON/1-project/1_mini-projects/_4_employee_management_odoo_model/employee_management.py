class Employee:
    emp_id=100

    def __init__(self,name,department,salary):
        self.name = name
        self.department = department
        self.salary = salary
        self.emp_id = Employee.emp_id
        Employee.emp_id_generator()

    def increase_salary(self,increment):
        self.salary = self.salary+increment

    @classmethod
    def emp_id_generator(cls):
        cls.emp_id=cls.emp_id+1

emp_1=Employee("Nishad","Software-R&D",600000)
emp_2=Employee("Naima","CFO",600000)

employees = []
employees = [emp_1,emp_2]

for employee in employees:
    print(f"Employee Id :  EMP_ {employee.emp_id}\n"
                            f"Name : {employee.name } \n"
                            f"Department : {employee.department} \n"
                            f"Salary :{employee.salary} \n"
                            "\n")

print("####### Employees after salary increment #######")
emp_1.increase_salary(100000)
for employee in employees:
    print(f"Employee Id :  EMP_ {employee.emp_id}\n"
                            f"Name : {employee.name } \n"
                            f"Department : {employee.department} \n"
                            f"Salary :{employee.salary} \n"
                            "\n")



        