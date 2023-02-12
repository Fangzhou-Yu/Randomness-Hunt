# Fangzhou Yu
# Approximate distribution of 01 sequencies
file = open("binary_data.txt", "r")
## make each group 2800
## file has SIZE 2800000
SIZE = 2800000
line = file.readline()
file.close()
data = []
i = 0
while i < SIZE:
    segment = line[i:i+2799]
    d = {}
    for j in range(0, len(segment)):
        if j + 4 == len(segment):
            break
        comb = segment[j:j+4]
        if comb in d.keys():
            d[segment[j:j+4]] += 1
        else:
            d[segment[j:j + 4]] = 1
    data.append(d)
    i += 2800

## Calculate mean and variance for each sample
## with CLT, fairly assume they follow a normal distribution
mean= {}
var = {}

for sample in data:
    for item in sample.items():
        ## convert this 4 bit value to int format
        n = int(item[0][0]) * (2 ** 3) + int(item[0][1]) * (2 ** 2) + int(item[0][2]) * (2 ** 1) + int(item[0][3]) * (
                2 ** 0)
        if n in mean:
            mean[n] += item[1] / 1000
        else:
            mean[n] = item[1]/ 1000
print(mean)

for sample in data:
    for item in sample.items():
        n = int(item[0][0]) * (2 ** 3) + int(item[0][1]) * (2 ** 2) + int(item[0][2]) * (2 ** 1) + int(item[0][3]) * (
                2 ** 0)
        if n in var.keys():
            var[n] += (item[1] - mean[n])**2 / 1000
        else:
            var[n] = (item[1] - mean[n])**2 / 1000
print(var)
