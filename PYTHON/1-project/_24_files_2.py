#-----Json--------#
import json

emp_data = {
                "name":"Nishad",
                "age":"46",
                "designation":"CEO of Billionaire Company"
           }

file_path = r"C:\Users\NSD\Desktop\new json.json"

with open(file_path,"w") as file:
    json.dump(emp_data,file,indent=4)
    print("success")

#-----CSV--------#

import csv

employees = [
                ['Name','Age','Designation'],
                ['Nishad',46,'CEO Of Billion Dollar Company'],
                ['Naima',36,'CFO']
            ]

file_path = r"C:\Users\NSD\Desktop\new json.csv"

with open(file_path ,'w',newline='') as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)

    print("Success")