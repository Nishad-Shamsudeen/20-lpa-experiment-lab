import csv,json
from pathlib import Path

attendance=[]
report= {}
valid_row=0
invalid_row=0
errors_list = []

BASE_DIR =Path(__file__).resolve().parent
att_input = (BASE_DIR.parent/"files"/"attendance.csv")


json_file_loc=BASE_DIR.parent/"files"/"attendance.json"

with open (att_input,"r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    rows = list(csv_reader)
    report['total_rows']=len(rows)
    error ={}
    with open (json_file_loc,"w") as json_file:
      for index,row in enumerate(rows):
          for inner_index,emp_data in enumerate(row):
            if inner_index==0:
              #  emp_id=int(emp_data)
              #  print(emp_data)
               try:
                 emp_id=int(emp_data)
               except ValueError:
                #  print(f"{emp_data} cant be converted to number if it is alphabets")
                 error["row"] = index+1
                 error["reason"] = "Emp Id Is Not a Valid Number" 
                 errors_list.append(error)
  
            if not emp_data:
               invalid_row+=1
               break
            
      report['invalid_row']=invalid_row 
      report['errors']= errors_list     
      json.dump(report,json_file,indent=4)
    # print(report)  
      # print(row)
     
error ={}
error_list=[]
error['row']=1
error_list.append(error)
print(f"first append{error_list}")
error['row']=2
error_list.append(error)
print(f"first append{error_list}")
  