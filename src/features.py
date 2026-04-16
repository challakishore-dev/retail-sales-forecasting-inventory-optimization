def make_features(df):
    df=df.copy()
    df['month']=df['date'].dt.month
    df['dow']=df['date'].dt.dayofweek
    df['lag_1']=df.groupby(['store_id','item_id'])['qty_sold'].shift(1)
    df['lag_7']=df.groupby(['store_id','item_id'])['qty_sold'].shift(7)
    df['roll7']=df.groupby(['store_id','item_id'])['qty_sold'].transform(lambda x:x.shift(1).rolling(7).mean())
    return df.dropna()
