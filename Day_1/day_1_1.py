file = open('day_1.txt')
elves = [0]

while True:
    line = file.readline()
    if not line:
        break
    if line != "\n":
        elves[-1] += int(line)
    else:
        elves.append(0)

print(max(elves)) #frist_task

sorted_elves = sorted(elves, reverse=True)
print(sum(sorted_elves[0:3])) #second_task
