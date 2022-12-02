file = open('day_1.txt')
elves = []
current_elf = 0

while True:
    line = file.readline()
    if not line:
        break
    if line != "\n":
        current_elf += int(line)
    else:
        elves.append(current_elf)
        current_elf = 0

print(max(elves))
