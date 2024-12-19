# import random

# ticket_lottery = random.sample(range(0, 20), k=5)

# print("Provide 5 numbers from 0 to 20(one by one- separated by spacebars):")
# ticket_input = list(map(int, input().split()))

# tl = sorted(ticket_lottery)
# ti = sorted(ticket_input)

# for item in ti:
#     points = 0
#     if ((item <= len(ti)) and (item in tl)):
#             points += 1
#             #print("Item: {}, Lotto:{}, Points:{}".format(item, tl, points))
#     elif((item <= len(ti)) and (item not in tl)):
#             item += 1
#             continue
#     else:
#             break

# print("You got {} points in total".format(points))

import random

## Lotto Game Class ###
class LottoGame:
    def __init__(self):
        self.numbers = []
        self.winning_numbers = []

    def generate_winning_numbers(self):
        self.winning_numbers = random.sample(range(1, 50), 6)
        self.winning_numbers()

    def get_user_numbers(self):
        while len(self.numbers) < 6:
            try:
                num = int(input("Enter number {} (1-49): ".format(len(self.numbers) + 1)))
                if 1 <= num <= 49 and num not in self.numbers:
                    self.numbers.append(num)
                else:
                    print("Invalid number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play_game(self):
        self.generate_winning_numbers()
        print("Welcome to Lotto!")
        self.get_user_numbers()
        self.numbers()
        print("Your numbers:", self.numbers)
        print("Winning numbers:", self.winning_numbers)
        self.check_results()

    def check_results(self):
        matches = len(set(self.numbers) & set(self.winning_numbers))
        if matches == 6:
            print("Congratulations! You won the jackpot!")
        elif matches == 5:
            print("Congratulations! You won a prize!")
        elif matches == 4:
            print("Well done! You won a smaller prize.")
        elif matches == 3:
            print("Better luck next time!")
        else:
            print("Sorry, no match.")

## Main Function ###
def main(self):
    lotto = LottoGame()
    play_again = "y"
    while play_again.lower() == "y":
        play_again = input("Play again? (y/n): ")
        self.play_game()
    print("Thanks for playing!")

if __name__ == "__main__":
 main()

