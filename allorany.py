x = input(" ").split()
count = 0
cond1 = 'F'
for i in range(len(x)):
    x[i] = int(x[i])
    if x[i] <= 0:
        cond1 = 'FN'
        break
    elif x[i] >= 0:
        if x[i] < 10:
            cond1 = 'T'
        count = count + 1
    else:
        continue

if count == len(x) and cond1 == 'T':
    print("True")
elif cond1 == 'FN':
    print("False")
else:
    print("False")
