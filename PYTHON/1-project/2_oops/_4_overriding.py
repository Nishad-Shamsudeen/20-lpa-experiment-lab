class BaseClass:
    def __init__(self):
        print("Constructor working")
    def set_name(self,name):
        self.name=name
        print("Base class")

class Subclass(BaseClass):
   
#    Constructor overriding
    def __init__(self):
        print("Subclass Init")

        #calling baseclass __init__
        # Both below works the same,to keep the coading standard use super().__init__()
        BaseClass.__init__(self) # This will work ,calling constructor
        super().__init__()# This will work ,calling constructor
        

    # function overriding
    def set_name(self, name):
        
        super().set_name(name)#It will call the base class function
        self.name=name
        print("Sub class")
        # return super().set_name(name)
    def welcome(self):
     return "Welcome to subclass " +self.name
    
welcome_msg=Subclass()
welcome_msg.set_name("Nishad")
# print(welcome_msg.welcome())