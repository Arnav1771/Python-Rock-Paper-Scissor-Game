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

#Write your code below this line 👇
game_images=[rock,paper,scissors]
user_input=int(input("Type '0' for Rock,'1' for Paper or '2' for Scissors? '\n' "))
if user_input>=3 or user_input<0:
  print("you typed an invalid number")
else:
  print(game_images[user_input])
  computer_input=random.randint(0,2)
  print(f"computer chose: ")
  print(game_images[computer_input])
  
  if user_input==0 and computer_input==2:
    print("You wins")
  elif computer_input==0 and user_input==0:
    print("You lose")
  elif computer_input>user_input:
    print("You lose")
  elif user_input>computer_input:
    print("You win")
  elif computer_input==user_input:
    print("it is a draw")
