import pandas as pd
import os

files = [x for x in os.listdir("labeled-tweets")]
pd.set_option("display.max_rows", 10, "display.max_columns", None)
dfs = pd.concat([pd.read_csv("labeled-tweets/" + f) for f in files])
dfs = dfs.drop(columns=[
    'Unnamed: 0',
    'Unnamed: 5',
    'Unnamed: 6',
    'Unnamed: 7',
    'Unnamed: 8',
    'Unnamed: 9',
    'Unnamed: 10',
    'Unnamed: 11',
    'Unnamed: 12',
    'Unnamed: 13',
    'Unnamed: 14',
    'Unnamed: 15',
    'Unnamed: 16'])
print(dfs.head())
print(len(dfs))
dfs.to_csv('all_merged_tweets.csv')

