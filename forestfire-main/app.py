import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import warnings



application = Flask(__name__)
app=application

## import ridge regresor model and standard scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))
warnings.filterwarnings("ignore", category=UserWarning)
## Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('home.html')

@app.route('/predict_datapoint',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)

        return render_template('home.html',result=result[0])

    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run()