def my_turn(my_choice):
    if line[0] == "A":  # Rock
        if my_choice == "Y": #Paper=2
            return 8
        if my_choice == "X": #Rock=1
            return 4
        if my_choice == "Z": #Scissor=3
            return 3
    if line[0] == "B": #Paper
        if my_choice == "Y": #Paper=2
            return 5
        if my_choice == "X": #Rock=1
            return 1
        if my_choice == "Z": #Scissor=3
            return 9
    if line[0] == "C": #Scissor
        if my_choice == "Y": #Paper=2
            return 2
        if my_choice == "X": #Rock=1
            return 7
        if my_choice == "Z": #Scissor=3
            return 6

file = open('day_2.txt')
total = 0

while True:
    line = file.readline()
    if not line:
        break
    total += my_turn(line[2])


print(total)
file.close()