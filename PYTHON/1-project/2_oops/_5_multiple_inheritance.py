class First:
    def display(self):
        print("First")

class Second:
    def display(self):
        print("Second")

class Third(Second,First):
    def diplay_third(self):
        print("Third")

new_obj=Third()
# new_obj.diplay_third()
new_obj.display()
# Method resolution order
print(Third.mro())
