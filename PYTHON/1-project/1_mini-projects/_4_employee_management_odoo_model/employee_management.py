class Employee():
    emp_id = 100
    def __init__(self,name,department,salary):
        # self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.emp_id = Employee.emp_id

        Employee.add_emp()
 
    def increase_salary(self,salary):
        self.salary = self.salary + salary
       
    
    def change_department(self,new_department):
        self.department = new_department
    @classmethod
    def add_emp(cls):
        cls.emp_id = cls.emp_id + 1
        return cls.emp_id


employees = []
#Creating employee object
emp_1=Employee(name="Nishad",department="IT",salary=150000)
emp_2=Employee(name="Naima",department="Finance",salary=250000)
emp_3=Employee(name="NSD",department="Founder",salary=20000000)
employees = [emp_1, emp_2, emp_3]


emp_1.increase_salary(250000)

emp_2.change_department("CEO")

def display_info():
        result =""
        for employee in employees:
            
                result += (f"Employee Id :  EMP_ {employee.emp_id}\n"
                            f"Name : {employee.name } \n"
                            f"Department : {employee.department} \n"
                            f"Salary :{employee.salary} \n"
                            "\n")
                                 
        return result
print(display_info())

