import csv
with open("height-weight.csv") as CSV:
    rd = csv.reader(CSV)
    data = list(rd)
data.pop(0)
weight = []
for i in range(0,len(data)):
    num = data[i][2]
    weight.append(float(num))

sum = 0
for a in weight:
    sum = sum+a

mean = sum/len(weight)
print(mean)