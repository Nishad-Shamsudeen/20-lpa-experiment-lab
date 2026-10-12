
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student('{self.name}','{self.grade}')"  # for developers

    # def __str__(self):
    #     return f"Student('{self.name}','{self.grade})"  # for users

my_student = Student("Nishad", "A+")

# print(my_student)        # calls __str__  → Nishad scored A+
nsd_string = repr(my_student)  # calls __repr__ → Student('Nishad','A+')
nsd_obj = eval(nsd_string)
print(type(nsd_obj))