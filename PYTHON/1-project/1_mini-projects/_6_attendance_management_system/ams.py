from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Employee:
    emp_name:str
    emp_id:int
    department=str

    #shared counter used for employee ID
    _next_id:ClassVar[int]=0

    def __post_init(self):
        self.emp_id = self._next_id
        Employee._next_id +=1

@dataclass
class AttendanceRecord:
    emp_id:int
    check_in:str
    check_out:str
    attendance_id:int
    #shared counter used for Attendance ID
    _next_attendance_id:ClassVar[int]=0

    def __post_init(self):
        self.attendance_id = self._next_attendance_id
        AttendanceRecord.attendance_id +=1

