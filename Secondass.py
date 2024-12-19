class Quiz:
    def __init__(self):
        self.allstudents = []
        self.studentscores = []
        self.questions = [
            ('1. What is the capital of Nigeria  a). Lagos b). Abuja'),
            ('2. What is the name of Osun State Governor? a.) Governor Adeleke b). Governor Bello'),
            ('3. What is the capital of Osogbo  a). Lagos b). Osun'),
            ('4. Who is the founder of SQI  a). Adeyemi Aderinto b). Abiodun Gbenga'),
            ('5. What year was SQI founded  a). 2002 b). 2008')
        ]
        self.answers = ['b', 'a', 'b', 'a', 'b']
    
    def add_student(self):
        """Function to collect student names."""
        num_users = int(input('How many users are taking the Test: '))
        for user in range(num_users):
            students = input(f'Name of Student {user + 1}: ') 
            self.allstudents.append(students)
    
    def conduct_test(self):
        """Function to conduct the quiz for each student."""
        for student in self.allstudents:
            print(f'{student}, Answer the following Questions Correctly:')
            scores = 0
            for question, correct_answer in zip(self.questions, self.answers):
                print(question)
                user_answer = input('Answer: ')
                if user_answer.lower() == correct_answer:
                    print('correct')
                    scores += 5
                else:
                    print('wrong')   
            self.studentscores.append(scores)

    def display_scores(self):
        """Display the final score for all students."""
        for student, score in zip(self.allstudents, self.studentscores):
            print(f'{student} scored {score}')
            print('-' * 50)

    def find_highest_and_lowest(self):
        """Find and display the highest and lowest scoring students."""
        max_score = max(self.studentscores)
        index_max = self.studentscores.index(max_score)
        print(f'Highest score is {max_score} by {self.allstudents[index_max]}')

        min_score = min(self.studentscores)
        index_min = self.studentscores.index(min_score)
        print(f'Lowest score is {min_score} by {self.allstudents[index_min]}')

    def calculate_average_score(self):
        """Calculate and display the average score of all students."""
        total_score = sum(self.studentscores)
        mean_score = total_score / len(self.studentscores)
        print(f'Average score is {mean_score:.2f}')

    def start_quiz(self):
        """Main method to run all functions."""
        self.add_student()
        self.conduct_test()
        self.display_scores()
        self.find_highest_and_lowest()
        self.calculate_average_score()

# Creating an instance of the Quiz class and starting the quiz
quiz = Quiz()
quiz.start_quiz()
