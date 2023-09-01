from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# Median Developer Salaries by Age
dev_x = [25,26,27,28,29,30,31,32,33,34,35]

dev_y =[38496,42000,46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(dev_x, dev_y, 'k--', label= 'All Devs')
plt.plot(dev_x, dev_y, color = 'k', label= 'All Devs')
# Median Python Developer Salaries by Age
py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(py_dev_x,py_dev_y, 'b-.', label= 'Python')

plt.xlabel('Age')
plt.ylabel('Salary (USD)')


plt.title('Median Salary (USD) by Age')

# plt.legend(['All Devs', 'Python'])

plt.tight_layout()

plt.show()
