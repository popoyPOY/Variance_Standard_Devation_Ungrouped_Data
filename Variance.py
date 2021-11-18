from math import sqrt

Data = [1.6, 1.2, 1.9, 1.5, 1.5, 1.5, 1.0, 1.3, 1.0]

mean = sum(Data) / len(Data)

result = [element - mean for element in Data]

sqrd = []

count = 0

for x in result:
    d = result[count] * x
    count +=1
    sqrd.append(d)

total_sqrd = sum(sqrd)

n = len(Data) - 1

Variance = round(total_sqrd / n, 2)

Standard_Devation = round(sqrt(Variance), 2)

print(Variance)

    