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


