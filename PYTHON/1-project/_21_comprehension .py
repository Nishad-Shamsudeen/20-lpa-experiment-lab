fruits = ["apple","kiwi","grapes","mang"]
new_fruits = []

new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

fruits_dictionary= {fruit:len(fruit) for fruit in fruits if "a" in fruit }
print(fruits_dictionary)
