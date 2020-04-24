google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

  buildChart(getParametros("jatai","resumo"));
  buildChart(getParametros("mineiros","resumo"));
  buildChart(getParametros("rioverde","resumo"));
}
