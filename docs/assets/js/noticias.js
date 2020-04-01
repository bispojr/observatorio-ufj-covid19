google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(coletaNoticias);

function coletaNoticias() {
  var queryString = encodeURIComponent('SELECT A, B, C, D, E, F');

  var query = new google.visualization.Query(
      'https://docs.google.com/spreadsheets/d/178wCqYRbSXRQui2l3pLOI3Yz5OktNzNvWr_AE2GWPEg/gviz/tq?sheet=Dados&headers=1&tq=' + queryString);
  query.send(coletaNoticiasPasso2);
}

function coletaNoticiasPasso2(response) {
  if (response.isError()) {
    alert('Erro na consulta: ' + response.getMessage() + ' ' + response.getDetailedMessage());
    return;
  }

  //var data = JSON.parse(response.getDataTable().toJSON());
  var data = response.getDataTable();

  for (var i = 0; i < 3; i++) {

    var chamadaCurta = data.getValue(i,0);
    var descricao = data.getValue(i,2);
    var icone = data.getValue(i,4);
    var url = data.getValue(i,5);

    var selector = "#noticia0" + (i+1);
    
    $(selector + " span").addClass(icone);
    $(selector + " header h3").text(chamadaCurta);
    $(selector + " p").text(descricao);
    $(selector + " a").attr("href", url);
    /*$(selector + "> a").hover(function(){
      $(selector).css("background-color", "white");
      }, function(){
      $(selector).css("background-color", "transparent");
    });*/
  }

}