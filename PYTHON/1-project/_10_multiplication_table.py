number = int(input("Enter a number for multiplication table"))
total_count = int(input("Number of Times"))

for i in range(1,total_count+1):
    result=number * i
    result = str(number) +" X "+str(i)+" = "+str(result)
    print(str(result),'\n')