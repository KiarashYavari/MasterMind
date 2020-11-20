import random

colors = {
    1: "red",
    2: "blue",
    3: "green",
    4: "yellow",
    5: "white",
}
print("choose your difficulty? 2 for esay , 4 for medium, 6 for hard")

limitation = int(input())
initial = []
while len(initial) < limitation:
    r = random.randint(1, 5)
    if r not in initial:
        initial.append(r)
initial = [colors[i] for i in initial]  # tabdile adadha be rang
# start of guessing the colors
win = False
# print(guess)
for turn in range(limitation):
    guess = input()
    guess = guess.split(",")
    white = 0
    black = 0
    for items in range(limitation):
        if guess[items] == initial[items]:
            black += 1
        elif guess[items] in initial:
            white += 1
    print("black: {}  white: {}".format(black, white))
    if black == limitation:
        win = True
        print("you won =))")
        exit()
if not win:
    initial_state = ",".join(initial)
    print("you lose =(( the colors were {}".format(initial_state))
