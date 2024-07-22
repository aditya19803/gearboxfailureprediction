from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict_placement():
    master_load = float(request.form.get('Master Motor Load'))
    slave_load = float(request.form.get('Slave Motor Load'))

    #prediction

    result = model.predict(np.array([master_load,slave_load]).reshape(1,2))

    if result[0] == 1:
        result = 'Warning! Breakdown may happen'
    
    elif result[0] == 0:
        result = 'Gearbox is running safe'

    return render_template('index.html', result = result)

if __name__ == '__main__':
    app.run(debug = True)