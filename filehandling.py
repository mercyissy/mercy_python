# MODE
'''
r => read only
w => write only
a => append 
x => create

'''

file = open(r'C:\Users\ADMIN\OneDrive\Desktop\mercy.py\timetable.py', mode='r', encoding="utf-8")
#print(file.read())
file.close()

# TO WRITE
# file = open('note.txt', mode='r')
# file.write('Hello Everyone (2)...')

# TO ADD TO AN EXISTING FILE
# file = open('note.txt', mode='a')
# file.write('Hello Everyone (2)...')

# file = open('issy.docx', mode='x')
# ANOTHER WAY TO OPEN A FILE
# with open(r'C:\Users\ADMIN\OneDrive\Desktop\mercy.py\timetable.py', mode='r', encoding="utf-8") as file:
#     print(file.read())
# AND THIS TO CLOSE IT
# print(file.read)

# Classwork

info = []
president_names = []
president_height = []

with open(r'C:\Users\ADMIN\OneDrive\Desktop\mercy.py\president_height.csv') as file:
    info = file.readlines()

info.pop(0)
#print(info)
for data in info:
    data = data.strip('\n')
    data = data.split(',')
    name = data[1]
    height = int(data[2])
    president_names.append(name)
    president_height.append(height)

data = max(president_height)
index_max = president_height.index(max(president_height))
print(president_names[index_max])


data = min(president_height)
index_min = president_height.index(min(president_height))
print(president_names[index_min])

length = len(president_height)
sum = sum(president_height)
mean_height = sum / length  
print('Average height is', mean_height)

# print(president_names)
# print(president_height)



