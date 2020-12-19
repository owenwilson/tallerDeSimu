from flask import Flask, render_template
from tinversa import *
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/poisson')
def poisson():
    return render_template('poisson.html')

@app.route('/binomial')
def binomial():
    return render_template('binomial.html')

@app.route('/inversa')
def inversa():
    tinversa = gfg
    return render_template('inversa.html', transformada=tinversa)

@app.route('/reporte_poisson.pdf')
def reporte_pdf():
    html = render_template('poisson.html')
    return render_pdf(HTML(string=html))

@app.route('/reporte_home.pdf')
def reporte_home():
    html = render_template('index.html')
    return render_pdf(HTML(string=html))

if __name__ == '__main__':
    app.run(debug=True)
    # app.run();