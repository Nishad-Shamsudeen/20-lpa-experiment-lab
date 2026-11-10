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
          # print(f"Iteration =={index+1}")
          for inner_index,emp_data in enumerate(row):
            print("Inner Loop Start")
            error ={}
            if inner_index==0:
               try:
                 emp_id=int(emp_data)
               except ValueError:
                 error["row"] = index+1
                 error["reason"] = "Emp Id Is Not a Valid Number" 
                 errors_list.append(error)
  
            if not emp_data: # Checking Employee Data Is Empty Or Not       
            
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
           
            
            print(f"Current CSV Row : {index+1}")
            print(f"Inner Index : {inner_index}")
            print(f"Employee Data : {emp_data}")
            print("")
            print("########## Append Before Validation #############")
            print(f"Error Before First Append : {error}")
            print(f"Error List First Append : {errors_list}")
            print(" ")
            if inner_index ==2 or inner_index ==3:
              # error ={}
              is_date=is_valid_datetime(emp_data)
              print(f"Date is valid? : {is_date}")
              print(f"Inner Index after Funtion call: {inner_index}")              
              if not is_date and inner_index==2:

                error["row"] = index+1
                error["validity reason"] = "Check In Time Is Not Valid"
                # print(f"Error Reason : {error["reason"]}")
                print(f"Current inner index before append:{inner_index}")
                print(f"Error Before append : {error}")
                
                errors_list.append(error)
                print(" ")
                print("########## After Validation Append #############")
                print(f"Error List After First Append : {errors_list}")

              elif not is_date and inner_index==3:
                error["row"] = index+1
                error["reason"] = "Check Out Time Is Not Valid"
                # print(f"Current inner index before append:{inner_index}")

                errors_list.append(error)
            print("Inner Loop Ends")

            
      report['invalid_row']=invalid_row 
      report['errors']= errors_list     
      json.dump(report,json_file,indent=4)
# print(report)
     