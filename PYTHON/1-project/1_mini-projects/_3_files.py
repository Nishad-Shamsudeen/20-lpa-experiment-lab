import csv

employees =[
            ['Name','Age','Department'],
            ["Arun",28,"IT"],
            ["Sara",32,"HR"],
            ["Rahul",25,"Finance"],
            ["Amina",30,"Marketing"]
            ]

file_path =r"C:\Users\NSD\Desktop\employees.csv"

with open(file_path,"w",newline="") as file:
    writer =csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print("success")