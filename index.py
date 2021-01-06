from flask import Flask, render_template, request, url_for
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

@app.route('/inversa')
def inversa():
    return render_template('inversa.html')

@app.route('/inversa_resultado', methods=['POST'])
def inversa_resultado():
    seed(1)
    data = random()
    cantidadmeses = int(request.form['cantidadmeses'])
    n_bins = request.form['input1']
    n_samples = request.form['input2']
    resinv = inverse_transform_sampling(float(data), int(n_bins), int(n_samples))
    meses = len(resinv)
    numeracionTabla = cantidadmeses
    numeracion = []
    for x in range(1,numeracionTabla+1):
        numeracion.append(x)

    numbersAleatory = []
    for positivo in resinv:
        if(len(numbersAleatory) < cantidadmeses):
            aux = round(np.abs(positivo), 4)
            numbersAleatory.append(aux)

    invetarioInicial = []
    for invetarioInc in range(1,cantidadmeses+1):
        # auxInv = int(uniform(10,300))
        invetarioInicial.append(int(n_bins))

    reorden = int(request.form['r'])

    demandaAjustada = []
    for demandaAj in range(1,cantidadmeses+1):
        factorEstacional = uniform(1.0, 2.5)
        demanda = int(uniform(1,8))
        resultadoDemandaFactor = round(int(demanda * factorEstacional), 4)
        demandaAjustada.append(resultadoDemandaFactor)

    invetarioFinal = []
    for invetarioF in range(0,cantidadmeses):
        invfinal = invetarioInicial[invetarioF] - demandaAjustada[invetarioF]
        invetarioFinal.append(invfinal)

    # print(invetarioFinal)

    for inventarioFinaltoinventarioInicial in range(1, cantidadmeses):
        refactor = invetarioFinal[inventarioFinaltoinventarioInicial-1]
        invetarioInicial[inventarioFinaltoinventarioInicial] = refactor
        invf = invetarioInicial[inventarioFinaltoinventarioInicial] - demandaAjustada[inventarioFinaltoinventarioInicial]
        invetarioFinal[inventarioFinaltoinventarioInicial] = invf

    faltante = []
    for faltanteInv in range(0,cantidadmeses):
        if (invetarioFinal[faltanteInv] >= 0):
            faltante.append(0)
        else:
            faltante.append(abs(invetarioFinal[faltanteInv]))

    orden = []
    for ordenInv in range(0,cantidadmeses):
        if((invetarioFinal[ordenInv] < reorden) and len(orden)==0 ):
            # orden[0] = 1
            orden.append(1)
        else:
            if((invetarioFinal[ordenInv] < reorden) and len(orden)==1 ):
                # orden[0] = 0
                orden.append(0)
            else:
                if(invetarioFinal[ordenInv] > reorden and len(orden)==0):
                    # orden[0] = 1
                    orden.append(1)
                else:
                    # orden[0] = 0
                    orden.append(0)

    inventarioPromedio = []
    for inventarioProm in range(0,cantidadmeses):
        promedioaux = (invetarioInicial[inventarioProm] + invetarioFinal[inventarioProm]) / 2
        inventarioPromedio.append(int(promedioaux))

    q = []
    qq = len(n_samples)
    for x in range(0,qq):
        q.append(x)

    return render_template('inversa.html',
    numeracion=numeracion,
    n_bins=invetarioInicial,
    n_samples=n_samples,
    resinv=numbersAleatory,
    demandaAjustada=demandaAjustada,
    inventariofinal=invetarioFinal,
    faltante=faltante,
    orden=orden,
    inventarioPromedio=inventarioPromedio,
    q=q)

@app.route('/reporte_inversa.pdf')
def reporte_pdf():
    html = render_template('inversa.html')
    return render_pdf(HTML(string=html))

# @app.route('/reporte_home.pdf')
# def reporte_home():
#     html = render_template('index.html')
#     return render_pdf(HTML(string=html))

if __name__ == '__main__':
    app.run(debug=True)
    # app.run();