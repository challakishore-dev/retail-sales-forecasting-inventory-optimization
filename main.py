from src.preprocess import load_data
from src.features import make_features
from src.inventory import recommend
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd, joblib, os

os.makedirs("outputs", exist_ok=True)
os.makedirs("models", exist_ok=True)

df=load_data('data/retail_sales.csv')
df=make_features(df)
X=df[['store_id','item_id','promo_flag','month','dow','lag_1','lag_7','roll7']]
y=df['qty_sold']
split=int(len(df)*0.8)
Xtr,Xte=X.iloc[:split],X.iloc[split:]
ytr,yte=y.iloc[:split],y.iloc[split:]
model=RandomForestRegressor(n_estimators=120,random_state=42)
model.fit(Xtr,ytr)
pred=model.predict(Xte)
print('MAE:', round(mean_absolute_error(yte,pred),2))
os.makedirs('models',exist_ok=True)
joblib.dump(model,'models/model.pkl')
out=pd.DataFrame({'actual':yte.values,'predicted':pred})
out.to_csv('outputs/predictions.csv',index=False)
avg=pred[:7].mean(); std=(yte.values[:50]-pred[:50]).std()
print('Inventory:', recommend(avg,std,60,7))
print('Done Successfully')
