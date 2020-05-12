google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

  buildChart(getParametros("rioverde","todas"));
  buildChart(getParametros("rioverde","monitorados"));
  buildChart(getParametros("rioverde","resumo"));
}
