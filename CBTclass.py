quest_ans = {
    '1. What is the  capital of Nigeria a. Tokyo b. Abuja c. Accra': 'b',
    '2. What is the capital if Japan  a. Tokyo b. Abuja c. Accra': 'a',
    '3. what is the capital of Ghana a. Tokyo b. Abuja c. Accra': 'c',
}

student_db = []

def registerstudent():
    global student_db

    while True:
        info = {
            'fullname':input('Fullname: '),
            'score':0
        }
        student_db.append(info)
        user = input('press 1 to stop or enter to continue') 
        if user == '1':
            break
        else:
            continue

    print('Registration successful...')
    print(student_db)
    dashboard()

def dashboard():
        print( '''
        Welcome to myCBT APP
              
        1. Register student
        2. View Result
        3. Take Test
        #. Exit
        ''')
        option = input('option: ')
        if option == '1':
            registerstudent()
        elif option == '2':
            resultStatistic()
        elif option == '3':
            takeTest()
        elif option == '#':
            exit()
        else:
            print('Invalid option')
            dashboard()

def resultStatistic():
        global student_db
        scores = []
        if not  student_db:
            print('No student registered')
            registerstudent()

        print('Student Result....')
        for student in student_db:
            print(f'fullname: {student["fullname"]}\nscore: {student["score"]}')
            scores.append(student['score'])

        max_score =  max(scores)
        index_maxScore = scores.index(max_score)
        max_student = student_db[index_maxScore]
        print(f"{max_student['fullname']} got the highest score")



        min_score =  min(scores)
        index_minScore = scores.index(min_score)
        min_student = student_db[index_minScore]
        print(f"{min_student['fullname']} got the lowest score")


        mean_score = sum(scores)
        length = len(scores)
        mean_score = mean_score / length
        print(f"Mean score: {mean_score}")


def takeTest():
        global student_db
        if quest_ans:
            print('Questions are available')

            if student_db:
                print('Time to take the test...')
                for student in student_db:
                    print(f"{student['fullname']} its time for your test...")
                    for ques, ans in quest_ans.items():
                        print(ques)
                        user_ans = input('Answer: ')
                        if user_ans.strip().lower() == ans:
                          print('Correct')
                          student['score'] += 5
                        else:
                            print('Incorrect')

                    print(f"Test completed. Score = {student['score']}")

                print(student_db)
                dashboard()

            else:
                print('No students to take test')
                registerstudent()

        else:
            print('No questions available')
            dashboard()

dashboard()



class Exam:
    def __init__(self):
      self.quest_ans = {
           '1. What is the  capital of Nigeria a. Tokyo b. Abuja c. Accra': 'b',
           '2. What is the capital if Japan  a. Tokyo b. Abuja c. Accra': 'a',
           '3. what is the capital of Ghana a. Tokyo b. Abuja c. Accra': 'c',
           }
      student_db = []

    def dashboard(self):
        print( '''
        Welcome to myCBT APP
              
        1. Register student
        2. View Result
        3. Take Test
        #. Exit
        ''')
        option = input('option: ')
        if option == '1':
            self.registerstudent()
        elif option == '2':
            self.resultStatistic()
        elif option == '3':
            self.takeTest()
        elif option == '#':
            exit()
        else:
            print('Invalid option')
            self.dashboard()

def registerstudent(self):
        while True:
            info = {
            'fullname':input('Fullname: '),
            'score':0
               }
            self.student_db.append(info)
            user = input('press 1 to stop or enter to continue')
            if user == '1':
                break
            else:
                continue

        print('Registration successful...')
        print(self.student_db)
        dashboard()

def takeTest(self):
        
        if self.quest_ans:
            print('Questions are available')

            if self.student_db:
                print('Time to take the test...')
                for student in self.student_db:
                    print(f"{student['fullname']} its time for your test...")
                    for ques, ans in quest_ans.items():
                        print(ques)
                        user_ans = input('Answer: ')
                        if user_ans.strip().lower() == ans:
                          print('Correct')
                          student['score'] += 5
                        else:
                            print('Incorrect')

                    print(f"Test completed. Score = {student['score']}")

                print(self.student_db)
                self.dashboard()

            else:
                print('No student found kindly register students...')
                self.registerStudent()

def resultStatistic(self):
    
        scores = []
        if not  self.student_db:
            print('No student registered')
            self.registerstudent()

        print('Student Result....')
        for student in self.student_db:
            print(f'fullname: {student["fullname"]}\nscore: {student["score"]}')
            scores.append(student['score'])

        max_score =  max(scores)
        index_maxScore = scores.index(max_score)
        max_student = self.student_db[index_maxScore]
        print(f"{max_student['fullname']} got the highest score")



        min_score =  min(scores)
        index_minScore = scores.index(min_score)
        min_student = self.student_db[index_minScore]
        print(f"{min_student['fullname']} got the lowest score")


        mean_score = sum(scores)
        length = len(scores)
        mean_score = mean_score / length
        print(f"Mean score: {mean_score}")

        self.dashboard()


# test1 = Exam()
# test1.quest_ans.update({'4. What is the capital of Turkey a. Ankara b. Lace c. Buba': 'a'})
# test1.quest_ans = {'4. What is the capital of Turkey a. Ankara b. Lace c. Buba': 'a'}
# print(test1.quest_ans)

# test1.dashboard()

# test2 = Exam()
# print(test2.quest_ans)
