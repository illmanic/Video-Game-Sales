import pandas as pd
import numpy as nu
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import stats
sns.set(style="white", color_codes=True)

df = pd.read_csv('video game sales 2016-12-22.csv', parse_dates=['Year_of_Release'])

df.shape
df.info
df.dtypes

df['User_Score'] = pd.to_numeric(df['User_Score'], downcast = 'integer', errors = 'coerce')

pc = df[df['Platform'] == 'PC']

sns.jointplot(x = 'Critic_Score', y = 'User_Score', data = pc, kind = 'reg')

df['Year_of_Release'].value_counts().plot(c = ['Platform'])

df.groupby('Genre')[['NA_Sales', 'Global_Sales']].sum().sort_values('Global_Sales', ascending = False).plot(kind = 'bar')

