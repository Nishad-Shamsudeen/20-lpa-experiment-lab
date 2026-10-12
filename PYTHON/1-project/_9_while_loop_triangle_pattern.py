# column = 0
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

# ANOTHER PATTERN VERSION DONE WITH ONLY 2HR AFTER 2 MONTHS OF NO CODE PYTHON ON 12-08-26

# row = 5

# for j in range(row):
#     space = (row+2)-j
#     for k in range(space):
#      print(" ",end="")
#     #  if(k==(space-1)):
#     Star=((j+1)*2)-1
#     for L in range(Star):
#      print("*",end="")
     
#     print("\n")