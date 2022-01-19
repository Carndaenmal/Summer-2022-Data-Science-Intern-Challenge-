import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/2019-challenge-shopify.csv')
print(round(df['order_amount'].mean(), 2)) # replicate the problem
print('After viewing the data I noticed outliers')
df_over_thousand = df[(df['order_amount'] > 1000)] # remove outliers after viewing data
df_less_equal_thousand = df[(df['order_amount'] <= 1000)] # set compliment
print('I think the best metric to report is to split the population and report the mean of both groups. A median might be a better estimator for future analysis.')
print('Here are the values for both groups: ')
print(round(df_over_thousand['order_amount'].mean(),2))
print(round(df_less_equal_thousand['order_amount'].mean(),2))
print('Here is a median: ')
print(df['order_amount'].median())

df['Amount per Item'] = df['order_amount']/df['total_items']
print('Normalized amount: ')
print(df['Amount per Item'].mean())


df_plot = [sum(df_over_thousand['order_amount']),sum(df_less_equal_thousand['order_amount'])]

plt.bar(['Over a Thousand', 'Less Than or Equal to a Thousand'],df_plot) # visual representation of the problem
plt.savefig('Bar Plot of Shops with more or less than a Thousand Order Value')
plt.show()




