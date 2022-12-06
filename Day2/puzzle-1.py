with open("Day2/data.txt") as f:
    data = f.read().splitlines()

points_xyz = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

score = 0


for value in range(len(data)):
    data[value] = data[value].split()
    score = points_xyz[data[value][1]]

    if data[value][0] == 'A' and data[value][1] == "Y":
        score+=6
    elif data[value][0] == 'A' and data[value][1] == "Z":
        score+=0
    elif data[value][0] == 'B' and data[value][1] == "Z":
        score+=6
    elif data[value][0] == 'B' and data[value][1] == "X":
        score+=0
    elif data[value][0] == 'C' and data[value][1] == "X":
        score+=6
    elif data[value][0] == 'C' and data[value][1] == "Y":
        score+=0
    else:
        score+=3

    data[value].append(score)

total = 0

for i in data:
    total+=i[2]
print(total)