import numpy as np
from scipy.stats import norm
def recommend(avg,std,on_hand,lead):
    z=norm.ppf(0.95)
    ss=z*std*np.sqrt(lead)
    rop=avg*lead+ss
    qty=max(0,int(round(rop-on_hand)))
    return ss,rop,qty
