import os
from flask import Flask, render_template, request
from FinalModel1 import predict_power

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('inputForm.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_thick = float(request.form['input_thick'])
    input_width = float(request.form['input_width'])
    ip_wt = float(request.form['ip_wt'])
    thickness_actual = float(request.form['thickness_actual'])
    number_of_passes = int(request.form['number_of_passes'])

    predicted_power = predict_power(input_thick, input_width, ip_wt, thickness_actual, number_of_passes)

    return render_template('output.html', 
                           predicted_power=predicted_power,
                           input_thick=input_thick,
                           input_width=input_width,
                           ip_wt=ip_wt,
                           thickness_actual=thickness_actual,
                           number_of_passes=number_of_passes)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
