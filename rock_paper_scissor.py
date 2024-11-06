import random

print("Hi, Welcome to the Rock-Paper-Scissors game!\n\n")
print("you can choose rock,paper or scissor\nYou are playing against the computer\n\n")
print("Rock vs Scissor wins Scissor\nRock vs Paper wins Paper\nScissor vs Paper wins Scissor\n")



u_win = [(2, 1), (1, 3), (3, 2)]
c_win = [(1, 2), (3, 1), (2, 3)]

u = 0  
c = 0  


while u < 3 and c < 3:
    user = int(input("Enter a choice (rock:1, paper:2, scissor:3): "))
    if user not in [1, 2, 3]:
        print("Invalid input. Please choose 1, 2, or 3.")
        continue
    computer = random.randint(1, 3)
    print(f"Computer chose: {computer}")
    result = (user, computer)
    if user == computer:
        print("It's a tie!")
    elif result in u_win:
        u += 1
        print(f"You win this round! Your score: {u}, Computer score: {c}")
    else:
        c += 1
        print(f"Computer wins this round! Your score: {u}, Computer score: {c}")
if u > c:
    print(f"You win the game by {u} points!")
else:
    print(f"Computer wins the game by {c} points!")
