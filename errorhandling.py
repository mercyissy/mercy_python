# Two basic categories of error
# 1. runtime error 

# e.g 

# val1 = int(input("Value 1: "))
# val2 = int(input("Value 2: "))
# runtime error: if user enters a string instead of a number, this will throw an error
# print(f'Answer: {val1 + val2}')

# print('Done')

# 2. compile type error
#print(answer)

# try:
#     print(answer)

# except:
#     print('Error occured')

#     print('Anything else....')
# try:
#    val1 = int(input("Value 1: "))
#    val2 = int(input("Value 2: ")) 

# except:
#    print('Error occured')
# else:
#    print(f'Answer: {val1 + val2}')

# finally:
#    print('Anything else....')


try:
   val1 = int(input("Value 1: "))
   val2 = int(input("Value 2: ")) 
   # print(answer)
# except ValueError as v:
#    print(v)
# except NameError as n:
#    print(n)

except Exception as e:
   print(e)