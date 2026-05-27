import numpy as np
import matplotlib.pyplot as plt

numbers = []

np.random.seed(0) # so results are reproducible

for i in range (300): 
 
 n = np.random.randint(1,800001)
 estimate = (1 + 1/n)**n # continuous compounding that converges to e as n gets larger
 numbers.append(estimate)

numbers = np.array(numbers)

print(f"Monte Carlo estimate of e: {np.mean(numbers)}")

plt.hist(numbers, bins=30, edgecolor="black") # histogram formatting
plt.title("Monte Carlo Estimates of e")
plt.xlabel("Estimate") # label of x axis
plt.ylabel("Frequency") # label of y axis
plt.show()

