class SampleConstructor:
    year =2026
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def display(self):
        return ("Name is :" + self.name + "\n"
                "Age is :" + str(self.age) + "\n"
                "Place is :" + self.place + "\n"
                )
    # Class metod ,its common for each instance that is created from the class
    @classmethod
    def add_year(cls):
        cls.year= cls.year+1
        return cls.year
    # This function belongs to the class but does not need any class or object data
    # It just does its own job like a helper tool anyone can use
    @staticmethod
    def sample_function():
     return "This is the test function"

        # print("Testing Constructor")

instance_1=SampleConstructor("Nishad",28,"varkala")
instance_2=SampleConstructor("Naima",18,"varkala")
display=instance_1.display() 
display_2=instance_2.display() 
print(display)
print(display_2)
print("**************")
print(SampleConstructor.year)
print(SampleConstructor.add_year())
print(SampleConstructor.sample_function())