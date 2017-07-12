import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]

x2 = [1, 2, 3]
y2 = [8, 14, 9]

plt.plot(x, y, label='first line')
plt.plot(x2, y2, label='second line')

plt.xlabel('plot number')
plt.ylabel('important variable')
plt.title('interesting graph\ncheck it out')
plt.legend()
plt.show()
