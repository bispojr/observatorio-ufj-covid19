google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawProjection);

function drawProjection() {

  buildProjection(getProjectionParameters("rioverde"));
}
