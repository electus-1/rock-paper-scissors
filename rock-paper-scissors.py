import random
def return_rps(choice):
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
  if choice == 0:
     return rock
  elif choice == 1:
    return paper
  elif choice == 2:
    return scissors
  else:
    print("Acceptable inputs are 0, 1 and 2.")

def determine_winner(user_choice, computer_choice):
  if(user_choice == 0):
    if(computer_choice == 0):
      return "It's a draw"
    elif(computer_choice == 1):
      return "You lose"
    elif(computer_choice == 2):
      return "You win!"
  if(user_choice == 1):
    if(computer_choice == 0):
      return "You win!"
    elif(computer_choice == 1):
      return "It's a draw"
    elif(computer_choice == 2):
      return "You lose"

  if(user_choice == 2):
    if(computer_choice == 0):
      return "You lose"
    elif(computer_choice == 1):
      return "You win!"
    elif(computer_choice == 2):
      return "It's a draw"
    
while True:
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors or 3 to Quit.\n"))
  if user_choice == 3:
    break
  else:  
    computer_choice = random.randint(0, 2)
    print(f"{return_rps(user_choice)}\nComputer chose:\n{return_rps(computer_choice)}")
    print(determine_winner(user_choice, computer_choice) + "\n")
  