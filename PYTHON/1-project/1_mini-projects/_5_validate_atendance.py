import csv,json
from pathlib import Path

attendance=[]


BASE_DIR =Path(__file__).resolve().parent
att_input = (BASE_DIR.parent/"files"/"attendance.csv")


json_file=BASE_DIR.parent/"files"/"attendance.json"

# BASE_DIR =Path(__file__).resolve().parent
# att_input = (f"{BASE_DIR}\\files\\attendance.csv")
# print(att_input)

# print(att_input.exists())
with open (att_input,"r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    rows = list(csv_reader)
    for row in csv_reader:
      print(row)
     
  