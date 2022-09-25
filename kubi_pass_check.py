def check_password(psw):
    import re
    if len(psw)<8:
       raise Exception("Password has to be 8 chars long")
    elif not re.search("[a-z]",psw):
        raise Exception("Password must  contain letters")
    elif not re.search("[A-Z]",psw):
        raise Exception("Password must contain capital letters")
    elif not re.search("[_@$]",psw):
        raise Exception("Password must contain special characters")

password ="$Pistachio35"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Password is valid")
finally:
    print("validation tamamlandı")
