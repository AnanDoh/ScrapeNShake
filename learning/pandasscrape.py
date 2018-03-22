import bs4 as bs
import urllib.request
import pandas as pd

dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0) #pandas dataframe/header=0 makes first row header
for df in dfs:
    print(df)
