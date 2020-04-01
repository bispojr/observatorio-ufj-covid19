google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

  var parametros = {};

  parametros.jatai ={};

  parametros.jatai.resumo = {};
  parametros.jatai.resumo = {};
  parametros.jatai.resumo.query = 'SELECT A, B, D, E, F, G';
  parametros.jatai.resumo.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.jatai.resumo.googleSheet += '1nCDjAvdEWVzwJjLhRkkVHiw2SK63SKcYXb7doIUI5VQ';
  parametros.jatai.resumo.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.jatai.resumo.colors = ['red', 'yellow', 'green', 'black', 'blue'];
  parametros.jatai.resumo.xTitle = 'Dia/Mês';
  parametros.jatai.resumo.yTitle = 'Número de casos';
  parametros.jatai.resumo.idDiv = 'jatai-grafico-resumo';

  parametros.mineiros ={};

  parametros.mineiros.resumo = {};
  parametros.mineiros.resumo.query = 'SELECT A, B, C, D';
  parametros.mineiros.resumo.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.mineiros.resumo.googleSheet += '1MPFPI6nZvoPjSanXFcVqh3TrWDRJ7J5SXbhKkW6p5NY';
  parametros.mineiros.resumo.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.mineiros.resumo.colors = ['green', 'brown', 'orange'];
  parametros.mineiros.resumo.xTitle = 'Dia/Mês';
  parametros.mineiros.resumo.yTitle = 'Número de casos';
  parametros.mineiros.resumo.idDiv = 'mineiros-grafico';

  buildChart(parametros.jatai.resumo);
  buildChart(parametros.mineiros.resumo);
}
