file = open('day_3.txt')
total = 0

while True:
    line = file.readline()
    if not line:
        break

    half = int((len(line)-1)/2)
    left_half = line[0:half]
    right_half = line[half:-1]
    for char in left_half:
        if char in right_half:
            num_char = ord(char)-96
            if num_char < 0:
                num_char += 58
            total += num_char
            break

print(total)
file.close()