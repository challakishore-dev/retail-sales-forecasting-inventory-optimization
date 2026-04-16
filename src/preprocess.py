import pandas as pd
def load_data(path):
    df=pd.read_csv(path,parse_dates=['date'])
    return df.sort_values(['store_id','item_id','date'])
