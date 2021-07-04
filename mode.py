import csv
with open("height-weight.csv") as CSV:
    rd = csv.reader(CSV)
    data = list(rd)
data.pop(0)
weight = []
for i in range(0,len(data)):
    num = data[i][1]
    weight.append(float(num))
    
import statistics
mode = statistics.mode(weight)
print(mode)
mean = statistics.mean(weight)
print(mean)
median = statistics.median(weight)
print(median)