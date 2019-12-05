count = 0

valid = []
for i in range(245182, 790572):
    b = [int(d) for d in str(i)]
    check_double = False
    check_increase = True
    for c in range(0, 5):
        if (b[c] == b[c+1]):
            check_double = True
        if (b[c] > b[c+1]):
            check_increase = False

    if(check_double and check_increase):
        valid.append(i)

new_valid = []
for j in range(0, 1099):
    count1 = 0
    count2 = 0
    count3 = 0
    pair1_pass = False
    pair2_pass = False
    e = [int(f) for f in str(valid[j])]
    for g in range(0, 5):
        if ((e[g] == e[g+1]) and (pair1_pass == False) and (pair2_pass == False)):
            count1 += 1
        if ((e[g] != e[g+1]) and (count1 != 0)):
            pair1_pass = True
        if ((e[g] == e[g+1]) and (pair1_pass == True)) :
            count2 += 1
        if ((e[g] != e[g+1]) and (count2 != 0)):
            pair2_pass = True
        if ((e[g] == e[g+1]) and (pair2_pass == True)):
            count3 += 1
    count1 += 1
    count2 += 1
    count3 += 1

    if((count1 == 2) or (count2 == 2) or (count3 == 2)) :
        new_valid.append(valid[j])

print(len(new_valid))
#710