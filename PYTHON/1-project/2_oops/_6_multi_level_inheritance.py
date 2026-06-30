class First:
    def display(self):
        print("First Class")
class Second(First):
    def display_second(self):
        print("Second Class")
class Third(Second):
    def display_third(self):
        print("Third Class")

new_obj = Third()
new_obj.display()