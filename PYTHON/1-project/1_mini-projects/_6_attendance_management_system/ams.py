from dataclasses import dataclass
from typing import ClassVar

#Employee Class Creation
@dataclass
class Employee:
    emp_name:str
    department:str
    emp_id:int=0

    #shared counter used for employee ID
    _next_id:ClassVar[int]=1

    def __post_init__(self):
        self.emp_id = self._next_id
        Employee._next_id +=1

#Attendance Record Class Creation
@dataclass
class AttendanceRecord:
    emp_id:int
    check_in:str
    check_out:str
    attendance_id:int
    #shared counter used for Attendance ID
    _next_attendance_id:ClassVar[int]=0

    def __post_init__(self):
        self.attendance_id = self._next_attendance_id
        AttendanceRecord._next_attendance_id +=1

#Adding Employee Details
employees = {}
def add_employee():
    name = input("Enter Employee Name:")
    emp_department = input(f"Enter {name}'s Department:")
    emp = Employee(emp_name=name,department=emp_department)
    employees['emp_id']=emp.emp_id
    return employees
employees=add_employee()
print(employees)

