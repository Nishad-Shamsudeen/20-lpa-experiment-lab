from dataclasses import dataclass
from typing import ClassVar
from datetime import datetime

@dataclass
class Employee:
    emp_name : str
    department : str
    title : str
    emp_id : int =0
     # Shared counter
    _next_id: ClassVar[int] = 1

    # Automatically assign the ID after initialization
    def __post_init__(self):
        self.emp_id = self._next_id
        Employee._next_id +=1
        # pass
@dataclass  
class AttendanceRecord:
    emp_id : int
    check_in : str
    check_out : str
    attendance_id : int =0

    _next_attendence_id:ClassVar[int]=1
    def __post_init__(self):
        self.attendance_id = self._next_attendence_id
        AttendanceRecord._next_attendence_id +=1

    def total_work_hours(self):
        # datetime.strptime(self.check_in,'%H:%M')
        work_hours = datetime.strptime(self.check_out,'%H:%M')-datetime.strptime(self.check_in,'%H:%M')
        return work_hours.total_seconds() / 3600
employees={}
emp_1 = Employee('Nishad','IT','Cloud Engineer')
emp_2 = Employee('Naima','Finace','CFO')

employees[emp_1.emp_id]=emp_1
employees[emp_2.emp_id]=emp_2

# day_1=AttendanceRecord(1, datetime.strptime('08:00', '%H:%M'), datetime.strptime('18:00', '%H:%M'))
day_1=AttendanceRecord(1,'08:00', '18:00')
day_2=AttendanceRecord(1,'08:00', '18:00')


print(day_1.total_work_hours())
attendance =[day_1,day_2]
def total_work_days():

    return len(attendance)

print(total_work_days())
# print(attendance)
# print(employees)

