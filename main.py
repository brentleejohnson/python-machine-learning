import matplotlib.pyplot as plt
import numpy as np

# Challenge 1
numbers_list = np.arange(20)
mean = np.mean(numbers_list)
stdoflist = np.std(numbers_list)
variance = np.var(numbers_list)

print(numbers_list)
print(mean)
print(stdoflist)
print(variance)

# Challenge 2
nums = [0.5, 0.7, 1., 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]

output = np.histogram(nums, bins)
print("nums: " + str(nums))
print("bins: " + str(bins))
print(output)

plt.hist(nums, bins)
plt.xlabel("Nums")
plt.ylabel("Bins")
plt.title("Histogram of nums against bins")
plt.show()
