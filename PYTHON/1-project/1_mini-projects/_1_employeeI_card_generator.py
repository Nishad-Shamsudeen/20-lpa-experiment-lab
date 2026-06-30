
companyName =input("Enter Company Name")
allottedEmployeeId=1000
employeeName=input("Enter Your Name")
eNameForMailId = employeeName.lower().replace(" ","")

# Operations & Logics
companyNameConverted = companyName.lower().replace(" ","")

# generates mail ID
emailid = eNameForMailId + "@" + companyNameConverted + ".com"

#company code 
companyCode = companyName.rsplit(" ")   # rsplit(" ") will split the string with " ",and return a splited array
companyCode = companyCode[0]

employeeId = companyCode + str(allottedEmployeeId)
# allottedEmployeeId = allottedEmployeeId+1 # increase employeeId



print("Employee Name :" + employeeName)
print("Company :" +companyName)
print("Employee ID :" + employeeId)
print("Email :" + emailid)