count = 0
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
        count += 1

print(count)
#1099