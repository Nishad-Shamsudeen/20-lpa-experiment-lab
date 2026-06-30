#function without arg without return value
def sum():
    num=10
    num2=11
    sum=num+num2
    print("sum ="+str(sum))


#function without arg with return value
def sum1():
    num=10
    num2=11
    sum=num+num2
    return ("sum ="+str(sum))

#function with arg without return value
def sum2(num,num2):
    sum=num+num2
    print("sum ="+str(sum))

#function with arg with return value
def sum3(num,num2):
    sum=num+num2
    return ("sum ="+str(sum))

#  __name__ == "__main__"  used to avoid execute all line.
# Only allowed required function to be called.
if __name__ == "__main__":
    sum2(11,12)
    print(sum1())
    sum()
    print(sum3(1,12))