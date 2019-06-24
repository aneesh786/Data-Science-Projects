import csv
import sys
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
##For errors like pandas.errors.ParserError: field larger than field limit (131072)####
#csv.field_size_limit(sys.maxsize)
maxInt = sys.maxsize
while True:
        try:
               csv.field_size_limit(maxInt)
               break
        except OverflowError:
                maxInt = int(maxInt/10)

df1 = pd.read_csv('C:\Aneesh\Kaggle\zomato-bangalore-restaurants\zomato.csv',engine='python')
df1.rename(columns={'approx_cost(for two people)':'cost_for_two'},inplace=True)
df1.cost_for_two.fillna('0',inplace=True)
df1.cost_for_two.fillna('0')
df1.cost_for_two = df1.cost_for_two.str.replace(',', '')
df1.cost_for_two = df1.cost_for_two.astype('int64')
df1['rate'] = [''.join(c.split()) for c in df1['rate'].astype(str)] ###Removes unnecessary spaces###
df1['rate'] = df1.rate.str.replace('/5','')
df1['rate'] = df1['rate'].str.replace('-','0')
df1['listed_in(city)'].value_counts() ###provides area wise restaurants list###
df1.groupby('listed_in(city)')['name'].count()##Not much useful###
df1.groupby('listed_in(type)')['name'].count()
df1.groupby('rate')['dish_liked'].count()
df1.groupby('rate')['name'].count()
df1.groupby(['location','listed_in(city)'])['dish_liked'].count()
df1.dish_liked.isnull().sum()
df1.rate.fillna(value=0,inplace=True)
df1.sort_values(by=['rate'],ascending=True,inplace=True)
##df1['rate'] = df1[df1['rate'].str.contains('-',na=False)]['rate'].str.replace('-','0')##Do not use this###
df1.groupby('rate')['location'].count()
df1.groupby('rate')['approx_cost(for two people)'].value_counts().tail(40)
df1.rate.max()
df1.groupby([df1.rate=='4.9'])['name'].tail()
df1.groupby([df1.rate=='4.9'])['location','name'].tail()




df1.groupby(['listed_in(city)','rate'])['name'].