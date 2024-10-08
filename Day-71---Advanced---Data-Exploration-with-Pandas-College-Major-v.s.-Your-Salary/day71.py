# -*- coding: utf-8 -*-
"""day71.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12NNFc1t_ljrMhlxN3aHAEKNOCEaIhHTu
"""

import pandas as pd
df = pd.read_csv('salaries-by-college-major.csv')

df.head()

df.shape

df.columns

df.isna()

df.tail()

clean_df = df.dropna()
clean_df.tail()

clean_df['Starting Median Salary']

clean_df['Starting Median Salary'].max()

clean_df['Starting Median Salary'].idxmax()

clean_df['Undergraduate Major'].loc[43]

clean_df.loc[43]

max_index = clean_df['Mid-Career Median Salary'].idxmax()
clean_df['Undergraduate Major'].loc[max_index]

clean_df['Mid-Career 10th Percentile Salary'].loc[max_index]

min_index = clean_df['Starting Median Salary'].idxmin()
clean_df['Undergraduate Major'].loc[min_index]

min_index_mid_salary = clean_df['Mid-Career Median Salary'].idxmin()
clean_df['Undergraduate Major'][min_index_mid_salary]

clean_df['Mid-Career 90th Percentile Salary'].loc[min_index_mid_salary]

clean_df.loc[min_index_mid_salary]

clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

spread_col = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
  clean_df.insert(1,'Spread',spread_col)
  clean_df.head()

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major','Spread']].head()

highest_values = clean_df.sort_values(by=['Mid-Career 90th Percentile Salary'], ascending=False)

highest_values[['Undergraduate Major','Mid-Career 90th Percentile Salary']].head()

highest_spread = clean_df.sort_values(by=["Spread"],ascending=False)
highest_spread[['Undergraduate Major','Spread']].head()

highest_spread = clean_df.sort_values(by=['Mid-Career Median Salary'],ascending=False)
highest_spread[['Undergraduate Major','Mid-Career Median Salary']].head()

clean_df.groupby('Group').count()

clean_df.groupby('Group').mean(numeric_only=True)

pd.options.display.float_format = '{:,.2f}'.format
clean_df.groupby('Group').mean(numeric_only=True)

