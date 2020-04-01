google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

  var parametros = [];

  parametros["jatai"] = {};
  parametros["jatai"].query = 'SELECT A, B, D, E, F, G';
  parametros["jatai"].googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros["jatai"].googleSheet += '1nCDjAvdEWVzwJjLhRkkVHiw2SK63SKcYXb7doIUI5VQ';
  parametros["jatai"].googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros["jatai"].colors = ['red', 'yellow', 'green', 'black', 'blue'];
  parametros["jatai"].xTitle = 'Dia/Mês';
  parametros["jatai"].yTitle = 'Número de casos';
  parametros["jatai"].idDiv = 'jatai-grafico';

  parametros["mineiros"] = {};
  parametros["mineiros"].query = 'SELECT A, B, C';
  parametros["mineiros"].googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros["mineiros"].googleSheet += '1MPFPI6nZvoPjSanXFcVqh3TrWDRJ7J5SXbhKkW6p5NY';
  parametros["mineiros"].googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros["mineiros"].colors = ['green', 'brown'];
  parametros["mineiros"].xTitle = 'Dia/Mês';
  parametros["mineiros"].yTitle = 'Número de casos';
  parametros["mineiros"].idDiv = 'mineiros-grafico';

  buildChart(parametros["jatai"]);
  buildChart(parametros["mineiros"]);

  coletaNoticias();
}
