import csv
with open("height-weight.csv") as CSV:
    rd = csv.reader(CSV)
    data = list(rd)
data.pop(0)
weight = []
for i in range(0,len(data)):
    num = data[i][2]
    weight.append(float(num))

weight.sort()
n = len(weight)
if n % 2 == 0:
    median1 = float(weight[n//2])
    median2 = float(weight[n//2+1])
    median = (median1+median2)/2
else:
    median = float(weight[n//2])
print(median)
