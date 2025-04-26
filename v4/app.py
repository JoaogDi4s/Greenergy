from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/OqueSao')
def OqueSao():
    return render_template('OqueSao.html')

if __name__ == '__main__':
    app.run(debug=True)
