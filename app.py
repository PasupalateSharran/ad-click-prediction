import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = [float(request.form['input1']),
                      float(request.form['input2']),
                      float(request.form['input3']),
                      float(request.form['input4']),
                      float(request.form['input5'])]
        loaded_model = pickle.load(open('model.pkl', 'rb'))
        result = loaded_model.predict([input_data])
        return render_template('result.html', prediction = result[0])







if __name__ == '__main__':
    app.run(debug=True)