#creating a higher and lower game using python 
import random
import art
import game_data
game_over = False

print(art.logo)
while not game_over:
    score = 0
    random_item = random.choice(game_data.data)
    print(f"Compare A: {random_item['name']}, a {random_item['description']}, from {random_item[ 'country']} ")
    print(art.vs)
    random_item_2 = random.choice(game_data.data)
    print(f"Against B: {random_item_2['name']}, a {random_item_2['description']}, from {random_item_2[ 'country']} ")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n " * 10)

    a_followers = random_item_2['follower_count']
    b_followers = random_item_2['follower_count']

    if a_followers > b_followers:
        correct_answer = 'a'


    else:
        correct_answer = 'b'

    if answer == correct_answer:

        score += 1
        print(f"You are correct!, Current Score: {score}")



    else:
        print("You are wrong!")
        game_over = True





