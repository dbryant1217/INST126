# Consolidation Project

import random

# TODO Firgure out how to roll dice

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

# TODO Figure out how to tuple out

def check_tuple_out(dice):
    if dice[0] == dice[1] and dice[1] == dice[2]:
        return True
    return False

# Figure out how to play one turn
def play_turn():
    print("\nYour turn:")
    dice = roll_dice() 
    print("You rolled:", dice)
    
    # Check for "Tuple Out"
    if check_tuple_out(dice):
        print("TUPLE OUT!")
        return 0  
    # End the turn with 0 points
    
    # Find fixed dice that cannot be re-rolled
    fixed_dice = []
    if dice[0] == dice[1]:
        fixed_dice.extend([dice[0], dice[1]])
    elif dice[0] == dice[2]:
        fixed_dice.extend([dice[0], dice[2]])
    elif dice[1] == dice[2]:
        fixed_dice.extend([dice[1], dice[2]])

    # Print fixed dice
    if fixed_dice:
        print("Fixed dice:", fixed_dice)
    else:
        print("No fixed dice")

    # Let player reroll non fixed dice
    while True:

        non_fixed = [d for d in dice if d not in fixed_dice]
        if not non_fixed: 
            break

        print("Dice to reroll:", non_fixed)
        reroll = input("Do you want to reroll? (yes/no): ").strip().lower()
        
        if reroll == "yes":
            for i in range(len(dice)):
                if dice[i] not in fixed_dice:  
                    dice[i] = random.randint(1, 6)
            print("You rerolled:", dice)

            # Check for tuple out after reroll
            if check_tuple_out(dice):
                print("TUPLE OUT!")
                return 0
            
            # Update fixed dice when you reroll
            fixed_dice = []
            if dice[0] == dice[1]:
                fixed_dice.extend([dice[0], dice[1]])
            elif dice[0] == dice[2]:
                fixed_dice.extend([dice[0], dice[2]])
            elif dice[1] == dice[2]:
                fixed_dice.extend([dice[1], dice[2]])
            print("Updated fixed dice:", fixed_dice)
        elif reroll == "no":
            break
        else:
            print("Please type 'yes' or 'no'.")

    # Calculate and output score
    score = sum(dice)
    print("You scored", score, "points this round.")
    return score

# Main game loop
print("Welcome to the Tuple Out Dice Game!")
total_score = 0
target_score = 50  

# Set a target score to win

while total_score < target_score:
    print("\nYour total score is:", total_score)
    print("It's your turn!")
    score = play_turn()
    total_score += score 
    
    if total_score >= target_score:
        print("\nCongratulations! You scored", total_score, "points and won the game!")
        break
    
    # Ask if player wants to continue playing
    keep_playing = input("Do you want to continue playing? (yes/no): ").strip().lower()
    if keep_playing == "no":
        print("You've reached the end of the game, Congradulations! Your final score is:", total_score)
        break
    elif keep_playing != "yes":
        print("Invalid input. Exiting the game.")
        break