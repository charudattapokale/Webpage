import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import time

app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    '''
    For rendering results on HTML GUI
    '''
    text_features = [x for x in request.form.values()]
    print(f"post:{text_features}")
    final_features = text_features[0]

    #prediction = model.predict(final_features)

    #output = round(prediction[0], 2)

    output = final_features
    time.sleep(5)
    return jsonify(result=output)
    
    
    #return render_template('index.html', prediction_text='Predicted Tag {}'.format(final_features))


if __name__ == "__main__":
    app.run(debug=True)