test="Global Test"
def check_scope():
    def do_local():
        test="this test is local "
    def do_non_local():
        nonlocal test
        test = "this test is non local"
    def do_global():
        global test
        test="this is global Test"

    test="default"
    do_local()
    print("test value after do_local : "+test)
    do_non_local()
    # test="test value is changes after calling do no local "
    print("test value after do_non_local : "+test)
    do_global()
    print("test value after do_global : "+test)

print("test value before do_global:: "+test)
check_scope()
print("test value after do_global:: "+test)