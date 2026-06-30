class Sample():
    def set_name(self,name):
        self.name = name
    def __add__(self, other):
        full_name=self.name+" "+ other.name
        return full_name

first_name = Sample()
second_name = Sample()

first_name.set_name("Nishad")
second_name.set_name("Shamsudeen")
full_name = first_name + second_name 
print(full_name)