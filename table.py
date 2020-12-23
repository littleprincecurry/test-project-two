import pandas as pd



def returnTable():
    df = pd.read_json('https://test-project-two.herokuapp.com/news')
    news_table = df.to_html()
    return news_table
