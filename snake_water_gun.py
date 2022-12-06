import random

def game(resp, rand):
    if resp == rand:
        return "draw"
    elif (rand == "Snake"):
        if (resp == "Water"):
            return "loss"
        elif (resp == "Gun"):
            return "win"
    elif (rand == "Water"):
        if (resp == "Gun"):
            return "loss" 
        elif (resp == "Snake"):
            return "win"
    elif (rand == "Gun"):
        if (resp == "Snake"):
            return "loss"
        elif (resp == "Water"):
            return "win"

inp1 = input("Choose - Snake(s), Water(w) or Gun(g):  ")
if inp1 == "s":
    inp1 = "Snake"
elif inp1 == "w":
    inp1 = "Water"
elif inp1 == "g":
    inp1 = "Gun"
else:
    print("Wrong input. Please try again.")
    exit()

rand_var = random.randint(1,3)
if (rand_var == 1):
    inp2 = "Snake"
elif (rand_var == 2):
    inp2 = "Water"
elif (rand_var == 3):
    inp2 = "Gun"

print("Computer is choosing")

result = game(inp1, inp2)

print(f"\nYou chose {inp1}")
print(f"Computer chose {inp2}")

if result == "draw":
    print("\nThe grame ended in a draw")
elif result == "win":
    print("\nCongratulations! You won")
elif result == "loss":
    print("\nYou Lost :(")