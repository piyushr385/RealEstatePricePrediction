#Import Libraries
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import joblib
import model
 
app = Flask(__name__)


# render html page
@app.route('/')
def home():
    return render_template('index.html')

# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict(): 
    #take data from form and store in each feature    
    input_features = [x for x in request.form.values()]
    BHK = input_features[0]
    Bathroom = input_features[1]
    rate_persqft = input_features[2]
    area_insqft = input_features[3]
    construction_status = input_features[4]
    Sale_type = input_features[5]
    location = input_features[6]
     
    # predict the price of house by calling model.py
    predicted_price = model.predict_house_price(BHK,Bathroom,rate_persqft,area_insqft,construction_status,Sale_type,location)       
    
 
    # render the html page and show the output
    return render_template('index.html', prediction_text='Predicted Price of House is {} (Lakhs)'.format(predicted_price))
 
 #if __name__ == "__main__":
 #   app.run(host="0.0.0.0", port="8080")
     
if __name__ == "__main__":
    app.run(debug = True)