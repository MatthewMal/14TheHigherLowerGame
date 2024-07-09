from game_data import data
import random
import os


def format_data(account):
    acc_name = account["name"]
    acc_description = account["description"]
    acc_origin = account["country"]
    return f"{acc_name}, {acc_description} from {acc_origin}"


vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
current_score = 0
candidate_A = (data.pop(random.randint(0, len(data)-1)))

while len(data) > 1:
    candidate_B = (data.pop(random.randint(0, len(data) - 1)))
    if candidate_A['follower_count'] > candidate_B['follower_count']:
        winner = 'a'
    else:
        winner = 'b'
    # print(f"psst, the winner is {winner}")
    print(f'Compare A: {format_data(candidate_A)}')
    print(vs)
    print(f'Against B: {format_data(candidate_B)}')
    pick = input("\nWho has more followers? Type 'A' or 'B'': ")
    pick = pick.lower()
    while pick not in ['a', 'b']:
        pick = input("There was a miss-input. Please type either 'A' or 'B'!: ")
    if pick == winner:
        current_score += 1
        print(f"\nYou're right! Your current score is {current_score}.\n")
        candidate_A = candidate_B
    else:
        print(f"\nNope! Game over. Your score was {current_score}.")
        exit(0)

