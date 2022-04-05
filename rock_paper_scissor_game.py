import random

print("""********************\n Welcome the ROCK, PAPER and SCISSORS game!!!!!!\n
  ********************""")

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
player_choice = input("What do you choose Type? Type 0 for Rock, 1 for Paper, 2 for Scissor:\n")
random_choice = random.randint(0,2)

if player_choice ==  str(random_choice):
  print("DRAW!!!")

elif (player_choice == '0') and  (str(random_choice) == '1'):
  print(f"{rock} \n {paper}\n COMPUTER WIN")
  
elif (player_choice == '0') and  (str(random_choice) == '2'):
  print(f"{rock} \n {scissors}\n YOU WIN")

elif (player_choice == '1') and  (str(random_choice) == '0'):
  print(f"{paper} \n {rock}\n YOU WIN")

elif (player_choice == '1') and  (str(random_choice) == '2'):
  print(f"{paper} \n {scissors}\n COMPUTER WIN")

elif (player_choice == '2') and  (str(random_choice) == '0'):
  print(f"{scissors} \n {rock}\n COMPUTER WIN")

elif (player_choice == '2') and  (str(random_choice) == '1'):
  print(f"{scissors} \n {paper}\n YOU WIN")

else:
  print("Please follow the game instructions!!!!")    