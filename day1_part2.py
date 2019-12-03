day1 = open("day1_input.txt", "rt")
text_array = day1.read().splitlines()
text_array = [int(i) for i in text_array]

def recursive_call(n):
    if n <= 0:
        a = int(0)
        return a
    else:
        return n + recursive_call(int((n/3))-2)

sum = 0
j = 0

for j in range (len(text_array)):
    sum += (recursive_call(int(text_array[j] / 3) -2))

print(sum)
#5035632