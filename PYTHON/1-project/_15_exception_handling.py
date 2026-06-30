def exception_fun(devisor):
    try:
        quotient= 10/devisor
        # print(quotient= 10/devisor)
        return ("10 is divisible by " + str(devisor) + " and the quotient is " + str(quotient))
    except:
        return("10 cant devided by "+str(devisor))
print(exception_fun(2))


