import random
option=("rock","paper","scissors")
player=None 
computer=random.choice(option)

while player not in option:
 player=input("enter your choice (rock,paper,scissors):")
 print(f"player:{player}")
 print(f"computer:{computer}")

 if player==computer:
  print("it id ties")
 elif player=="rock" and computer=="scissors":
  print("you win")
 elif player=="paper" and computer=="rock":
  print("you win")
 elif player=="scissors" and computer=="paper":
  print("you win ")
 else:
  print("you lose")
  print("THANK YOU")