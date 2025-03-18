import numpy as np

data = np.array([3, 5, 7, 9])

# Compute Mean
mean = np.mean(data)

# Compute Variance
variance = np.var(data)

# Compute Standard Deviation
std_dev = np.std(data)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)

#  mean is average of all 
#  Variance -> summation((value-mean)^2)/total values
# standard deviation -> underoot(variance)

