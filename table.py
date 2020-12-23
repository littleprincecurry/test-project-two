import pandas as pd



def returnTable():
    df = pd.read_json('/news')
    news_table = pd.to_html(df)
    return news_table
