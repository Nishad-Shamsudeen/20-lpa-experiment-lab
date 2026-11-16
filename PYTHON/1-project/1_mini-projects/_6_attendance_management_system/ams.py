from dataclasses import dataclass
from typing import ClassVar
from datetime import datetime
from pathlib import Path
import json

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
    attendance_id:int=0
    #shared counter used for Attendance ID
    _next_attendance_id:ClassVar[int]=1

    def __post_init__(self):
        self.attendance_id = self._next_attendance_id
        AttendanceRecord._next_attendance_id +=1

BASE_DIR = Path(__file__).resolve().parent
att_record_json =BASE_DIR/"files"/"ams_att_record.json"

#Adding Employee Details
employees = {}
def add_employee():
    name = input("Enter Employee Name:")
    emp_department = input(f"Enter {name}'s Department:")
    emp = Employee(emp_name=name,department=emp_department)
    employees[f"emp_{emp.emp_id}"]=emp
    print(employees)
add_employee()
# add_employee()

def is_valid_datetime(date_string):
  try:
    datetime.strptime(date_string,"%H:%M %d-%m-%Y")
    return True
  except ValueError:
    return False

def is_valid_date(date_string):
  try:
    datetime.strptime(date_string,"%d-%m-%Y")
    return True
  except ValueError:
    return False

def add_attendance_record(emp_id):
    with open(att_record_json,"w") as json_file:
     att_record = []
     for i in employees :
        employee=employees[i]
        if emp_id==employee.emp_id:
           check_in = input("Enter Check in Time-HH:MM DD-MM-YYYY")
           is_check_in =  is_valid_datetime(check_in)
           print(f"is_check_in:{is_check_in}")
           if is_check_in:
            check_out =input("Enter Check out Time-HH:MM DD-MM-YYYY")
            is_checkout = is_valid_datetime(check_out)
            if is_checkout:
               attendance=AttendanceRecord(emp_id,check_in,check_out)
               print(f"Attendance Object:{attendance}")
               emp_attendance = {}
               emp_attendance["employee_id"]=emp_id
               emp_attendance["attendance_id"]=attendance.attendance_id
               emp_attendance['Check in']=attendance.check_in
               emp_attendance['check out']=attendance.check_out
               att_record.append(emp_attendance)
           else :
              print("Enter Valid Punch Time !")
              add_attendance_record(emp_id)
     json.dump(att_record,json_file,indent=4)


def validate_emp_id():
    #Checking Employee ID Valid or not
    try:
     emp_id=int(input("Enter Employee ID"))
     add_attendance_record(emp_id)
    except ValueError:
      print("Enter Valid Employee Id")
      validate_emp_id()
    
validate_emp_id()

def date_formater(date_str):
   date_obj = datetime.strptime(date_str,"%H:%M %d-%m-%Y")
   return datetime.strftime(date_obj,"%d-%m-%Y")

def track_attendance_record(emp_id,date):
  print("Function works")
  with open (att_record_json,"r", encoding="utf-8") as file:
    data = json.load(file)

    for emp_attendance in data:

       print(f"Employee Id:{emp_attendance['employee_id'] }")
       if emp_attendance['employee_id'] == emp_id:
          emp_att_date = emp_attendance['Check in']
          att_date = date_formater(emp_att_date)
          print(f"Attendance Format:{att_date}")
          print(f"Attendance Date from Input:{date}")
          if att_date == date:
             print("Employee Attendance Details is available")
            #  print(f"Employee Name:{emp_attendance}")
          
       else:
          print("Entered Employee have no attendance record")
    # print(f"Json File :{data}")
   
   
tracker_id=input("Enter Employee Id to check")

tracker_date=input("Enter attendance date to check DD-MM-YYYY")
is_date_valid = is_valid_date(tracker_date)
print(f"is_date_valid:{is_date_valid}")
if is_date_valid:
 track_attendance_record(tracker_id,tracker_date)
