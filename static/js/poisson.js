function miFuncion(){
const euler = 2.718;

let lambda = document.getElementById("lambda").value;
let x = document.getElementById("x").value;
let varA = Math.pow(euler,-lambda);
let varB = Math.pow(lambda,x)

let lambdaA = document.getElementById("lambdaB").value;
let a = document.getElementById("b").value;
let varC = Math.pow(euler,-lambdaA);
let varD = Math.pow(lambda,x);

let lambdaB = document.getElementById("lambdaC").value;
let b = document.getElementById("c").value;
let varE = Math.pow(euler,-lambdaB);
let varF = Math.pow(lambda,x);

let lambdaC = document.getElementById("lambdaD").value;
let c = document.getElementById("d").value;
let varG = Math.pow(euler,-lambdaC);
let varH = Math.pow(lambda,x);

function factorial(n){
    if(n==0){
        return 1;
    }
    return n * factorial(n-1);
}

function probabilidad(varA, varB, x){
    let resProbabilidad = ((varA*varB)/factorial(x));
    return resProbabilidad;
}

let resultado = probabilidad(varA, varB, x);
let mes2 = probabilidad(varC, varD, a);
let mes3 = probabilidad(varE, varF, b);
let mes4 = probabilidad(varG, varH, c);
document.getElementById("demo").innerHTML = resultado;


var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Mes1', 'Mes2', 'Mes3', 'Mes4', 'Mes5', 'Mes6', 'Mes7', 'Mes8', 'Mes9', 'Mes10', 'Mes11', 'Mes12'],
            datasets: [{
                label: 'Inventarios',
                data: [resultado, mes2, mes3, mes4],
                backgroundColor: [
                    'rgba(66, 134, 244, 0.2)',
                    'rgba(74, 135, 72, 0.2)',
                    'rgba(229, 89, 50, 0.2)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });

document.getElementById('lambda').value='';
document.getElementById('x').value='';
}