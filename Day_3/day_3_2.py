file = open('day_3.txt')
total = 0
count = 0
elves_3 = []

while True:
    line = file.readline()
    if not line:
        break

    count += 1
    elves_3.append(line)
    if count == 3:
        for char in elves_3[0]:
            if char in elves_3[1] and char in elves_3[2]:
                num_char = ord(char)-96
                if num_char < 0:
                    num_char += 58
                total += num_char
                count = 0
                elves_3 = []
                break

print(total)
file.close()