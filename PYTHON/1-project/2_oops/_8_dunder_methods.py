class Numbers():
    def __init__(self,val):
        self.value=val
    def __add__(self,other):
        result=self.value+other.value
        return result
    
    def __sub__(self, other):
        result=self.value-other.value
        return result
    
    def __mul__(self, other):
         result=self.value*other.value
         return result
    def __eq__(self, other):
             result=self.value==other.value
             return result
    def __lt__(self, other):
                 result=self.value<other.value
                 return result
    def __gt__ (self, other):
                     result=self.value<other.value
                     return result
   
number_1=Numbers(2)
number_2=Numbers(2)

print(number_1+number_2)
print(number_1-number_2)
print(number_1*number_2)
print(number_1==number_2)
print(number_1<number_2)
print(number_1>number_2)