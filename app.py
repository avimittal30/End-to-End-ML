from flask import Flask, render_template, request

import os

import numpy as np
import pandas as pd
from mlProject.pipeline.stage06_prediction import PredictionPipeline

app=Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful"


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            CustomerId =int(request.form['CustomerId'])
            CreditScore =int(request.form['CreditScore'])
            Gender =int(request.form['Gender'])
            Age =int(request.form['Age'])
            Tenure =int(request.form['Tenure'])
            Balance =float(request.form['Balance'])
            NumOfProducts =int(request.form['NumOfProducts'])
            HasCrCard =int(request.form['HasCrCard'])
            IsActiveMember=int(request.form['IsActiveMember'])
            EstimatedSalary =float(request.form['EstimatedSalary'])
            Geography_Germany =int(request.form['Geography_Germany'])
            Geography_Spain =int(request.form['Geography_Spain'])
       
         
            data = [CustomerId,CreditScore,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography_Germany,Geography_Spain]
            data = np.array(data).reshape(1, 12)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            result = "Likely to Churn" if predict == 1 else "Unlikely to Churn"
            
            return result

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')



if __name__=="__main__":
    # app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(host="0.0.0.0", port=8080)
