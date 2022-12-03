with open('Day1/data.txt') as f:
    data = f.readlines()

data_split = [[]]
for value in data:
    if value != '\n':
        data_split[-1].append(int(value[:-1]))
    else:
        data_split.append([])

print(sum(sorted([sum(value) for value in data_split])[-3:]))
