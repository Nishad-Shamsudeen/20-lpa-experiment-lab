def exception_handle(deviser):
    try:
        quotient = 10/deviser
        return str(10) + "is devisible by" + str(deviser)
    except:
        return "10 is not devisible by " + str(deviser)

print(exception_handle(0))