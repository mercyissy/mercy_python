import re

def check_email(email:str):

    pattern = r'^\w+@\w+\.\w+$'
   
    mail = re.match(pattern, email)
    print(mail)

    if mail:
        print("Valid email")
    else:
        print('invalid email')

# inp = input('Email: ')

# check_email(inp)

def is_valid_password(password:str):
    pattern = r'^\d{8}$'

    passw = re.match(pattern, password)
    print(passw)

    if passw:
        print("Valid password")
    else:
        print('invalid password')

inp = input('Password: ')

is_valid_password(inp)