class SampleConstructor:
    year=2024
    def __init__(self,name,age,place): #Constructor works when the Object created
        # pass
        self.name = name
        self.age = age
        self.place = place
    
   

    def display(self):
        print("Name : " + self.name + "\n" 
              "Place : "+ self.place +"\n"
              "Age : "+str(self.age)+"\n"
              "Year : " +str(SampleConstructor.year))
        
    def add_age(self):
            self.age=self.age+1

    @classmethod #This is class method .it will be common for all the object that is created from the class
    def add_year(cls):
        cls.year=cls.year+1

    @staticmethod
    def fun_message():
         print("Welcome")
      

instance_1=SampleConstructor("Nishad",34,"Bengaluru")
instance_2=SampleConstructor("Naima",24,"Varkala")

SampleConstructor.fun_message()

instance_1.display()
print("---------")
instance_2.display()
print("---------")

SampleConstructor.add_year()
instance_1.add_age()
instance_2.add_age()
instance_1.display()
print("---------")
instance_2.display()

