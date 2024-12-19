info = []
student_names = []
students_grade = []
student_score = []
# a_grade = []
# b_grade = []
# c_grade = []
# d_grade = []
# e_grade = []
# f_grade = []
# student_grade_a = []
# student_grade_b = []
# student_grade_c = []
# student_grade_d = []
# student_grade_e = []
# student_grade_f = []
with open(r'C:\Users\ADMIN\OneDrive\Desktop\mercy.py\student_grades.csv') as file:
    info = file.readlines()

    header = info.pop(0)
    info.pop(0)

with open('GradeA.csv', 'w') as file:
    file.write(header)
# print(info)


for data in info:
    data = data.strip('\n')
    data = data.split(',')
    # name = data[0]
    # score = data[1]
    # grade = data[2]
    # student_names.append(name)
    # student_score.append(score)
    # students_grade.append(grade)
    score = int(data[1])


# print(student_names)
# print(students_grade)
    if score >= 70 and score <= 100:
        data[2] = 'A'
        data = ','.join(data)
        
        with open('GradeA.csv', 'a') as gradeA:
            gradeA.write(data + "\n")

    elif score >= 60 and score <= 69:
        data[2] = 'B'
        data = ','.join(data)
        
        with open('GradeB.csv', 'a') as gradeB:
            gradeB.write(data + "\n")

            with open('details.csv', 'w', newline='') as files:
               writer = csv.writer(files)
               writer.writerows(data)


    elif score >= 55 and score <= 59:
            data[2] = 'C'
            data = ','.join(data)

            with open('GradeC.csv', 'a') as gradeC:
                 gradeC.write(data + "\n")

                 with open('details.csv', 'w', newline='') as files:
                    writer = csv.writer(files)
                    writer.writerows(data)
    elif score >= 45 and score <= 54:
            data[2] = 'D'
            data = ','.join(data)

            with open('GradeD.csv', 'a') as gradeC:
                 gradeC.write(data + "\n")

                 with open('details.csv', 'w', newline='') as files:
                    writer = csv.writer(files)
                    writer.writerows(data)
        
    elif score >= 40 and score <= 44:
          data[2] = 'E'
          data = ','.join(data)

          with open('GradeE.csv', 'a') as gradeE:
               gradeE.write(data + "\n")

               with open('details.csv', 'w', newline='') as files:
                    writer = csv.writer(files)
                    writer.writerows(data)
          
    else:
        data[2] = 'F'
        data = ','.join(data)

        with open('GradeF.csv', 'a') as gradeF:
               gradeF.write(data + "\n")

        with open('details.csv', 'w', newline='') as files:
               writer = csv.writer(files)
               writer.writerows(data)
        
        

# for a in range(len(students_grade)):
#     if students_grade[a] == 'A':
#         student_grade_a.append(f'{student_names[a]}, A')
# print('\nStudents With the A grade =>\n')
# for name_a in student_grade_a:
#     print(name_a)

# for b in range(len(students_grade)):
#     if students_grade[b] == 'B':
#         student_grade_b.append(f'{student_names[b]}, B')
# print('\nStudents With the B grade =>\n')
# for name_b in student_grade_b:
#     print(name_b)

# for c in range(len(students_grade)):
#     if students_grade[c] == 'C':
#         student_grade_c.append(f'{student_names[c]}, C')
# print('\nStudents With the C grade =>\n')
# for name_c in student_grade_c:
#     print(name_c)

# for d in range(len(students_grade)):
#     if students_grade[d] == 'D':
#         student_grade_d.append(f'{student_names[d]}, D')
# print('\nStudents With the D grade =>\n')
# for name_d in student_grade_d:
#     print(name_d)

# for e in range(len(students_grade)):
#     if students_grade[e] == 'E':
#         student_grade_e.append(f'{student_names[e]}, E')
# print('\nStudents With the E grade =>\n')
# for name_e in student_grade_e:
#     print(name_e)

# for f in range(len(students_grade)):
#     if students_grade[f] == 'F':
#         student_grade_f.append(f'{student_names[f]}, F')
# print('\nStudents With the F grade =>\n')
# for name_f in student_grade_f:
#     print(name_f)

# with open(students_grade, 'w') as file:
#     for line in info:
#         name, grade = line.strip().split(',')
#         student_names(name + '\n')
#         students_grade(grade + '\n')

# print("Student names and grades separated and written to different files.")

import csv



with open('GradeA.csv') as file:
     #data = csv.reader(file)
     data = csv.DictReader(file)
     print(data.fieldnames)
     print(list(data.reader))
     print(data)

     #print(list(data))

    #  for info in data:
    #       print(info)

# data = [
#      ['Name', 'Account Balance'],
#      ['Mercy Issy', 400000],
#      ['Holla Ope', 1000000],
#      ['Bims Abimbola', 2000000000]
# ]

# with open('details.csv', 'w', newline='') as files:
#      writer = csv.writer(files)
#      writer.writerows(data)

data = [
     
     {'Name': 'Mercy Issy', 'Account Balance': 400000},
     {'Name': 'Holla Ope', 'Account Balance': 1000000},
     {'Name': 'Bims Abimbola', 'Account Balance': 2000000000}
]

with open('details.csv', 'w', newline='') as files:
     writer = csv.DictWriter(files, fieldnames= data[0].keys())
     writer.writeheader
     writer.writerows(data)


