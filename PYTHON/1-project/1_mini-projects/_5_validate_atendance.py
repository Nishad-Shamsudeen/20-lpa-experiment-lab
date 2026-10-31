import csv,json
from pathlib import Path
from datetime import datetime


report= {}
valid_row=0
invalid_row=0
errors_list = []

BASE_DIR =Path(__file__).resolve().parent
att_input = (BASE_DIR.parent/"files"/"attendance.csv")


json_file_loc=BASE_DIR.parent/"files"/"attendance.json"

def is_valid_datetime(date_string):
  try:
    datetime.strptime(date_string,"%d-%m-%Y %H:%M")
    return True
  except ValueError:
    return False

with open (att_input,"r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    rows = list(csv_reader)
    report['total_rows']=len(rows)
    # error ={}
    with open (json_file_loc,"w") as json_file:

      for index,row in enumerate(rows):
          print(f"Iteration =={index+1}")
          for inner_index,emp_data in enumerate(row):
            error ={}
            if inner_index==0:
               try:
                 emp_id=int(emp_data)
               except ValueError:
                 error["row"] = index+1
                 error["reason"] = "Emp Id Is Not a Valid Number" 
                 errors_list.append(error)
  
            if not emp_data:                
              # if inner_index==0:
              #   error["row"] = index+1
              #   error["reason"] = "Emp Id Is Empty"
              if inner_index==1:
                error["row"] = index+1
                error["reason"] = "Emp name Is Empty"
                errors_list.append(error)
              elif inner_index==2:
                error["row"] = index+1
                error["reason"] = "Check In Time Is Empty"
                errors_list.append(error)
              elif inner_index==3:
                error["row"] = index+1
                error["reason"] = "Check Out Time Is Empty"
                errors_list.append(error)

            if inner_index ==2 or inner_index ==3:
              is_date=is_valid_datetime(emp_data)
             
              # print()              
              if not is_date and inner_index==2:
                print(f"Inner Index={inner_index}")
                print(f"is date={is_date}")
                error["row"] = index+1
                error["reason"] = "Check In Time Is Not Valid"
                errors_list.append(error)

              elif not is_date and inner_index==3:
                error["row"] = index+1
                error["reason"] = "Check Out Time Is Not Valid"
                errors_list.append(error)
            
      report['invalid_row']=invalid_row 
      report['errors']= errors_list     
      json.dump(report,json_file,indent=4)
# print(report)
     