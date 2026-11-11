from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Employee:
    emp_name:str
    emp_id:int=0
    department=str

#shared counter used for employee ID
_next_id:
def __post

