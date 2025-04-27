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
    graficos.crescimentoEmpregados()
    return render_template('OqueSao.html')

@app.route('/imagens/<filename>')
def imagens(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'imagens'), filename)

@app.route('/hidrica')
def hidrica():
    return render_template('hidrica.html')

@app.route('/solar')
def solar():
    graficos.aumentoEconomiaSolar()
    return render_template('solar.html')

@app.route('/eolica')
def eolica():
    return render_template('eolica.html')

@app.route('/biomassa')
def biomassa():
    return render_template('biomassa.html')

@app.route('/geotermica')
def geotermica():
    return render_template('geotermica.html')

@app.route('/oceanica')
def oceanica():
    return render_template('oceanica.html')

if __name__ == '__main__':
    app.run(debug=True)
