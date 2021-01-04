from flask import Flask, render_template, request
from tiv import *
from random import seed
from random import random
from random import uniform
import numpy as np
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

@app.route('/inversa', methods=['GET'])
def inversa():
    return render_template('inversa.html')

@app.route('/inversa_resultado', methods=['POST'])
def inversa_resultado():
    seed(1)
    data = random()
    n_bins = request.form['input1']
    n_samples = request.form['input2']
    resinv = inverse_transform_sampling(float(data), int(n_bins), int(n_samples))
    meses = len(resinv)
    numeracion = []
    for x in range(1,meses+1):
        numeracion.append(x)

    numbersAleatory = []
    for positivo in resinv:
        aux = round(np.abs(positivo), 4)
        numbersAleatory.append(aux)

    invetarioInicial = []
    for invetarioInc in range(1,meses+1):
        auxInv = int(uniform(10,300))
        invetarioInicial.append(auxInv)

    r = request.form['r']

    demandaAjustada = []
    for demandaAj in range(1,meses+1):
        factorEstacional = uniform(1.0, 2.5)
        demanda = int(uniform(1,8))
        resultadoDemandaFactor = round(int(demanda * factorEstacional), 4)
        demandaAjustada.append(resultadoDemandaFactor)

    invetarioFinal = []
    for invetarioF in range(0,meses):
        invf = invetarioInicial[invetarioF] - demandaAjustada[invetarioF]
        invetarioFinal.append(invf)

    faltante = []
    for faltanteInv in range(0,meses):
        if(invetarioInicial[faltanteInv] - demandaAjustada[faltanteInv] > 0):
            faltante.append(0)
        else:
            if(invetarioInicial[faltanteInv] - demandaAjustada[faltanteInv] < 0):
                faltanteaux = invetarioInicial[faltanteInv] - demandaAjustada[faltanteInv]
                faltante.append(faltanteaux)

    for inventarioFinaltoinventarioInicial in range(1, meses):
        refactor = invetarioFinal[inventarioFinaltoinventarioInicial-1]
        invetarioInicial[inventarioFinaltoinventarioInicial] = refactor
        invf = invetarioInicial[inventarioFinaltoinventarioInicial] - demandaAjustada[inventarioFinaltoinventarioInicial]
        invetarioFinal[inventarioFinaltoinventarioInicial] = invf

    # orden = []
    # for ordenInv in range(0,meses):
    #     if(invetarioFinal[ordenInv] < r):
    #         orden.append(1)
    #     else:
    #         if(invetarioFinal[ordenInv > r]):
    #             orden.append

    inventarioPromedio = []
    for inventarioProm in range(0,meses):
        promedioaux = (invetarioInicial[inventarioProm] + invetarioFinal[inventarioProm]) / 2
        inventarioPromedio.append(int(promedioaux))

    return render_template('inversa.html',
    numeracion=numeracion,
    n_bins=invetarioInicial,
    n_samples=n_samples,
    resinv=numbersAleatory,
    demandaAjustada=demandaAjustada,
    inventariofinal=invetarioFinal,
    faltante=faltante,
    inventarioPromedio=inventarioPromedio)

@app.route('/reporte_poisson.pdf')
def reporte_pdf():
    html = render_template('poisson.html')
    return render_pdf(HTML(string=html))

# @app.route('/reporte_home.pdf')
# def reporte_home():
#     html = render_template('index.html')
#     return render_pdf(HTML(string=html))

if __name__ == '__main__':
    app.run(debug=True)
    # app.run();