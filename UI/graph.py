import matplotlib.pyplot as plt
import random
xLable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data1 = [220,220,220,220,220,220,220,220,220,220]

data2 = data1

data3 = data1

for i in range(len(data1)):
    data1[i] += random.randrange(0, 10)*0.1


plt.plot(xLable, data1)
for i in range(len(data1)):
    data2[i] += random.randrange(0, 10)*0.1
plt.plot(xLable, data2)
for i in range(len(data1)):
    data3[i] += random.randrange(0, 10)*0.1
plt.plot(xLable, data3)
plt.ylabel('Voltage')
plt.show()