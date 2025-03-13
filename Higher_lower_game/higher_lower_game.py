import game_art

import os

import random
import game_database

print(game_art.game_logo)
score=0




def display_accountinfo(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name} ,and he is a {description} and from {country}"
def check_answer(guess,account_1,account_2):
    if followers_Count_1<followers_Count_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False
account_2=random.choice(game_database.data)
continue_flag=True
while continue_flag:
    account_1=account_2

    account_2=random.choice(game_database.data)
    while account_1==account_2:
        account_2 = random.choice(game_database.data)

    print(f"compare 1:{display_accountinfo(account_1)}")
    print(game_art.vs)
    print(f"compare 2:{display_accountinfo(account_2)}")
    guess=int(input("enter who has more followers 1 or 2: "))


    followers_Count_1=account_1["follower_count"]
    followers_Count_2=account_2["follower_count"]
    # print(followers_Count_1)
    # print(followers_Count_2)

    is_correct=check_answer(guess,followers_Count_1,followers_Count_2)




    os.system('cls')
    print(game_art.game_logo)

    if is_correct==True:
        score+=1
        print(f"you are right and score is {score}")
    else:
        print(f"you are wrong score is {score}")
        continue_flag=False