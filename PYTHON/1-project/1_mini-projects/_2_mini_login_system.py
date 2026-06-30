stored_username = "admin"
stored_password = "Admin123"

empty_space =  False
count=0
logged_in = False
user_name =""
while count<3 :
    while not user_name : 
            user_name = input("Enter User Name :").lower()
            empty_space = " " in user_name

            if empty_space and user_name: 
               print("Space not allowed in user name")
               user_name =""
            else :
                break
    
    if not logged_in :
        password = input("Enter your Password")
        is_name_match = stored_username == user_name
        is_password_match = stored_password == password
        if is_name_match and is_password_match :
            print("Login Successfull")
            logged_in =True
            break
        else :
          print("Login Failed")
          count=count+1
          user_name =""
    if (logged_in) :
        break
if count==3 :
    print("Your account is blocked")
    # break
          
   





    