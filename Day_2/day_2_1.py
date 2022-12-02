def my_turn(my_choice):
    strategy = {}
    if line[0] == "A":
        strategy = {"Y": 8, "X": 4, "Z": 3}

    if line[0] == "B":
        strategy = {"Y": 5, "X": 1, "Z": 9}

    if line[0] == "C":
        strategy = {"Y": 2, "X": 7, "Z": 6}

    return strategy[my_choice]


file = open('day_2.txt')
total = 0

while True:
    line = file.readline()
    if not line:
        break
    total += my_turn(line[2])


print(total)
file.close()
