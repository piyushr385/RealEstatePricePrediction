#Import Libraries
import numpy as np
import pandas as pd
import joblib
 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
 
#load data
df = pd.read_csv('final_house_scrape.csv')

 
# Split data
X= df.drop('price(L)', axis=1)
y= df['price(L)']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=51)
 
# feature scaling
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)
 


model = joblib.load('random_model.pkl')
 
###### Load Model
 
def predict_house_price(BHK,Bathroom,rate_persqft,area_insqft,construction_status,Sale_type,location):
    x =np.zeros(len(X.columns)) # create zero numpy array
    # adding feature's value according to their column index
    x[0]=BHK
    x[1]=Bathroom
    x[2]=rate_persqft
    x[3]=area_insqft
 
    if "construction_status"=="Ready To Move":
        x[5]=1
     
    if "Sale_type"=="resale":
        x[7]=1
 
    if 'location_'+location in X.columns:
        loc_index = np.where(X.columns=="location_"+location)[0][0]
        x[loc_index]=1
 
    #print(loc_index)
 
    #print(x)
 
    # feature scaling
    x = sc.transform([x])[0] # give 2d np array for feature scaling and get 1d scaled np array
    #print(x)
 
    return model.predict([x])[0] # return the predicted value by train Random forest model.
