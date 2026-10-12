#function without arg without return value
def sum():
    num=11
    num1=23
    sum=num+num1
    print("Sum =" + str(sum))


#function without arg with return value
def sum1():
    num1=11
    num2=33
    sum=num1+num2
    return sum

#function with arg without return value
def sum2(num,num2):
   sum=num+num2
   print("Sum is "+str(sum))

#function with arg with return value
def sum3(num,num2):
    sum = num+num2
    # return sum
    return __name__
#  __name__ == "__main__"  used to avoid execute all line.
# Only allowed required function to be called.
if __name__ == "__main__":
    # sum2(11,12)
    # print(sum1())
    # sum()
    # print(sum3(1,12))
    print("welcome")
else:
    print("turbo")
