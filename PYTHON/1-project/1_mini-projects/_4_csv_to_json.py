import csv,json

employees = []
file_destination ="C://Users//NSD//Desktop//employees.csv"
file_json ="C://Users//NSD//Desktop//employees.json"

with open (file_destination,"r") as file:
    csv_reader =  csv.reader(file)
    header = next(csv_reader)

    with open(file_json,'w') as file_json:
     for emp in csv_reader:
         emp_dict = {}
         for index,key in enumerate(header):
            emp_dict[key]=emp[index]
         employees.append(emp_dict)
     json.dump(employees,file_json,indent=4)
    #  json.dump("}",file_json)
print(employees)
