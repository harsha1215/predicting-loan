from flask import Flask, render_template, request
import numpy as np 
import pandas as pd
import pickle
import os

app = Flask(__name__)
model=pickle.load(open(r'rdf.pkl', 'rb'))
#scale=pickle.load(open(r'scalei.pkl', 'rb'))

@app.route('/') # rendering the html template 
def home():
    return render_template("home.html")

@app.route('/submit',methods=["POST", "GET"])# route to show the predictions in a web UI 
def submit():
    #reading the inputs given by the user 
    input_feature=[int(x) for x in request.form.values()]
    #input_feature=[x for x in request.form.values()] 
    #input_feature = np. transpose (input_feature)
    #input_feature=['Male', 'Yes', '2', 'Graduate', 'Yes', '5465', '600', '500', '240', '1', 'Urban']

    input_feature=[np.array(input_feature)]
    print(input_feature)
    names = [ 'Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome',
    'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History','Property Area']
    data = pd.DataFrame(input_feature)
    print(data)
    
    # print(input_feature)

    
    #data scaled scale.fit_transform(data)
    #data = pandas. DataFrame (, columns=names)

    # predictions using the loaded model file
    prediction=model.predict(data)
    print(prediction)
    prediction=int(prediction)
    print(type(prediction))
    if(prediction == 0):
        return render_template("output.html", result = "Loan will Not be Approved!")
    else:
        return render_template("output.html",result ="Loan will be Approved")
    # showing the prediction results in a UI
    

    # return render_template("output.html", result = "Registered Successfully !!! ")



if __name__=="__main__":
    # app.run(host= '0.0.0.0', port=8000, debug=True)
    port=int(os.environ.get("PORT " ,5000))
    app.run(debug=True)