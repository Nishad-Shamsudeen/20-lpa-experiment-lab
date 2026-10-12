def outer_fun():
    a=10
    b=20

    def inner_fun(c):
        print(a+b+c)

    return inner_fun

reference = outer_fun()
print("test")
print("test")
print("test")
print("test")
print("test")
print("test")
print("test")
print("test")
reference(88)
