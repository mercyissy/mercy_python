class Calculator:
    def _init_(self):
        self.name = 'Casio'
  
    def calculate(self):
        try:
            self.val1 = int(input('value 1: '))
            self.val2 = int(input('value 2: '))
        
        except Exception as e:
            print(f'An error occurred: {e}')
        option = input(
                """
                1. Addition
                2. Subtraction
                3. Division
                4. Multiplication
                5. exit

                """
            )

        if option == '1':
                self.Addition()
        elif option == '2':
                self.Subtraction()
        elif option == '3':
                self.Division()
        elif option == '4':
                self.Multiplication()
        elif option == '5':
                exit()
        else:
                print('Invalid option, Try again!: ')
                self.calculate()
                

    def Addition(self):
        try:
            print(f'Answer: {self.val1 + self.val2}')
            user = input('press 1 to exit or enter to continue')
            if user == '1':
                exit()
            else:
                self.calculate()
        except Exception as e:
              print('Error occoured: {e}')
              self.calculate()

    def Subtraction(self):
        try:
            print(f'Answer: {self.val1 - self.val2}')
            user = input('press 1 to exit or enter to continue')
            if user == '1':
                exit()
            else:
                self.calculate()
        except Exception as e:
              print('Error occoured: {e}')
              self.calculate()

    def Division(self):
        try:
            print(f'Answer: {self.val1 / self.val2}')
            user = input('press 1 to exit or enter to continue')
            if user == '1':
                exit()
            else:
                self.calculate()
        except Exception as e:
              print('Error occoured: {e}')
              self.calculate()
    def Multiplication(self):
        try:
            print(f'Answer: {self.val1 * self.val2}')
            user = input('press 1 to exit or enter to continue')
            if user == '1':
                exit()
            else:
                self.calculate()
        except Exception as e:
              print('Error occoured: {e}')
              self.calculate()

mycalc = Calculator()
mycalc.calculate()

    