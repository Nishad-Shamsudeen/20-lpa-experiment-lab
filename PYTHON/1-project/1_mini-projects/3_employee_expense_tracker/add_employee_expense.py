# CODE IS BROKEN NEED FIX-CURRENTLY MOVE ON TO BRO VDO
employees_data=[]
employee={}
def add_employee():
    add_more= ""
    name = input("Enter Employee Name")
    department = input("Enter "+ name +"'s Department Name")
    while True:
     try:
         expense = input("Enter expense amount")
         expense =int(expense)
         employee={"name":name,"department":department.lower(), "expense":expense}
        #  break
        #  return employee
     except:
         print("Invalid expense amount !")

     add_more = input("Do you wanna add more expense..?(Y/N)")
     if(add_more.lower()=="y"):
         continue
        #  break
        #  return add_employee()
        # add_employee()
     elif(add_more.lower()=="n"):
          return employees_data             
     else:
          print("Invalid selection!")

    employees_data.append(employee)
    
    # while True:
     
       
# employees_data1=[{'name': 'Nishad', 'department': 'sds', 'expense': 1}, {'name': 'dsd', 'department': 'cs', 'expense': 1}]
def show_all_expenses():
    # if len(employees_data) == 0:
    #    add_employee()
       result = ""
       for employee in employees_data:
           result =  result+("Name :"+employee.get("name")+"\n"
               "Department:"+employee.get("department")+"\n"
               "Expense:"+str(employee.get("expense")))+"\n"
       return result
    # else:
    #    result = ""
    #    for employee in employees_data:
    #        result= result + ("Name :"+employee.get("name")+"\n"
    #            "Department:"+employee.get("department")+"\n"
    #            "Expense:"+str(employee.get("expense")))+"\n"
    #    return result

def department_total_expense(department_name):
 total_sum=0
 for employee in employees_data:
      
      if employee.get("department") == department_name.lower():
        #  total_sum=0
         total_sum= total_sum + (int(employee.get("expense")))
 return "Total Expense: " + str(total_sum)
# print(show_all_expenses())
   
   
# print(add_employeeexpense())
# add_employeeexpense()nishad