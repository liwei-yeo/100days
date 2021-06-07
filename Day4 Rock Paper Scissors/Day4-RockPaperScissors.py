rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
options = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if choice <0 or choice >=3:
    print("Invalid number!")
else:
    print(options[choice])
    com_choice = random.randint(0,2)
    print("Computer chose: \n" + options[com_choice])
    result = choice - com_choice
    resultlist = ["Draw.", "You win.", "You lose."]
    print(resultlist[result])
