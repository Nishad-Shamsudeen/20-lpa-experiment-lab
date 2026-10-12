class InvalidSalaryError(Exception):
    pass
class ZeroSalaryError(Exception):
    pass
# def set_salary(salary):
#     if salary<0:
#         raise InvalidSalaryError("Salary cannot be negative")
#     return salary

try:
    salary = int(input("Enter Your salary"))
    if salary<0:
         raise InvalidSalaryError("Salary cannot be negative")
    elif salary==0:
        raise ZeroSalaryError("Salary cannot be Zero")
    else:print(salary)

    # print(salary)
except InvalidSalaryError as error:
    print (f"Error: {error}")
except ZeroSalaryError as error:
    print (f"Error: {error}")
except ValueError:
    print("Enter a valid salary")


