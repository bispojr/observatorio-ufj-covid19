google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

var parametros = [];

parametros["jatai"] = {};
parametros["jatai"].query = 'SELECT A, B, D, E, F, G';
parametros["jatai"].googleSheet = 'https://docs.google.com/spreadsheets/d/1nCDjAvdEWVzwJjLhRkkVHiw2SK63SKcYXb7doIUI5VQ/gviz/tq?sheet=Dados&headers=1&tq=';
parametros["jatai"].colors = ['red', 'yellow', 'green', 'black', 'blue'];
parametros["jatai"].xTitle = 'Dia/Mês';
parametros["jatai"].yTitle = 'Número de casos';
parametros["jatai"].idDiv = 'jatai-grafico';

parametros["mineiros"] = {};
parametros["mineiros"].query = 'SELECT A, B, C';
parametros["mineiros"].googleSheet = 'https://docs.google.com/spreadsheets/d/1MPFPI6nZvoPjSanXFcVqh3TrWDRJ7J5SXbhKkW6p5NY/gviz/tq?sheet=Dados&headers=1&tq=';
parametros["mineiros"].colors = ['green', 'brown'];
parametros["mineiros"].xTitle = 'Dia/Mês';
parametros["mineiros"].yTitle = 'Número de casos';
parametros["mineiros"].idDiv = 'mineiros-grafico';

function drawChart() {

  buildChart("jatai");
  buildChart("mineiros");

  coletaNoticias();
}
