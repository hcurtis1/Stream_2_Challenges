import matplotlib.pyplot as plt

plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label="Example one", color='#191970')

plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label="Example two", color='#e1e1e1')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('Epic Graph\nAnother Line!...')

plt.show()
