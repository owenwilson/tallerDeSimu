from flask import Flask, render_template, request, url_for
from tiv import *
from random import seed
from random import random
from random import uniform
import numpy as np
from singleton import Singleton
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
    reorden = int(request.form['input3'])
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

    # reorden = int(request.form['reorden'])

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

    orden = [0]
    for ordenInv in range(0,cantidadmeses-1):
        if(invetarioFinal[ordenInv] < reorden):
            orden.append(1)
        else:
            if((invetarioFinal[ordenInv] < reorden) and orden[ordenInv] == 1 ):
                orden.append(0)
            else:
                if(invetarioFinal[ordenInv] > reorden and orden[ordenInv]==0):
                    orden.append(1)
                else:
                    orden.append(0)

    inventarioPromedio = []
    for inventarioProm in range(0,cantidadmeses):
        promedioaux = (invetarioInicial[inventarioProm] + invetarioFinal[inventarioProm]) / 2
        inventarioPromedio.append(int(promedioaux))

    q = []
    qq = len(n_samples)
    for x in range(0,qq):
        q.append(x)

    contandorOrden = 0
    for x in range(len(orden)):
        if(orden[x] == 1):
            contandorOrden += orden[x]

    contandorFaltante = 0
    for x in range(len(faltante)):
        if(faltante[x] > 0 ):
            contandorFaltante += faltante[x]

    contadorInventario = 0
    for x  in range(len(inventarioPromedio)):
        if(inventarioPromedio[x] > 0):
            contadorInventario += inventarioPromedio[x]

    auxiliar = Singleton.getInstance()
    auxiliar.orden = contandorOrden
    auxiliar.faltante = contandorFaltante
    auxiliar.inventarioPromedio = contadorInventario

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

@app.route('/resultado_costos', methods=['POST'])
def resultado_costos():
    auxiliar = Singleton.getInstance()
    variable = auxiliar.orden
    variable2 = auxiliar.faltante
    variable3 = auxiliar.inventarioPromedio
    # print(variable)

    costoOrdenar = int(request.form['costoOrdenar'])
    costoFaltante = int(request.form['costoFaltante'])
    costoInventario = int(request.form['costoInventario'])

    totalCostoOrden = variable * costoOrdenar
    totalCostoFaltante = variable2 * costoFaltante
    totalCostoInventarioPromedio = variable3 * costoInventario
    totalfinal = totalCostoOrden + totalCostoFaltante + totalCostoInventarioPromedio

    return render_template('inversa.html',
    contadorAuxiliar=totalCostoOrden,
    costoFaltante=totalCostoFaltante,
    costoInventario=totalCostoInventarioPromedio,
    totalfinal=totalfinal)

@app.route('/reporte_inversa.pdf')
def reporte_pdf():
    html = render_template('inversa.html')
    return render_pdf(HTML(string=html))

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)
    # app.run();
