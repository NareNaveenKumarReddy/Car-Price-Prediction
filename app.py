from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('CarPrice_Capstone_Project_2.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    CompanyName_buick=0
    CompanyName_porsche=0
    CompanyName_jaguar=0
    CompanyName_bmw=0
    CompanyName_toyota=0
    CompanyName_saab=0
    carbody_wagon=0
    drivewheel_rwd=0
    cylindernumber_four=0
    if request.method == 'POST':
        carwidth = float(request.form['carwidth'])
        CompanyName_audi=request.form['CompanyName_audi']
        if(CompanyName_audi =='audi'):
                CompanyName_audi=1
                CompanyName_buick=0
                CompanyName_porsche=0
                CompanyName_jaguar=0
                CompanyName_bmw=0
                CompanyName_toyota=0
                CompanyName_saab=0
        elif (CompanyName_buick=='buick'):
            CompanyName_audi=0
            CompanyName_buick=1
            CompanyName_porsche=0
            CompanyName_jaguar=0
            CompanyName_bmw=0
            CompanyName_toyota=0
            CompanyName_saab=0
        elif (CompanyName_porsche=='porsche'):
            CompanyName_audi=0
            CompanyName_buick=0
            CompanyName_porsche=1
            CompanyName_jaguar=0
            CompanyName_bmw=0
            CompanyName_toyota=0
            CompanyName_saab=0
        elif (CompanyName_jaguar=='jaguar'):
            CompanyName_audi=0
            CompanyName_buick=0
            CompanyName_porsche=0
            CompanyName_jaguar=1
            CompanyName_bmw=0
            CompanyName_toyota=0
            CompanyName_saab=0
        elif (CompanyName_bmw=='bmw'):
            CompanyName_audi=0
            CompanyName_buick=0
            CompanyName_porsche=0
            CompanyName_jaguar=0
            CompanyName_bmw=1
            CompanyName_toyota=0
            CompanyName_saab=0
        elif (CompanyName_toyota=='toyota'):
            CompanyName_audi=0
            CompanyName_buick=0
            CompanyName_porsche=0
            CompanyName_jaguar=0
            CompanyName_bmw=0
            CompanyName_toyota=1
            CompanyName_saab=0
        else:
            CompanyName_audi=0
            CompanyName_buick=0
            CompanyName_porsche=0
            CompanyName_jaguar=0
            CompanyName_bmw=0
            CompanyName_toyota=0
            CompanyName_saab=1   
        
        aspiration_turbo=request.form['aspiration_turbo']
        if(aspiration_turbo=='turbo'):
            aspiration_turbo=1
        else:
            aspiration_turbo=0
        carbody_hardtop=request.form['carbody_hardtop']
        if(carbody_hardtop=='hardtop'):
            carbody_hardtop=1
            carbody_wagon=0
        else:
            carbody_hardtop=0
            carbody_wagon=1
        drivewheel_fwd=request.form['drivewheel_fwd']
        if(drivewheel_fwd=='Front Wheel Drive'):
            drivewheel_fwd=1
            drivewheel_rwd=0
           
        else:
            drivewheel_fwd=0
            drivewheel_rwd=1
            
        cylindernumber_five=request.form['cylindernumber_five']
        if(cylindernumber_five=='5'):
            cylindernumber_five=1
            cylindernumber_four=0
        else:
            cylindernumber_five=0
            cylindernumber_four=1
        prediction=model.predict([[cylindernumber_four,cylindernumber_five,drivewheel_fwd,drivewheel_rwd,carwidth,carbody_hardtop,carbody_wagon,aspiration_turbo,CompanyName_audi,CompanyName_buick,CompanyName_jaguar,CompanyName_bmw,CompanyName_toyota,CompanyName_saab,CompanyName_porsche]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)