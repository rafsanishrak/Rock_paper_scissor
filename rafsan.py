import random

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

game = [rock,paper,scissors]

user = int(input("What you're choosing? 0 for Rock, 1 for Paper, 2 for Scissors \n"))
print("You chose: \n")
if user >= 3 or user < 0:
  print("Invalid number, you lose.")

else:
  print(game[user])

  comp = random.randint(0,2)
  print("Computer Chose:")
  print(game[comp])



  if user == 2 and comp == 0:
    print("You lose, Computer wins.")

  elif user == 0 and comp == 2:
    print("You win !!!")

  elif user > comp:
    print("You win !!!")

  elif comp > user:
    print("You lose, Computer wins")

  elif user == comp:
    print("It's a draw, computer chose the same.")
