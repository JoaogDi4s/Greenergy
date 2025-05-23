from flask import Flask, render_template
from scipy.interpolate import splrep, splev
import numpy as np
import graficos
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/Quizzes')
def Quizzes():
    return render_template('Quizzes.html')

@app.route('/QuizSolar')
def QuizSolar():
    return render_template('QuizSolar.html')

# @app.route('/Estatisticas')
# def Estatisticas():
#     return render_template('Estatisticas.html')

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
    graficos.energiaHidreletrica()
    graficos.setorEnergiaHidrica()
    return render_template('hidrica.html')

@app.route('/solar')
def solar():
    graficos.aumentoEconomiaSolar()
    graficos.energiaSolarSetor()
    return render_template('solar.html')

@app.route('/eolica')
def eolica():
    graficos.geracaoEolica()
    return render_template('eolica.html')

@app.route('/biomassa')
def biomassa():
    graficos.geracaoBiomassa()
    return render_template('biomassa.html')

@app.route('/geotermica')
def geotermica():
    graficos.geracaoGeotermica()
    return render_template('geotermica.html')

@app.route('/oceanica')
def oceanica():
    graficos.geracaoOceanica()
    return render_template('oceanica.html')

if __name__ == '__main__':
    app.run(debug=True)