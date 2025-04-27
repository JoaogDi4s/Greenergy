from flask import Flask, render_template
import graficos
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/OqueSao')
def OqueSao():
    graficos.matrizEnergetica()
    return render_template('OqueSao.html')

@app.route('/imagens/<filename>')
def imagens(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'imagens'), filename)

if __name__ == '__main__':
    app.run(debug=True)
