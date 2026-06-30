class BaseClass:
    def __init__(self):
        print("Constructor works when object is crete")
    def set_name(self,name):
            self.name=name
            print("Entered name is : ",self.name)


class SubClass(BaseClass):
    def default_fun():
         print("Testing")

new_obj = SubClass()
new_obj.set_name("Nishad")
