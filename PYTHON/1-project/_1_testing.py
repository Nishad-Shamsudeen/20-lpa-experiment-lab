employees_data=[
    {
   "name":"Nishad",
   "department":"IT",
   "expense":1
    },{
   "name":"Naima",
   "department":"IT",
   "expense":2
    }
           ]
def department_total_expense(department_name):
 total_sum=0
 for employee in employees_data:
      
      if employee.get("department") == department_name:
        #  total_sum=0
         total_sum= total_sum + (int(employee.get("expense")))
 return total_sum
print(department_total_expense("IT"))