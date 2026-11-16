from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
att_record_json =BASE_DIR/"files"/"ams_att_record.json"
# new_data = {'employee_id': 2, 'attendance_id': 2, 'Check in': '11:11 11-11-2026', 'check out': '11:11 11-11-2026'}
with open (att_record_json,"r", encoding="utf-8") as file:
       data = json.load(file)
       print(data)
    #    data.append(new_data)
    #    with open(att_record_json,"w") as json_file:
    #           json.dump(data,json_file,indent=4)