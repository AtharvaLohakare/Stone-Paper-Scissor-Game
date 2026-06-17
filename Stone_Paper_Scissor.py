# rock = -1
# paper = 0
# Scissor = 1

import random

print("""
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

winning_message = ("Great Job!","You Defeated the Computer!" ,"Awesome!","Victory is yours!")
losing_messages = ("Computer wins!","Better luck next time!","You lost this round!","Try again!")


print("----------------------Rock Paper Scissor Game----------------------")



with open("UserName.txt") as f:
    user_name = f.read()

if user_name == "":
    user_name = input("Enter Your Name :")
    with open("UserName.txt" ,"w") as f:
        f.write(user_name)


print(f"Welcome! {user_name}\nMay the best move win\n")

choices = {"rock" : -1 , "paper" : 0 , "scissor" : 1}
rev_choices = {-1 : "rock" , 0 : "paper" , 1 : "scissor"}

wins = 0
losses = 0
draws = 0

while True:
    print("1. First to 3 wins")
    print("2. First to 5 wins")
    choice_mode = input("Select Mode :")
    if choice_mode == "1":
        mode = 3
        break
    elif choice_mode == "2":
        mode = 5
        break
    else:
        print("Invalid input")

round_no = 1

while wins < mode and losses < mode:
   
    print(f"\n----- Round {round_no} -----")

    computer_choice = random.choice((-1,0,1))
    user = input("Enter Your Choice :")
    user = user.lower()

    if user not in choices:
        print("Invalid Input")
        continue
    else:
        round_no += 1
        user_choice = choices[user]

        print(f"Computer Choice is {rev_choices[computer_choice]}")
        # print(f"Your Choice is {rev_choices[user_choice]}")

        if user_choice == computer_choice :
            print("Match is Draw\n")
            draws += 1

        else:
            if computer_choice == 1 and user_choice == -1:
                print(random.choice(winning_message),"\n")
                wins += 1
            elif computer_choice == 1 and user_choice == 0:
                print(random.choice(losing_messages),"\n")
                losses += 1 
            elif computer_choice == 0 and user_choice == -1:
                print(random.choice(losing_messages),"\n")
                losses += 1 
            elif computer_choice == 0 and user_choice == 1:
                print(random.choice(winning_message),"\n")
                wins += 1
            elif computer_choice == -1 and user_choice == 1:
                print(random.choice(losing_messages),"\n")
                losses += 1 
            elif computer_choice == -1 and user_choice == 0:
                print(random.choice(winning_message),"\n")
                wins += 1
            else :
                print("Incorrect Input")
            
print("\n----- GAME OVER -----")

if wins == mode:
    print(f"Congratulations {user_name}! You are the Winner 🏆")
else:
    print("Computer Wins! Better Luck Next Time 😄")


print("\n------ FINALSCORE ------")
print(f"{user_name} : {wins}")
print(f"Computer : {losses}")
print(f"Draws : {draws}")
print("------------------------")
print("Thanks for Playing")
