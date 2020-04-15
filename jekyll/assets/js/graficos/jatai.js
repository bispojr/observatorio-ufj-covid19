google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

  var parametros = {};

  parametros.jatai ={};

  parametros.jatai.resumo = {};
  parametros.jatai.resumo = {};
  parametros.jatai.resumo.query = 'SELECT A, B, G, I';
  parametros.jatai.resumo.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.jatai.resumo.googleSheet += '1nCDjAvdEWVzwJjLhRkkVHiw2SK63SKcYXb7doIUI5VQ';
  parametros.jatai.resumo.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.jatai.resumo.colors = ['red', 'blue', 'purple'];
  parametros.jatai.resumo.xTitle = 'Dia/Mês';
  parametros.jatai.resumo.yTitle = 'Número de casos';
  parametros.jatai.resumo.idDiv = 'jatai-grafico-resumo';
  parametros.jatai.resumo.data_atualizacao = "#data-atualizacao-jatai";

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
  parametros.jatai.monitorados.data_atualizacao = false;

  parametros.jatai.todas = {};
  parametros.jatai.todas.query = 'SELECT A, B, C, D, E, F, G, H';
  parametros.jatai.todas.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.jatai.todas.googleSheet += '1nCDjAvdEWVzwJjLhRkkVHiw2SK63SKcYXb7doIUI5VQ';
  parametros.jatai.todas.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.jatai.todas.colors = ['red', 'pink', 'yellow', 'green', 'black', 'blue', 'brown'];
  parametros.jatai.todas.xTitle = 'Dia/Mês';
  parametros.jatai.todas.yTitle = 'Número de casos';
  parametros.jatai.todas.idDiv = 'jatai-grafico-todas';
  parametros.jatai.todas.data_atualizacao = false;

  buildChart(parametros.jatai.resumo);
  buildChart(parametros.jatai.todas);
  buildChart(parametros.jatai.monitorados);
}
