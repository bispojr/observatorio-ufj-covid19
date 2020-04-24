google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

  var parametros = {};

  parametros.mineiros ={};

  parametros.mineiros.resumo = {};
  parametros.mineiros.resumo.query = 'SELECT A, E, H, I, G';
  parametros.mineiros.resumo.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.mineiros.resumo.googleSheet += '1MPFPI6nZvoPjSanXFcVqh3TrWDRJ7J5SXbhKkW6p5NY';
  parametros.mineiros.resumo.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.mineiros.resumo.colors = ["red", 'purple', 'blue', 'black'];
  parametros.mineiros.resumo.xTitle = 'Dia/Mês';
  parametros.mineiros.resumo.yTitle = 'Número de casos';
  parametros.mineiros.resumo.idDiv = 'mineiros-grafico-resumo';
  parametros.mineiros.resumo.data_atualizacao = "#data-atualizacao-mineiros";

  parametros.mineiros.todas = {};
  parametros.mineiros.todas.query = 'SELECT A, B, C, D, E, F, G, H';
  parametros.mineiros.todas.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.mineiros.todas.googleSheet += '1MPFPI6nZvoPjSanXFcVqh3TrWDRJ7J5SXbhKkW6p5NY';
  parametros.mineiros.todas.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.mineiros.todas.colors = ['green', 'brown', 'orange', 'red', 'pink', 'gray', 'purple'];
  parametros.mineiros.todas.xTitle = 'Dia/Mês';
  parametros.mineiros.todas.yTitle = 'Número de casos';
  parametros.mineiros.todas.idDiv = 'mineiros-grafico-todas';
  parametros.mineiros.todas.data_atualizacao = false;

  parametros.mineiros.monitorados = {};
  parametros.mineiros.monitorados.query = 'SELECT A, B, C';
  parametros.mineiros.monitorados.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.mineiros.monitorados.googleSheet += '1MPFPI6nZvoPjSanXFcVqh3TrWDRJ7J5SXbhKkW6p5NY';
  parametros.mineiros.monitorados.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.mineiros.monitorados.colors = ['green', 'brown'];
  parametros.mineiros.monitorados.xTitle = 'Dia/Mês';
  parametros.mineiros.monitorados.yTitle = 'Número de casos';
  parametros.mineiros.monitorados.idDiv = 'mineiros-grafico-monitorados';
  parametros.mineiros.monitorados.data_atualizacao = false;

  buildChart(parametros.mineiros.resumo);
  buildChart(parametros.mineiros.todas);
  buildChart(parametros.mineiros.monitorados);
}
