import re
password = input("Type your password: ")
if len(re.findall(r"\S",password)) > 6:
    if len(re.findall(r"\d",password)) > 1:
        if len(re.findall(r"\W",password)) > 1:
            if len(re.findall("[A-Z]",password)) > 1:
                print("Strong")
            else:
                print("Password must contain at least 2 capital letters")
        else:
            print("Password must contain at least 2 special characters")    
    else:
        print("Password must contain at least 2 numbers")
else:
    print("Password must contain at least 7 characters")
