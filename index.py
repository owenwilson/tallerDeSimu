from flask import Flask, render_template
from tinversa import *

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

if __name__ == '__main__':
    app.run(debug=True)
    # app.run();