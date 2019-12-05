day2 = open("day02_input.txt", "rt")
text_array = day2.read().split(",")
text_array = [int(i) for i in text_array]
day2.close()

text_array[1] = 1
text_array[2] = 2
a = 0
gone_through = False
while(text_array[a] != 99):
    if((text_array[a] == 1) and not(gone_through)):
        first_number = text_array[a+1]
        second_number = text_array[a+2]
        third_number = text_array[a+3]
        text_array[third_number] = text_array[first_number] + text_array[second_number]
        gone_through = True

    elif((text_array[a] == 2) and not(gone_through)):   
        first_number = text_array[a+1]
        second_number = text_array[a+2]
        third_number = text_array[a+3]
        text_array[third_number] = text_array[first_number] * text_array[second_number]
        gone_through = True
    
    a += 4
    gone_through = False

print(text_array[0])
#5098658