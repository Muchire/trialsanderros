# rock paper scissors game
import random
while True:
   choices =["rock","paper","scissors"]

   computer = random.choice(choices)
   player = None
while player not in choices:
   player= input ("rock, paper or scissors?")
   if player==computer:
      print("computer:", computer)
      print("tie")
   elif player == "rock":
       if computer=="paper":
        print("computer:", computer)
        print("player:", player)
        print("you lose")
   if computer == "scissors":
        print("computer:", computer)
        print("player:", player)
        print("you win")
   elif player == "paper":
       if computer=="rock":
        print("computer:", computer)
        print("player:", player)
        print("you win")
        if computer == "scissors":
         print("computer:", computer)
         print("player:", player)
         print("you lose")
   elif player == "scissors":
       if computer=="paper":
        print("computer:", computer)
        print("player:", player)
        print("you win")
   if computer == "rock":
        print("computer:", computer)
        print("player:", player)
        print("you lose")
   play_again=input("play again?(yes/no):").lower()
#
#     if play_again != "yes":
#        break
print("bye")