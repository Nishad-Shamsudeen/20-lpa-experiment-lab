column = 0
r=5
space=0
star=0
# total_point=""
for j in range(r):
     space = (r-(j+1))*2
     star = ((j+1)*2)-1
     
     for x in range(space+star):
        #  print(x)
      if(x<space):
        print(" ",end="")
      else :
         print("*",end=" ")
     print("\n")
    #  print("space"+str(star))