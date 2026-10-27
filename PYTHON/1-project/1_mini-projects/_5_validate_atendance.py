import csv,json
from pathlib import Path

attendance=[]

att_input=Path("../files/attendance.csv")
# json_file="../../1-project/files/attendance.json"

print(att_input.exists())
# with open (att_input,"r") as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)
#     print(header)