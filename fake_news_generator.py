# 1- import the random module

import random

# 2- Create subjects , actions and things_or_place

subjects = [
    "Salman Khan",
    "MsDhoni",
    "Jhon Sinha",
    "Modi",
    "Boy's Group",
    "Group of Monkey's",
    "Cab Driver From Bihar"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declars war on",
    "ordes",
    "celebrates"
]

things_or_places = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of Samosa",
    "inside Parliament",
    "at Ganga Ghat",
    "during IPL match",
    "at India Gate"
]

# 3- start the headline generatore loop

while True :
    subject = random.choice(subjects)
    action = random.choice(actions)
    thing_or_place = random.choice(things_or_places)

    headline = f"BREAKING NEWS : {subject} {action} {thing_or_place}"
    print("\n" + headline)

    user_input = input("\n Do you want another headline? (yes/no) : ").strip().lower()
    if user_input == "no" :
        break

# goodbye message
print("\n Thanks for using Fake News Generator. Have a fun day.")