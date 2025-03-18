# Bell-shaped curve
# ✅ Symmetric around the mean
# ✅ 68-95-99.7 Rule:

# 68% of values lie within 1 standard deviation
# 95% within 2 standard deviations
# 99.7% within 3 standard deviations

# the mean tells the center of the curve and the standard deviation explains the width og the curve eg-> if SD-> 1 then every unit from mean to the left and the right will inc and dec by 1 value 
#  eg -> mean = 10 and sd = 2 then left of mean next unit will be 8 and right of mean next unit will be 12 then SD helps in determininf the width of the plot 

#  normal distribution has a (n) shape graph 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
data = np.random.normal(loc=50, scale=10, size=1000)  # Mean=50, Std=10

# Plot
sns.histplot(data, kde=True, bins=30)
plt.title("Normal Distribution")
plt.show()
