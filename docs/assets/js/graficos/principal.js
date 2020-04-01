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

  parametros.jatai.monitorados = {};
  parametros.jatai.monitorados = {};
  parametros.jatai.monitorados.query = 'SELECT A, H, E';
  parametros.jatai.monitorados.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.jatai.monitorados.googleSheet += '1nCDjAvdEWVzwJjLhRkkVHiw2SK63SKcYXb7doIUI5VQ';
  parametros.jatai.monitorados.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.jatai.monitorados.colors = ['brown', 'green'];
  parametros.jatai.monitorados.xTitle = 'Dia/Mês';
  parametros.jatai.monitorados.yTitle = 'Número de casos';
  parametros.jatai.monitorados.idDiv = 'jatai-grafico-monitorados';

  parametros.jatai.todas = {};
  parametros.jatai.todas.query = 'SELECT A, B, C, D, E, F, G, H';
  parametros.jatai.todas.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.jatai.todas.googleSheet += '1nCDjAvdEWVzwJjLhRkkVHiw2SK63SKcYXb7doIUI5VQ';
  parametros.jatai.todas.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.jatai.todas.colors = ['red', 'pink', 'yellow', 'green', 'black', 'blue', 'brown'];
  parametros.jatai.todas.xTitle = 'Dia/Mês';
  parametros.jatai.todas.yTitle = 'Número de casos';
  parametros.jatai.todas.idDiv = 'jatai-grafico-todas';

  parametros.mineiros ={};

  parametros.mineiros.resumo = {};
  parametros.mineiros.resumo.query = 'SELECT A, B, C', 'D';
  parametros.mineiros.resumo.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.mineiros.resumo.googleSheet += '1MPFPI6nZvoPjSanXFcVqh3TrWDRJ7J5SXbhKkW6p5NY';
  parametros.mineiros.resumo.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.mineiros.resumo.colors = ['green', 'brown', 'orange'];
  parametros.mineiros.resumo.xTitle = 'Dia/Mês';
  parametros.mineiros.resumo.yTitle = 'Número de casos';
  parametros.mineiros.resumo.idDiv = 'mineiros-grafico';

  parametros.mineiros.todas = {};
  parametros.mineiros.todas.query = 'SELECT A, B, C, D, E, F, G, H';
  parametros.mineiros.todas.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.mineiros.todas.googleSheet += '1MPFPI6nZvoPjSanXFcVqh3TrWDRJ7J5SXbhKkW6p5NY';
  parametros.mineiros.todas.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.mineiros.todas.colors = ['green', 'brown', 'orange', 'red', 'pink', 'gray', 'purple'];
  parametros.mineiros.todas.xTitle = 'Dia/Mês';
  parametros.mineiros.todas.yTitle = 'Número de casos';
  parametros.mineiros.todas.idDiv = 'mineiros-grafico-todas';

  parametros.mineiros.monitorados = {};
  parametros.mineiros.monitorados.query = 'SELECT A, B, C';
  parametros.mineiros.monitorados.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.mineiros.monitorados.googleSheet += '1MPFPI6nZvoPjSanXFcVqh3TrWDRJ7J5SXbhKkW6p5NY';
  parametros.mineiros.monitorados.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.mineiros.monitorados.colors = ['green', 'brown'];
  parametros.mineiros.monitorados.xTitle = 'Dia/Mês';
  parametros.mineiros.monitorados.yTitle = 'Número de casos';
  parametros.mineiros.monitorados.idDiv = 'mineiros-grafico-monitorados';

  buildChart(parametros.jatai.resumo);
  buildChart(parametros.jatai.todas);
  buildChart(parametros.jatai.monitorados);

  buildChart(parametros.mineiros.resumo);
  buildChart(parametros.mineiros.todas);
  buildChart(parametros.mineiros.monitorados);

  coletaNoticias();
}
