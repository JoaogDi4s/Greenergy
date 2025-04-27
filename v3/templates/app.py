from flask import Flask, render_template
import graficos
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('/v3/html/index.html')

@app.route('/OqueSao')
def OqueSao():
    graficos.matrizEnergetica()
    graficos.crescimentoEmpregados()
    return render_template('/v3/html/OqueSao.html')

@app.route('/imagens/<filename>')
def imagens(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'imagens'), filename)


@app.route('/hidrica')
def hidrica():
    return render_template('/v3/html/energias/hidrica.html')

@app.route('/solar')
def solar():
    graficos.aumentoEconomiaSolar()
    return render_template('/v3/html/energias/solar.html')
@app.route('/eolica')
def solar():
    
    return render_template('/v3/html/energias/eolica.html')
@app.route('/biomassa')
def solar():
    
    return render_template('/v3/html/energias/biomassa.html')
@app.route('/geotermica')
def solar():
    
    return render_template('/v3/html/energias/geotermica.html')
@app.route('/oceanica')
def solar():
    
    return render_template('/v3/html/energias/oceanica.html')


if __name__ == '__main__':
    app.run(debug=True)