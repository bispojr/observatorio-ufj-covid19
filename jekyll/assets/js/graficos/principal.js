google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

  var jatai = {};
  
  jatai.query = 'SELECT A, B, D, E, F, G';
  jatai.googleSheet = 'https://docs.google.com/spreadsheets/d/1nCDjAvdEWVzwJjLhRkkVHiw2SK63SKcYXb7doIUI5VQ/gviz/tq?sheet=Dados&headers=1&tq=';
  jatai.colors = ['red', 'yellow', 'green', 'black', 'blue'];
  jatai.xTitle = 'Dia (Março)';
  jatai.yTitle = 'Número de casos';
  jatai.idDiv = 'jatai-grafico';
  
  buildChart(jatai);

  var mineiros = {};

  mineiros.query = 'SELECT A, B, C';
  mineiros.googleSheet = 'https://docs.google.com/spreadsheets/d/1MPFPI6nZvoPjSanXFcVqh3TrWDRJ7J5SXbhKkW6p5NY/gviz/tq?sheet=Dados&headers=1&tq=';
  mineiros.colors = ['green', 'brown'];
  mineiros.xTitle = 'Dia (Março)';
  mineiros.yTitle = 'Número de casos';
  mineiros.idDiv = 'mineiros-grafico';
  
  buildChart(mineiros);

  coletaNoticias();
}
