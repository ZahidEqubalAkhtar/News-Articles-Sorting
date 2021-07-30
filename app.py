import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import logging
import string
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)


def punctuation_removal(x):
    return " ".join([a for a in (''.join([a for a in x if a not in string.punctuation])).lower().split()])
app = Flask(__name__)

model=pickle.load(open("final_model.pkl","rb"))

@app.route('/')
def home():
    logging.info("Model pickle file loaded successfully")

    return render_template('3.html')
    logging.info("rendering html template has been done successfully")


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    text= request.form["textarea1"]

    final_text = punctuation_removal(text)



    prediction = model.predict([final_text])



    #int_features = [i for i in request.form.values()]
    #int_features_punc=punctuation_removal(int_features)

    #print(int_features)
    #final_features = [np.array(int_features)]
    logging.info("Model Prediction")
    #prediction = model.predict([int_features_punc])





    return render_template('3.html',textinput=text, prediction_text='This News Article will be  classified as {}'.format(prediction[0]))





if __name__ == "__main__":

    #app.run(debug=True)
    app.run(host='0.0.0.0',port=8080)

    logging.info("App is Running Perfectly")