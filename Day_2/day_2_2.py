def my_turn(my_choice):
    if my_choice == "Y": #draw
        if line[0] == "A":
            return 4
        if line[0] == "B":
            return 5
        if line[0] == "C":
            return 6
    if my_choice == "X": #lose
        if line[0] == "A":
            return 3
        if line[0] == "B":
            return 1
        if line[0] == "C":
            return 2
    if my_choice == "Z": #won
        if line[0] == "A":
            return 8
        if line[0] == "B":
            return 9
        if line[0] == "C":
            return 7


file = open('day_2.txt')
total = 0

while True:
    line = file.readline()
    if not line:
        break
    total += my_turn(line[2])


print(total)
file.close()