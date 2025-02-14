from flask import Flask, request, render_template
import joblib

app = Flask(__name__, template_folder='templates')
vectorizer, model = joblib.load('password_strength_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        password_vec = vectorizer.transform([password])
        prediction = model.predict(password_vec)[0]
        return render_template('index.html', password=password, strength=prediction)
    return render_template('index.html', password='', strength='')

if __name__ == '__main__':
    app.run(debug=True, port=5000)