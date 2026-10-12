class Employee:
    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     return f"Employee(name='{self.name}')"

    def __str__(self):
        return f"Employee(name='{self.name}')"
emp1 = Employee("Nishad")
emp2 = Employee("Naima")

employees = ["Nishad", "Naima"]
print(employees)
# print(person_1)
# print(person_2)
# print(person_1 ==person_2)


    