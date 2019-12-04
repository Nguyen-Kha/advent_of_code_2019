day1 = open("day1_input.txt", "rt")
text_array = day1.read().splitlines()
text_array = [int(i) for i in text_array]

sum = 0
j = 0 

for j in range (len(text_array)):
    sum += int((text_array[j] / 3)) - 2

print(sum)
# 3358992