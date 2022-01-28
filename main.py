import random

operator = ["rock","paper","scissors"]
computer = random.choice(operator)
user = input("enter your choice (rock, paper, scissors): ")

if user == computer:
    print("its a tie, you both choose" + " " + user)
    
def choice (u, c):
    if u == c:
        print("Its tie!")

    elif u == "rock":
        if c == "paper":
            print("You loose!", computer, "covers", user) 
                  
        else:
            print("You win!", user, "break", computer)

    elif u == "paper":
        if c == "scissors":
            print("You loose!", computer, "cuts", user ) 
        else:
            print("You win!", user, "cover", computer)

    elif u == "scissors":
        if c == "rock":
            print("You loose!", computer, "breaks", user)    
        else:
            print("You win!", user, "cuts", computer)      
choice(user, computer) 

if user not in operator:
    print("invalid operator")