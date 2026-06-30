test="global"
def check_scope():
    def do_local():
        test="this is local variable"
    def do_non_local():
        nonlocal test
        test="this is non local variable"
    def do_global():
        global test
        print(test)
        test ="this is global test"


    test ="default"
    do_local()
    print("test value after do local "+"'"+ test+"'")
    do_non_local()
    print("test value after do non local "+"'"+ test+"'")
    do_global()
    print("test value after do global "+"'"+ test+"'") 
# print(test)
check_scope()
# print("test value after do global "+"'"+ test+"'")
