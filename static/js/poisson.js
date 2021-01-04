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
        type: 'line',
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

$('#downloadPdf').click(function(event) {
    // get size of report page
    var reportPageHeight = $('#reportPage').innerHeight();
    var reportPageWidth = $('#reportPage').innerWidth();
  
    // create a new canvas object that we will populate with all other canvas objects
    var pdfCanvas = $('<canvas />').attr({
      id: "canvaspdf",
      width: reportPageWidth,
      height: reportPageHeight
    });
  
    // keep track canvas position
    var pdfctx = $(pdfCanvas)[0].getContext('2d');
    var pdfctxX = 0;
    var pdfctxY = 0;
    var buffer = 100;
  
    // for each chart.js chart
    $("canvas").each(function(index) {
      // get the chart height/width
      var canvasHeight = $(this).innerHeight();
      var canvasWidth = $(this).innerWidth();
  
      // draw the chart into the new canvas
      pdfctx.drawImage($(this)[0], pdfctxX, pdfctxY, canvasWidth, canvasHeight);
      pdfctxX += canvasWidth + buffer;
  
      // our report page is in a grid pattern so replicate that in the new canvas
      if (index % 2 === 1) {
        pdfctxX = 0;
        pdfctxY += canvasHeight + buffer;
      }
    });
  
    // create new pdf and add our new canvas as an image
    var pdf = new jsPDF('l', 'pt', [reportPageWidth, reportPageHeight]);
    pdf.addImage($(pdfCanvas)[0], 'PNG', 0, 0);
  
    // download the pdf
    pdf.save('filename.pdf');
});