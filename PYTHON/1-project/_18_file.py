# File writing
# "w" is one of the file mode or file opening mode
file=open("_19_new_test_file.py","w")
file.write("print('Nishad')")
file.close()

#Read a file by using "with"

# with is called a Context Manager
# It automatically handles opening and closing the file for you —
#  even if an error occurs in between. 

with open("_19_new_test_file.py","r") as file_1:
    print(file_1.read())

