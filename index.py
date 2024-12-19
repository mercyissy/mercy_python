# print("welcome to class")

# Type of commenting
# 1. Single line comment 
# 2. Multi-line comment

# single line comment or double line comment 
"""
Hello my people
"""
"""
"""

# Concatenation : is the method of joining two or more strings together

# print("Welcome to class" + "Mercy")

# age = 20
# print("Age:" + str(age))

# age = age + 1
# print("Age:" + str(age))

# Python variables
# Variable name
# Assignment operator
# Value

# student = 'Daniel'
# print(student)
# print('Welcome to class' + student)

# students = 'Daniel', 'Mercy', 'ope',
# print(students)

#Rules guiding varable declaration
# 1. variables name must start with a letter or underscore
# 2. variable name must be descriptive
# 3. variable name must not contain a space character
# 4. Avoid using any python keywords
   # camel casing
firstName ='dd'

   # snake casing
the_first_student = 'dd'

   # pascal casing
TheFirstStudent = 'dd'

#value
# Age =20

# Name ="Dike Mercy "
# Hobbie =" swimming "

# print(Name +  str(age) +  Hobbie)

# Assignment : search for other type of concatenation method

# Types pf variable declaration
# 1. single variable, single value
"""
name ='Dami' 
"""

# 2. single variable multiple values
'''
students= 'Daniel', 'Mercy', 'ope',
'''

# 3. Multiple variable single value
"""
x, y = 20
"""

'''
x, *y = 20, 34, 78
'''
N = 20
# print(f"+{N}")
# a) 20
# b) Error
# c) +20 
# d)21


# Python DATA TYPES
# 1.) Number type:
   # i. Integers e.g 10, 30, 343 int()
   # ii Float e.g 10.3, 34.55 float()
   # iii. Complex e.g 3 + 4j complex()

   # num = 3
   
   # print(type(num))
   # print(float(num))

# 2.) text type
   # strings str() e.g 'Dami' 

# 3.) Boolen Type bool() e.g True, False
# isMarried = False
# print(isMarried)

# print(str(isMarried))

# 4.) sequence type
  # i.) tuple  tuple() e.g ('Ope', 'Mercy', 34, True)
  # ii. List list()  e.g ('Ope', 'Mercy', 34, True)
  # len is know how many items are in the parental quote 
  # iii. Range range() e.g range(20)

# myTuple =('Ope', 'Mercy', 34, True)
# myList = ['Ope', 'Mercy', 34, True]
# print(tuple(myList))
# print(type(myList))

# var = range(20)
# var = range(1, 21)
# var = range(1, 21, 2)
# print(list(var))

# 5. Mapping type
   # i. dictionary dict() e.g {'name': 'Dami', 'age': 20}

# person1 = {
#       'name': 'Dami',
#       'age': 20,
#       'isMarried': True
#    }
# print(person1)

# 6. set types
  # i. set set() e.g {'Ope', 'Mercy', 'Daniel', 'Aliyah'}
# myset = {'Ope', 'Mercy', 'Daniel', 'Aliyah'}
# num = {9,4,5,7,6,3,2,2,1}
# print(myset)
# print(num)

# 7. Binary types
  # i. byte 
  # ii. byte array
    # Binary numbers
# print(bin(10))

# name = 'Dami' # ['D', 'a', 'm', 'i']
# print(ord('D'))
# print(chr(90))
# ord() will give out number while chr() will give out alphabet

# Read up on common python operators
# conditional statement

# Python Operators
# 1. Arithmentic (+, -, *, /, %, //, **)
# 2. Assignment operation e.g =, += (increment), -=(decrement), *=, /=, //=, **=
num = 2
# num += 5 # num = num + 5
# print(num)
# 3. Comparison operator e.g ==, !=, >, <, >=, <=
# conditional statement
# if num == 5:
#    print('num is 5')
# else:
#    print('num is not 5')   

# name = input('input your username: ')
# password = input('input your password: ')
# Confirm_password = input('confirm password: ')

# print(name, password)

# # password validation
# if(len(password) < 8 ):
#   print('your password must be greater than 8 characters')

# else: 

#    print('strong password')
#      # nested if/else
#    if(password == Confirm_password):
#        print('passwords match. contimue')
#    else:
#        print('password does not match')    

# 4. Logical operator => and, or, not
#      AND 
# A     B    result
# 1     1      1
# 0     1      0
# 1     0      0
# 0     0      0

#      OR
# A     B    result
# 1     1      1
# 0     1      1
# 1     0      1
# 0     0      0

#     NOT
# A       NOT A
# 1         0
# 0         1

username = 'Mercyissy'
password = '123456789'

# print('login')
# inp_user = input('username: ')
# inp_pass = input('password: ')
# if(inp_user == username and inp_pass == password):
#    print('login successful')
# else:
#    print('wrong username or password') 

# isMarried = True
# if(not isMarried):
#     print('You no try aswear')
# else:
#    print('You do wel. na man you be')

# 5. Membership operator => in, not in

favourite_dishes = ['yam', 'rice', 'pounded yam']
# print('rice' in favourite_dishes)

# 6. identity operator => is, is not

num = 4 
num2 = 4
# print(num is num2)

# A simple calculator
# value1 = float(input('First value: '))
# value2 = float(input('Second value: '))

# print(
#    '''
#       option;
#              1. Addition
#              2. subtraction
#              3. Division
#              #. Exit
#    '''
# )

# option = input('option: ')
# if option == '1':
#      result = value1 + value2
#      print(f'Result: {result}')

# elif option == '2':
#      result = value1 - value2
#      print(f'Result: {result}')

# elif option == '3':
#      result = value1 / value2
#      print(f'Result: {result}')

# elif option == '#': 
#      print('Goodbye...')
#      exit()

# else:
#    print('Invalid option!')     
     

# Assignment
# check if a number is odd or even 
# Build a USSD application 


# Python Strings
# Strings are sequence of characters. They can be enclosed in single quotes or double quotes
student_name = 'Daniel' #['D', 'a', 'n', 'i', 'e', 'l']
# #print(len(student_name)) 
# print(student_name[-6])
# # slicing
# print(student_name[:]) #'D', 'a', 'n'

# print(type(student_name))
# print(student_name.lower())
# print(student_name.upper())

expression = 'Daniel is a python programmer at SQI college of ICT'
# print(expression.capitalize())
# print(expression.title())

# print('1. What is the capital of Nigeria  a). Lagos b). Abuja')
# ans = input('Your answer: ')
# if ans.upper() == 'B':
#      print('Correct')
# else:
#    print('wrong')  

   # Assignment
   # how to grade a persons score when there is are multiple question  

# Strip() removes both leading and trailing whitespace

# print(len(expression.strip()))

# print(expression.count('Daniel'))

# print(len(expression.split()))

item = ['+234', '9017131043']
# print(''.join(item))
# print(expression.startswith('daniel'))
      
# print(expression.replace('Daniel', 'Aliyah'))

#   Assignment
# Escape characters

# Python collections/array
# list, tuple, set, dictionary

# List - ordered, mutable orn changeable, can be indexed, accept duplicate value
students = ['mercy', 'ope', 'daniel', 'aliyah', 'mercy']
# print(student[-4:-1])
# print(student[::-1])

# students[0], students[1] ='Abimbola', 'Abimbola'
# print(students)

# students.reverse()
# students.append('Abimbola')
# students.extend(['Abimbola', 'John', 'Shola'])
# print(students)

arr = [
    ['Banana', 'Apple', 'Orange', [23, 45]],
    ['Rice', 'Beans'],
    'Water',
    34,
    True 
]
# print(arr[0][3][1])

# students.remove('ope')
# students.pop(1)
# students.clear()
# students.insert(0, 'Abimbola')
# print(students)

# For loop
# for each_student in students:
   #  print('welcome,', each_student)
   #  print('--------------------------') 

# for x in range(20):
#     print(x)    

# info = []

# for x in range(5):
#     name = input(f'Name{x + 1}:')
#     info.append(name)

# print(info)

# for each in info:
#     print(each, 'is a member.')

students =['Ayo','Dele','Ade']
scores = [21, 23, 43]    
sum_score = sum(scores)
length = len(scores)
avg_score = sum_score/length
# print('Average score is', avg_score)

# print(min(scores))
# print(max(scores))

# for student, score in zip(students, scores):
#     print(f'{student} scored {score}')

# questions = [
#     '1. what is the capital of Nigeria a.) accra b.) lagos'
#     '2. what is the capital of Ghana a.) accra b.) lagos'
# ]
# answers = [
#     'b'
#     'a'
# ]
# for quest, ans in zip(questions, answers):
#     print(quest)
#     answer = input('Answer: ')
#     if answer.lower() == ans:
#         print('correct')
#     else:
#         print('wrong')    

# tuple: immutable or unchangeable, can be indexed, allows duplicate values, ordered
# tuple() or ()

# fruits = ('Banana', 'Orange', 'Apple', 'Orange')
# print(fruits[0:3])
# fruits[0] = 'watermelon'

# new = list(fruits)
# new[0] = 'watermelon'
# fruits = tuple(new)
# print(fruits)

# unpacking
#(first, second, *remaining) = fruits
#print(remaining)

# var = ('Favour')
# var2 = ('Favour',)
# print(typr(var))

# print(fruits.count('orange'))
# print(fruits.index('Apple'))

# list of tuple

# ques_and_ans = [
#     ('1. what is the capital of Nigeria a.) accra b.) lagos', 'b'),
#     ('2. what is the capital of Ghana a.) accra b.) lagos', 'a')
# ]

# for quest, ans in ques_and_ans:
   #  print(quest)
   #  print(ans)

    # set: immutable, unchangeable, can't be indexed, not ordered, does not accept duplicate value
    # set() 0r {}

fruits = {'Banana', 'Grape', 'Apple', 'Mango', 'Apple'}
# print(len(fruits))
# fruits.add('tomato')
# fruits.update(['tomato', 'watermelon'])
#fruits.remove('Grape')
#fruits.discard('Grape')
#print(fruits)

# {} => empty dctionary
# () => empty set

setA = {1, 3, 6, 7, 4, 2, 5, 9, 0, 8}
setB = {12, 13, 2, 1, 11}
setC = {1, 3, 4}

# print(setA.union(setB))
# print(setA.intersction(setB))
# print(setB - setA)
# print(setA.difference(setB))
# print(setA.symmetric_difference(setB))

# setA.intersection_update(setB)
# setA.symmetric_difference_update(setB)
# print(setA)

# print(setA.issuperset(setC))
# print(setC.issubset(setA))
# print(setC.isdisjoint(setB))

# Dictionary: ordered, changeable, does not allow duplicate
# dict(key=value) or {key:value}

phone = {
    'model':'Iphone16',
    'color':'Black',
    'rom':'128gb',
    'version':'ios18',
    'owner':{
        "name":'john doe',
        'address':'Lagos'
    }
}

# print(phone['color'])

#print(phone['owner']['name'])
# phone['model'] = 'Iphone18'
# phone['sold'] = True # can ne used to add another item 
# print(phone)

#print(phone.keys())

# for key in phone.keys():
#     print(key)

# for value in phone.values():
#     print(value)  

# 

ques_and_ans = {
   '1. what is the capital of Nigeria a.) accra b.) lagos':'b',
   '2. what is the capital of Ghana a.) accra b.) lagos':'a'
}

# for ques, ans in ques_and_ans.items():
#    print(ques)
#    user = input('answer ').strip()
#    if user.lower() == ans:
#        print('correct')
#    else:
#        print('wrong')

# x = 10
# while x>1:
#     print('Yo', x)
#     x -= 1


# students = []
# user = input('insert student name, press 1 to stop or enter to continue: ')
# while user != '1':
#     user = input('insert Name or 1 to stop: ')
#     students.append(user)

# print(students)     


   # Assignment
   # create a todolist then use delete and add function e.g .remove

# OOP
# Object Oriented Programming

# key principles of OOP
# 1. Class
# 2. Object

# CLASS
# class PhoneTemplate:
#     # State the properties and function
#     def _init_(self):

#         self.model = 'Iphone XR'
#         self.color = 'Blue'
#         self.state = True

#     def home(self):
#         user = input('''
#             1. make a call
#             2. switch on/off
#     ''')
#         if self.state:
#             if user == '1':
#                 self.make_a_call()
#             elif user == '2':
#                 self.switch_off_or_on()
#             else:
#                 print('Error')
#                 self.home()

#         else:
#             user = input('The phone is off. press 1 to switch on: ')
#             while user != '1':
#                 user = input('The phone is off. press 1 to switch on: ')
#             else:
#                 self.switch_off_or_on()


#     def make_a_call(self):
#         print(f'The {self.model} can make calls')

#     def switch_off_or_on(self):
#         if self.state:
#             print('switching off ...')
#             self.state = False
#         else:
#             print('switching on ...')
#             self.state = True
#         self.home()

# phone1 = PhoneTemplate()
# phone2 = PhoneTemplate()


# We can also change the phone model
# phone.model+ 'Iphone 15'
# print(phone.model)

# phone1.home()


# class Calculator:
#     def _init_(self):
#         self.name = 'Casio'

#     def calculate(self):
#         self.value1 = float(input('Value1: '))
#         self.value2 = float(input('value2: '))
#         option = input(
#             """
#             1. addition
#             2. subtraction
#             3. exit

#             """
#         )

#         if option == '1':
#             self.addition()
#         elif option == '2':
#             self.subtraction()
#         elif option == '3':
#             exit()
#         else:
#             print('Invalid option, Try again!: ')
#             self.calculate()

#     def addition(self):
#         print(f'Answer: {self.value1 + self.value2}')
#         user = input('press 1 to exit or enter to continue: ')
#         if user == '1':
#             exit()
#         else:
#             self.calculate()

#     def subtraction(self):
#         print(f'Answer: {self.value1 - self.value2}')
#         user = input('press 1 to exit or enter to continue: ')
#         if user == '1':
#             exit()
#         else:
#             self.calculate()


# mycalc = Calculator()
# mycalc.calculate()



# Parametized Function

# class Calculator:
#     def _init_(self):
#         self.name = 'Casio'

#     def calculate(self, value1:float, value2:float):
#         self.value1 = value1
#         self.value2 = value2
#         option = input(
#             """
#             1. addition
#             2.subtraction
#             3.exit

#             """
#         )

#         if option == '1':
#             self.addition()
#         elif option == '2':
#             self.subtraction()
#         elif option == '3':
#             exit()
#         else:
#             print('Invalid option, Try again!: ')
#             self.calculate()
            

#     def addition(self):
#         print(f'Answer: {self.value1 + self.value2}')
#         user = input('press 1 to exit or enter to continue')
#         if user == '1':
#             exit()
#         else:
#             self.calculate()

#     def subtraction(self):
#         print(f'Answer: {self.value1 - self.value2}')
#         user = input('press 1 to exit or enter to continue')
#         if user == '1':
#             exit()
#         else:
#             self.calculate()

# mycalc = Calculator()

# val1 = float(input('value 1: '))
# val2 = float(input('value 2: '))
# mycalc.calculate(val1, val2)

# Inheritance

class Parent:
   def __init__(self) -> None:
      self.surname = 'Tinubu'
      self.firstname = 'Ahmed'
      self.hobby = 'playing golf'

   def introduce(self):
       return(f'My name is {self.firstname} {self.surname}, I love {self.hobby}')  

# Father = Parent()
# Father.introduce()          

class Child(Parent):
   def __init__(self) -> None:
      super().__init__()
      self.firstname = 'Seyi'
      self.occupation = 'politician'

   def introduce(self):
      print(f'Hello everyone, My name is {self.firstname} {self.surname}, I am a {self.occupation}')
      #return super()..introduce()

      info = super().introduce()
      print(f'{info}, I am also {self.occupation}')   

   def run(self):
      print(f'{self.firstname} can run very fast')

# child1 = Child()
# child1.introduce()
# child1.run()

class Grandchild(Child):
   def __init__(self) -> None:
      super().__init__()
      self.firstname = 'Bola'
      self.hobby = 'swimming'

   def introduce(self):
      return super().introduce()
      # print(f'{self.firstname} {self.surname}, I love {self.hobby}')

# grand = Grandchild()
# grand.introduce() 



class user():
   def __init__(self, lastname, firstname, email,password) -> None:
      self.lastname = lastname
      self.firstname = firstname
      self.email = email
      self.password = password

   def info(self):
      return (f'Name: {self.firstname} {self.lastname}\nEmail: {self.email}')  

class staff(user):
   def __init__(self, lastname, firstname, email, password, staff_id, account_no) -> None:
      super().__init__(lastname, firstname, email, password)
      self.staff_id = staff_id
      self.account_no = account_no  

   def info(self):
      detail = super().info()
      print(f'Staff ID: {self.staff_id}\n{detail}\nAccount no: {self.account_no}')

# Ade = staff('Olatunji', 'Adetunji', 'olaade@gmail.com', '1235', '002', '123456789') 
# Ade.info()


# 1. python script - This is a python(.py) file with bunch of python syntax
# 2. python module - This is a python file that contains exportable functions, variables or class
# 3. python library - This is a folder  that contains bunch of modules


# import datetime
# from datetime import date
# import time
# import calendar
# from colorama import init, Fore,Back
# init()
# import pandas, numpy
import _sqlite3
import random

# mydate = datetime.date.today()
# print('loading....')
# time.sleep(2)
# print(mydate)

#print(Fore.RED + Back.GREEN + calendar.calendar(2024))
# print(Back.GREEN + calendar.calendar(2024))
# year 
#package installer for python (pip)

# val = random.randint(2349000000000,  2349099999999)
# print(val)

Fruits = ['Orange', 'Pineapple', 'Watermelon', 'Cherry', 'Mango']
# print(random.sample(Fruits, 3))
# print(random.choice(Fruits))
# random.shuffle(Fruits)
# print(Fruits)


# for gaming app
# numbers = list(range(0, 100))
# print(random.sample(numbers, 10))

# SQL 1
'''
DBMS -> Database management system
Two basic types of DBMS
1.  Relational DBMS (RDBMS)
- SQL(Structured Query Language)
Tables (row and columns)
e.g
mySchool Database
- student table
- teachingstaff table
- non Teachingstaff table
- expenditure table
- revenue table

# Application
- mySQL,  PostgreSQL, Oracle, MicrosoftSQL Server, IBM DB2, SQLite



2.  Non-Relational DBMS (NoSQL)
- Cluster -  a Group of Database
- Database - e.g  mySchool Database
- Collection - Group  of documents 
   e.g studentcollection
   [
     {  name: John, 
            age: 20, 
            gender: male
     }

     {  studentName: Ope, 
            age: 28, 
            gender: male
      }
   ]
- Document - The information  stored itself
   e.g   {  name: John, 
            age: 20, 
            gender: male
         }

# Application
- MongoDB, Cassandra, Redis, Couchbase, RavenDB, Firebase, CouchDB, RavenDB  
'''