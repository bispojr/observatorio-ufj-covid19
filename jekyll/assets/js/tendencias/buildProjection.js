var corGrafico = {};

corGrafico.confirmados = "red";
corGrafico.descartados = "pink";
corGrafico.investigados = "yellow";
corGrafico.notificados = "green";
corGrafico.isolados = "black";
corGrafico.internados = "blue";
corGrafico.monitorados = "brown";
corGrafico.recuperados = "purple";
corGrafico.obitos = "gray";
corGrafico.excluidos = "orange";

function buildProjection(param) {

  var url = "https://covidgoias.ufg.br/service/indicators/projections?cd_geocmu=" + param.cd_geocmu + "&lang=pt-br";

  $.ajax({
    type: 'GET',
    url: url,
    contentType: 'application/json',
    headers: {
      'Access-Control-Allow-Credentials' : true,
      'Access-Control-Allow-Origin':'https://www.deolhonocorona.com',
      'Access-Control-Allow-Methods':'GET',
      'Access-Control-Allow-Headers':'application/json'
    },
    success: function(data) {
      console.log(data);
    },
    error: function(error) {
      console.log("FAIL....=================");
    }
  });
  /*$.getJSON(url, function(dataJson) {
    
    console.log(dataJson);

    //Build a data table from dataJson
    //  var data = response.getDataTable();

    //Criação do ticks X
    /*var minX = data.getColumnRange(0).min;
    var maxX = data.getColumnRange(0).max;

    //Converte em dias
    var minXDias = Math.ceil(minX / (1000 * 60 * 60 * 24));
    var maxXDias = Math.ceil(maxX / (1000 * 60 * 60 * 24));
    var diffDias = maxXDias-minXDias;

    var ticksX = [];
    var stepX = Math.ceil(diffDias/5);
    var offsetX = diffDias%stepX;

    if(offsetX > 0){
      var val = minX * (1000 * 60 * 60 * 24);
      val = new Date(val);
      ticksX.push(minX);
    }

    for(var i=minXDias+offsetX; i <=maxXDias; i += stepX){
        var val = i * (1000 * 60 * 60 * 24);
        val = new Date(val);
        ticksX.push(val);
    }

    //Criação do ticks Y
    var minY = 0;

    var maxY = -1;
    for(var i=1; i<=data.getNumberOfColumns()-1; i++){
        maxY = Math.max(data.getColumnRange(i).max, maxY);
    }

    var ticksY = [];
    var stepY = Math.ceil((maxY-minY)/5);

    var stepGold = [1, 5, 10, 20, 50, 100, 200, 500];
    for(var i=0; i<stepGold.length; i++){
        if(stepY <= stepGold[i]){
            stepY = stepGold[i];
            break;
        }
    }

    var lastValue = 0;
    for(var i=minY; i <maxY; i += stepY){
        ticksY.push(i);
        lastValue = i;
    }
    ticksY.push(lastValue + stepY);

    //Option

    var options = {
        curveType: 'function',
        legend: { position: 'top' , maxLines: 2},
        isStacked: true,
        colors: param.colors,
        pointSize: 5,
        hAxis: {
            title: param.xTitle,
            format: 'd/M',
            //viewWindow: {min: minX, max: maxX},
            ticks: ticksX
            //gridlines: {count: stepX}
        },
        vAxis: {    
            title: param.yTitle,
            viewWindow: { min: minY },
            //ticks: ticksY 
            gridlines: {count: 5}
            }
        
      };

      var chart = new google.visualization.LineChart(document.getElementById(param.idDiv));
      chart.draw(data, options);


      //Data de atualização informada em cada página
      if(param.data_atualizacao != false){
          var mes = [
            "janeiro", "fevereiro", "março", 
            "abril", "maio", "junho", 
            "julho", "agosto", "setembro", 
            "outubro", "novembro", "dezembro"];

          $(param.data_atualizacao).text(maxX.getDate() + " de " + mes[maxX.getMonth()] + " de " + maxX.getFullYear());
      }
  });*/
}

function getProjectionParameters(cidade){

  switch(cidade){
    case "jatai":
      return getJataiParameters();
      break;
    case "rioverde":
      return getRioVerdeParameters();
      break;
  }
}

function getJataiParameters(){
  
  var parametros = {};
  
  parametros.query = 'SELECT A, B, D, E, F, G';
  parametros.colors = [
    corGrafico.confirmados, corGrafico.investigados, corGrafico.notificados, 
    corGrafico.isolados, corGrafico.internados];
  parametros.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.googleSheet += '1nCDjAvdEWVzwJjLhRkkVHiw2SK63SKcYXb7doIUI5VQ';
  parametros.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.xTitle = 'Dia/Mês';
  parametros.yTitle = 'Número de casos';
  parametros.idDiv = 'jatai-grafico-resumo';
  parametros.data_atualizacao = "#data-atualizacao-jatai";
  parametros.cd_geocmu = "5211909";

  return parametros;

}

function getRioVerdeParameters(){
/*
  B = Confirmados,  C = Descartados 
  D = Investigados  E= Notificados 
  F = Isolados      G = Internados  
  H = Monitorados   I = Recuperados
*/

  var parametros ={};

  parametros.googleSheet = 'https://docs.google.com/spreadsheets/d/'
  parametros.googleSheet += '1jrhI1EjA8KJNJ5CKEDe-oREPjeRnYviVKp9AJPPMlLE';
  parametros.googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq=';
  parametros.xTitle = 'Dia/Mês';
  parametros.yTitle = 'Número de casos';
  parametros.cd_geocmu = "5218805";

  return parametros;
}