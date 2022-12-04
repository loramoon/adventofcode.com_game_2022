file = open('day_4.txt')
total_task_1 = 0
total_task_2 = 0

while True:
    line = file.readline()
    if not line:
        break
    first_area, second_area = [], []
    first_range, second_range = line.split(",")
    first_range_start, first_range_end = [int(i) for i in first_range.split("-")]
    second_range_start, second_range_end = [int(i) for i in second_range.split("-")]

    for place in range(first_range_start, first_range_end + 1):
        first_area.append(place)
    for place in range(second_range_start, second_range_end + 1):
        second_area.append(place)

    if set(second_area).issubset(set(first_area)) or set(first_area).issubset(second_area):
        total_task_1 += 1

    for place in first_area:
        if place in second_area:
            total_task_2 += 1
            break

print(total_task_1)
print(total_task_2)
file.close()
