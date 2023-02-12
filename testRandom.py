# Fangzhou Yu
# Test Randomness
# 23W, CS62

# open file to read
file = open("list.txt", "r")
all = []
nl = []
for line in file:
    nl = []
    for char in line:
        if char == '1' or char == '0':
            nl.append(char)
    all.append(nl)
file.close()

# Find mine
myfile = open("../HW0/Q6.txt", "r")
mySeq = []
for line in myfile:
    for char in line:
        if char == '1' or char == '0':
            mySeq.append(char)
myfile.close()

for i in range(50):
    if all[i] == mySeq[:2760]:
        print(i)

## Set up dictionary to record result
dict = {}
for i in range(50):
    dict[i] = 0

# Test randomness
## All test comes from "Security Requirements for Cryptographic Modules"
## Federal Information Processing Standard (FIPS) 140-1, 1.1.1994
## test 1 the monobit test
for i in range(50):
    UPPER = 10346/20000
    LOWER = 9654 / 200000
    length = len(all[i])
    ones = all[i].count('1')
    ratio = ones/length
    if ratio < UPPER and ratio > LOWER:
        dict[i] += 1

## test 2 the poker test
### generated from 2000 samples, see getDistribution for how they are generated
### we can fairly assume they all follow normal distribution since the sample size is
### pretty big
mean = {10: 175.3190000000002, 5: 174.3650000000003, 11: 173.86000000000038, 7: 174.4110000000004,
        15: 174.35300000000007, 14: 174.41200000000043, 12: 174.46400000000025, 8: 174.9870000000003,
        0: 175.23399999999984, 1: 174.9700000000004, 2: 174.06000000000054, 4: 174.9990000000001,
        9: 174.47800000000035, 6: 174.86499999999992, 13: 174.82000000000014, 3: 175.40300000000022}
var = {10: 175.2352389999996, 5: 176.7857749999998, 11: 150.18640000000073, 7: 91.01007899999999,
       15: 415.5023910000005, 14: 90.59625599999995, 12: 97.3827039999999, 8: 100.38883099999978,
       0: 401.1352440000007, 1: 100.52709999999988, 2: 144.10839999999985, 4: 143.30299900000023,
       9: 145.54951599999995, 6: 142.7287749999998, 13: 143.81759999999971, 3: 101.91259099999992}

## test
for i in range(50):
    scale = len(all[i])/2800
    test2Dict = {}

    ## get a 95% confidence interval
    std = {}
    for item in var.items():
        std[item[0]] = ((item[1])**0.5)*scale
    ci_lower = {}
    ci_upper = {}
    for j in range(16):
        ci_lower[j] = mean.get(j)*scale - 1.96 * std.get(j)
        ci_upper[j] = mean.get(j)*scale + 1.96 * std.get(j) / (1000 ** 0.5)
    ## all possible 4-bit values
    for p in range(16):
        test2Dict[p] = 0
    ## count
    pos = 0
    op = 0
    while pos+3 < len(all[i]):
        op += 1
        num = int(all[i][pos])*(2**3) + int(all[i][pos+1])*(2**2) + int(all[i][pos+2])*(2**1) + int(all[i][pos+3])*(2**0)
        test2Dict[num] += 1
        pos += 4
    ## fit in to confidence interval
    fit = 0
    for p in range(16):
        if test2Dict[p] < ci_upper[p]*scale and test2Dict[p] > ci_lower[p]*scale:
            fit += 1
    if fit > 0:
        dict[i] += 1



## test 3 + 4 the runs test and the long run test
def countRuns(l, d0, d1):
    curr = l[0]
    count = 1
    for i in range(1, len(l)):
        if l[i] == curr:
            count += 1
        else:
            if curr == '0':
                if count > 6:
                    d0[6] += 1
                else:
                    d0[count] += 1
            if curr == '1':
                if count > 6:
                    d1[6] += 1
                elif count > 10:
                    return False
                    break
                else:
                    d1[count] += 1
            curr = l[i]
            count = 1
    return True

def examineDict(d0, d1, len):
    ratio = len/20000
    res = 0
    ## single 1s and 0s
    if (d0[1] > 2267*ratio) and (d1[1] > 2267*ratio) and (d0[1] < 2733*ratio) and (d1[1] < 2733*ratio):
        res += 1
    ## double
    if (d0[2] > 1079*ratio) and (d1[2] > 1079*ratio) and (d0[2] < 1421*ratio) and (d1[2] < 1421*ratio):
        res += 1
    ## triple
    if (d0[3] > 502*ratio) and (d1[3] > 502*ratio) and (d0[3] < 748*ratio) and (d1[3] < 748*ratio):
        res += 1
    ## four
    if (d0[4] > 223*ratio) and (d1[4] > 223*ratio) and (d0[4] < 402*ratio) and (d1[4] < 402*ratio):
        res += 1
    ## five
    if (d0[5] > 90*ratio) and (d1[5] > 90*ratio) and (d0[5] < 223*ratio) and (d1[5] < 223*ratio):
        res += 1
    ## geq6
    if (d0[6] > 90*ratio) and (d1[6] > 90*ratio) and (d0[6] < 223*ratio) and (d1[6] < 223*ratio):
        res += 1
    return res


for i in range(50):
    length = len(all[i])
    test3Dict0 = {}
    test3Dict1 = {}
    for j in range(1,7):
        test3Dict0[j] = 0
        test3Dict1[j] = 0
    if not countRuns(all[i], test3Dict0, test3Dict1):
        print("sequence ", i, " fails the long run test")
    else:
        score = examineDict(test3Dict0, test3Dict1, length)
    ## lower the standard since we have a smaller sample size
        if score >= 3:
            dict[i] += 1



n = 0
passList = []
for item in dict.items():
    if item[1] == 2:
        print(item[0], len(all[item[0]]))
        n += 1
        passList.append(item[0])
    elif item[1] == 3:
        n += 1
        print("All Good", item[0], len(all[item[0]]))
        passList.append(item[0])

print(n,"Sequencies pass")
passList.remove(32)

## Write the result to new file
result = open("Q4result.txt", "w")
for i in range(50):
    if i in passList:
        s = "S" + str(i) + " MACHINE"
        result.write(s)
        result.write("\n")
    else:
        s = "S"+ str(i) + " HUMAN"
        result.write(s)
        result.write("\n")
result.close()




