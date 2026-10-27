try :
    user_input = input("enter any number")
    num=int(user_input)
except Exception as e:
    print(f"An Error occured:{e}")