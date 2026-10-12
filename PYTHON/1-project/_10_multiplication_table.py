number = input("Enter a number for multiplication table")
count = int(input("How many times you want to print the table"))

for i in range(1,count+1):
    result= i*int(number)
    print(str(i)+" X " + number + " = " + str(result))