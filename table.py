import pandas as pd



def returnTable(x):
    df = pd.read_json(x)
    news_table = pd.to_html(df)
    return news_table
