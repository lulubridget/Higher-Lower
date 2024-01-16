from game_data import data
import random

winner = ""
final_score = 0
check_follower = ""
while check_follower == winner:
    A = data.pop(random.randint(0,len(data)-1))
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    B = data.pop(random.randint(0,len(data)-1))
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    if A["follower_count"]> B["follower_count"]:
        winner = "A"
    elif A["follower_count"]< B["follower_count"]:
        winner = "B"
        
    check_follower = input("Who has more followers? 'A' or 'B'").upper()
    if check_follower == winner:
        final_score+=1
        print(f"Right. Final score: {final_score}")
        continue
    else:
        print(f"Wrong. Final score:{final_score}")
        break



