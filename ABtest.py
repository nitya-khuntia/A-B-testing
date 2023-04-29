import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Control group data
control_group = np.random.binomial(n=50, p=0.2, size=75)

# Experimental group data
experimental_group = np.random.binomial(n=50, p=0.25, size=75)

# Calculate mean conversion rates for each group
control_mean = np.mean(control_group)
experimental_mean = np.mean(experimental_group)

# Calculate the two-tailed p-value using a two-sample t-test
t_stat, p_val = ttest_ind(control_group, experimental_group, equal_var=False)
p_val= '{:.6f}'.format(p_val)

# Print the mean conversion rates and p-value
print("Control group mean conversion rate:", control_mean)
print("Experimental group mean conversion rate:", experimental_mean)
print("Two-tailed p-value:", p_val)


# Barchart for conversion rates for each group 

labels = ['Control', 'Experiment']
means = [control_mean, experimental_mean]

plt.bar(labels, means, color=['gray', 'blue'])
plt.ylabel('Conversion rate')
plt.title('Loan application form redesign A/B test results')
plt.show()

