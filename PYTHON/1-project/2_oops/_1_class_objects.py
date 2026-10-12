class SampleClass:
    def class_funtion(self,arg):
        # self->current instance/current object
        self.name=arg #create/set that instance's name attribute
    def print_fun(self):
        print("Hi "+self.name+" Welcome to the world of the Robotics")

welcome_1=SampleClass()
# name="Nishad"
welcome_1.class_funtion("Nishad")
welcome_1.print_fun()
# The below is how objects works with class.the above is the modern way to write
welcome_2=SampleClass()
SampleClass.class_funtion(welcome_1,"Naima")
SampleClass.print_fun(welcome_1)