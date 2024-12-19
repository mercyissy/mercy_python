import mysql.connector as sql

mycon =  sql.connect(
    host = '127.0.0.1',
    user = 'root', 
    password = '',
    database = 'august_cohort' 
)

mycursor = mycon.cursor()
mycon.autocommit = True
# DDL - data definition language

# mycursor.execute("CREATE DATABASE august_cohort")
# print('Database created')

# mycursor.execute("CREATE TABLE staff(staff_id INT PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50), email VARCHAR(50) UNIQUE, password VARCHAR(30), date_created DATETIME DEFAULT CURRENT_TIMESTAMP)")
# print('Table created')

# mycursor.execute('SHOW DATABASES')
# for db in mycursor:
#     print(db)


# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)

# mycursor.execute("ALTER TABLE staff ADD (gender VARCHAR(10), department VARCHAR(50))")
# print('column added')

# mycursor.execute("ALTER TABLE staff CHANGE gender sex VARCHAR(10)")
# print('column updated')

# mycursor.execute("ALTER TABLE staff DROP COLUMN department")
# print('column dropped')
# Show is not a part of query
# mycursor.execute("SHOW COLUMNS FROM staff")
# for column in mycursor:
#     print(column)

# mycursor.execute("DROP TABLE staff")
# print('Table dropped')

# mycursor.execute("DROP DATABASE aaugust_cohort")
# print('Database dropped')


# DML - data manipulation language
def register():
    fullname = input('Fullname: ')
    email =  input('Email: ')
    password = input('Password: ')
    sex = input('Gender: ')
    


    query = "INSERT INTO staff(fullname, email, sex,  password) VALUE(%s, %s, %s, %s)"
    values = (fullname,  email, sex, password)
    mycursor.execute(query, values)

    print('Registration successful')

#register()

def ChangePassword():
    email = input('Email: ').strip()
    prevPassword = input('Old Password: ').strip()
    newPassword = input('New Password: ').strip()

    query = "UPDATE staff SET password = %s WHERE password = %s AND  email = %s"
    val = (newPassword, prevPassword, email)
    mycursor.execute(query, val)
    print('Password changed')

#ChangePassword()    

def deleteAccount():
    user = input('Are you sure (y/n)').strip().lower()
    if user == 'y':
        print('Terminating Operation...')
    else:
        email = input('Email: ').strip()
        password = input('Password: ')

        query = "DELETE FROM staff WHERE email = %s AND password = %s"
        val = (email,password)
        mycursor.execute(query, val)
        print('Account Deleted!')

#deleteAccount()



# DQL - data query language

# mycursor.execute('SELECT * FROM staff WHERE staff_id = 1')
# details = mycursor.fetchall()
# print(details)

# mycursor.execute('SELECT * FROM staff WHERE staff_id = 1')
# details = mycursor.fetchone()
# print(details)


import pwinput

def login():
    email = input('Email: ')
    password = pwinput.pwinput()

    query =  "SELECT * FROM staff WHERE email = %s AND password = %s"
    val = (email, password)
    mycursor.execute(query, val)
    details = mycursor.fetchone()
    print(details) 
    if details:
        print(f'Welcome {details[0]},') 
    else:
        print('Incorrect email or Password')

login()


