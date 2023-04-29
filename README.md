# A/B testing

# Objective: Evaluate the impact of a redesigned loan application form on loan conversion rates for XYZ.

# Hypotheses:

Null Hypothesis (H0): There is no significant difference in loan conversion rates between the control group (current loan application form) and the experimental group (redesigned loan application form).
Alternative Hypothesis (H1): There is a significant difference in loan conversion rates between the control group and the experimental group.

# control group and experimental group:

*Control group: users who are shown the current loan application form
*Experimental group: users who are shown the redesigned loan application form

# Determine the sample size needed for statistical significance:

*Desired level of significance: 0.05 (this means that we are willing to accept a 5% chance of a type I error, which is rejecting the null hypothesis when it's actually true)
*Desired power: 0.8 (this means that we want to detect a true difference in conversion rates with 80% probability)
\*Effect size: We can estimate the effect size based on historical conversion rates and how much of an improvement we hope to achieve with the redesigned form. For example, if historical conversion rates were 10% and we hope to achieve a 15% conversion rate with the redesigned form, the effect size would be 0.5.
In this w e are taking the effect size 0.2.

We can use a sample size calculator to obtain the sample size. With the above inputs sample size is coming out to be: 150

# Performing A/B testing

Refer to ABtest.py
We generated some random data to simulate the number of loan applications submitted by each group. We used a binomial distribution to model the number of successes (i.e., loan applications) out of 50 trials for each user. We assumed that the control group had a conversion rate of 20% and the experimental group had a conversion rate of 25%.

A two-sample t-test is then performed using the ttest_ind() function from the scipy.stats module to determine if there is a statistically significant difference between the mean conversion rates of the two groups. The t-test calculates a t-statistic and a p-value. The t-statistic measures the difference between the means of the two groups relative to the variance within each group. The p-value measures the probability of obtaining a t-statistic as extreme as the observed value, assuming the null hypothesis is true (i.e., there is no difference between the groups).

If the p-value is less than the level of significance (typically 0.05), then we reject the null hypothesis and conclude that there is a statistically significant difference between the two groups. If the p-value is greater than the level of significance, then we fail to reject the null hypothesis and conclude that there is not enough evidence to suggest a difference between the groups.
In our case the p-value is 0.000051 which is less than the level of significance i.e 0.05.

code will produce a bar chart that shows the conversion rate for the control group and the experiment group. The control group is represented by the gray bar, and the experiment group is represented by the blue bar. 


# Outcome
Based on the A/B test we performed, we found that the loan conversion rate for the experimental group (with the redesigned loan application form) was higher than the loan conversion rate for the control group (with the original loan application form). The p-value was less than the desired level of significance (alpha), indicating that the difference in conversion rates between the two groups is statistically significant.

Furthermore, the power of the test was satisfactory, indicating that we had a high probability of correctly rejecting the null hypothesis when it was false.In the A/B test example we conducted , we set the desired power to be 0.8. This means that we want to have an 80% chance of detecting a true difference if it exists.

The power of a test is the probability that the test correctly rejects a false null hypothesis (a type II error). 

Therefore, we can conclude that the redesigned loan application form has a positive impact on loan conversion rates for XYZ, and the company should implement it on a larger scale.