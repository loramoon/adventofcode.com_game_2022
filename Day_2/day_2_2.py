def my_turn(my_choice):
    strategy = {}
    if my_choice == "Y":
        strategy = {"A": 4, "B": 5, "C": 6}

    if my_choice == "X":
        strategy = {"A": 3, "B": 1, "C": 2}

    if my_choice == "Z":
        strategy = {"A": 8, "B": 9, "C": 7}

    return strategy[line[0]]


file = open('day_2.txt')
total = 0

while True:
    line = file.readline()
    if not line:
        break
    total += my_turn(line[2])


print(total)
file.close()
