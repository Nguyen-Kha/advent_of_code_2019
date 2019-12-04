day3 = open("day03_input.txt", "rt")
path1 = day3.readline().split(",")
path2 = day3.readline().split(",")
day3.close()

x1 = 0
y1 = 0
x2 = 0
y2 = 0
i = 0
a = 0
split_at = 1
coordinates1 = []
coordinates2 = []
steps1 = 0
steps2 = 0

for i in range(len(path1)):
    direction1 = path1[i][:split_at]
    unit1 = int(path1[i][split_at:])

    if (direction1 == 'U'):
        for j in range(unit1):
            y1 += 1
            coordinate = str(x1) + " " + str(y1)
            coordinates1.append(coordinate)
            steps1 += 1
    
    elif (direction1 == 'D'):
        for j in range(unit1):
            y1 -= 1
            coordinate = str(x1) + " " + str(y1)
            coordinates1.append(coordinate)
            steps1 += 1

    elif (direction1 == 'L'):
        for j in range(unit1):
            x1 -= 1
            coordinate = str(x1) + " " + str(y1)
            coordinates1.append(coordinate)
            steps1 += 1

    elif (direction1 == 'R'):
        for j in range(unit1):
            x1 += 1
            coordinate = str(x1) + " " + str(y1)
            coordinates1.append(coordinate)
            steps1 += 1

for a in range(len(path2)):
    direction2 = path2[a][:split_at]
    unit2 = int(path2[a][split_at:])

    if (direction2 == 'U'):
        for j in range(unit2):
            y2 += 1
            coordinate = str(x2) + " " + str(y2)
            coordinates2.append(coordinate)
            steps2 += 1
    
    elif (direction2 == 'D'):
        for j in range(unit2):
            y2 -= 1
            coordinate = str(x2) + " " + str(y2)
            coordinates2.append(coordinate)
            steps2 += 1

    elif (direction2 == 'L'):
        for j in range(unit2):
            x2 -= 1
            coordinate = str(x2) + " " + str(y2)
            coordinates2.append(coordinate)
            steps2 += 1

    elif (direction2 == 'R'):
        for j in range(unit2):
            x2 += 1
            coordinate = str(x2) + " " + str(y2)
            coordinates2.append(coordinate)
            steps2 += 1

intersections = list(set(coordinates1).intersection(set(coordinates2)))

print(intersections)

smallest = -1
for k in range(len(intersections)):
    sum = 0
    total_steps1 = int(coordinates1.index(intersections[k])) + 1
    total_steps2 = int(coordinates2.index(intersections[k])) + 1
    sum = total_steps1 + total_steps2
    if(smallest == -1):
        smallest = sum
    elif (smallest > sum):
        smallest = sum

print(smallest)
#14746