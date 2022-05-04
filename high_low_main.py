import random
import logo
import celeb_data

playing = True
image = logo.logo
vs = logo.vs
data = celeb_data.data

compare_a = data[random.randint(0, len(data))]
compare_b = data[random.randint(0, len(data))]

compare_a_followers = compare_a['follower_count']
compare_b_followers = compare_b['follower_count']

score = 0


print(image)

while playing:

    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
    players_pick = input("who has the most twitter followers ?: a or b?: ")

    if players_pick.lower() == 'a' and compare_a_followers > compare_b_followers:
        print("You're right! Current score: 1.")
        score = score +1
        compare_a = compare_b
        compare_a_followers = compare_b_followers

        compare_b = data[random.randint(0, len(data))]
        compare_b_followers = compare_b_followers
        print("______________________________________________-")


    elif players_pick.lower() == 'b' and compare_b_followers > compare_a_followers:
        print("You're right! Current score: 1.")
        score = score + 1
        compare_a = compare_b
        compare_b = data[random.randint(0, len(data))]
        print("_________________________________________________")

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        playing = False
