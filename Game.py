"""
This game will be in Player Vs. Computer
1. Game will run 10 times.
    i. If Majority winning goes to Computer, then winner will be Computer and vice-versa
    ii. If Computer and player draws the game, then user have a choice - whether to play or not
2. Game rules.
    i. Snake defeats Water
    ii. Water defeats Gun
    iii. Gun defeats Snake
    iv. If character same, then it will draw and point will not count
"""

import random
turns = 10

# Initailize the Count of Computer, player and Draw matches
comp_count = 0
player_count = 0
draw_count = 0

while not turns == 0 and not comp_count == 10 and not comp_count == 10 and not comp_count == 10:
    element = ["Snake", "Water", "Gun"]
    computer = random.choice(element)
    print("1. Snake\n2. Water\n3. Gun")
    player = int(input("Enter the number: "))
    if player == 1 and computer == element[0]:  # Draw by Snake - Snake
        print("Draw")
        draw_count += 1
    elif player == 2 and computer == element[1]:    # Draw by Water - Water
        print("Draw")
        draw_count += 1
    elif player == 3 and computer == element[2]:    # Draw by Gun - Gun
        print("Draw")
        draw_count += 1
    elif player == 1 and computer == element[1]:    # Player win-> Snake defeats Water
        print("Player Win")
        player_count += 1
    elif player == 2 and computer == element[2]:    # Player win-> Water defeats Gun
        print("Player Win")
        player_count += 1
    elif player == 3 and computer == element[0]:    # Player win-> Gun defeats Snake
        print("Player Win")
        player_count += 1
    elif player == 1 and computer == element[2]:    # Comp win-> Gun defeats Snake
        print("Computer Win")
        comp_count += 1
    elif player == 2 and computer == element[0]:    # Comp win-> Snake defeats Water
        print("Computer Win")
        comp_count += 1
    elif player == 3 and computer == element[1]:    # Comp win-> Water defeats Gun
        print("Computer Win")
        comp_count += 1
    else:
        print("Invalid number...")

    turns -= 1

print("Draw Match:", draw_count, "times")
print("Computer wins the Match: ", comp_count, "times")
print("Player wins the Match: ", player_count, "times")
print()
if comp_count < player_count:
    print("Player is the Winner...\nComputer is loser")
else:
    print("Computer is Winner...\nPlayer is loser")
