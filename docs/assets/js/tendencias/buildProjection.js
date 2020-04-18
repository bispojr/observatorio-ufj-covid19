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
  //var url = "/assets/js/tendencias/" + param.cd_geocmu + ".txt";

  $.getJSON(url, function(dataJson) {

    var diaMes = dataJson.timeseries.chartResult[0].dataResult.labels;
    var confirmados = dataJson.timeseries.chartResult[0].dataResult.datasets[0].data;
    var projetados = dataJson.timeseries.chartResult[0].dataResult.datasets[1].data;

    //Parser na criação da data
    var dataUltimoModelo = dataJson.timeseries.chartResult[0].last_model_date;
    dataUltimoModelo = dataUltimoModelo.split("T")[0].split("-");
    dataUltimoModelo = new Date(dataUltimoModelo[0], dataUltimoModelo[1] - 1, dataUltimoModelo[2]);

    var data = new google.visualization.DataTable();
    data.addColumn('date', 'Dia/Mês');
    data.addColumn('number', 'Projetados');
    data.addColumn('number', 'Confirmados');

    data.addRows(projetados.length);

    for (var i = 0; i < confirmados.length; i++) {
      
      var dateVal = diaMes[i].split("-");
      dateVal = new Date(dateVal[2], dateVal[1]-1, dateVal[0]);
      
      data.setCell(i, 0, dateVal);
      data.setCell(i, 2, confirmados[i]);
    }

    //Ligar os gráficos
    data.setCell(confirmados.length-1, 0, dateVal);
    data.setCell(confirmados.length-1, 1, confirmados[confirmados.length-1]);

    for (var i = confirmados.length; i < projetados.length; i++) {
      
      var dateVal = diaMes[i].split("-");
      dateVal = new Date(dateVal[2], dateVal[1]-1, dateVal[0]);
      
      data.setCell(i, 0, dateVal);
      data.setCell(i, 1, projetados[i]);
    }

    //Criação do ticks X
    var minX = data.getColumnRange(0).min;
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
        animation:{
          duration: 1000,
          startup: true,
        },
        series: {
          0: { lineDashStyle: [4, 4], pointShape: { type: 'square' }, pointSize: 10 }
        },
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

          $(param.data_atualizacao).text(
            dataUltimoModelo.getDate() + " de " + 
            mes[dataUltimoModelo.getMonth()] + " de " + 
            dataUltimoModelo.getFullYear()
          );
      }

  });
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
  
  parametros.colors = [
    "royalblue", corGrafico.confirmados];
  parametros.xTitle = 'Dia/Mês';
  parametros.yTitle = 'Número de casos';
  parametros.idDiv = 'jatai-tendencias';
  parametros.data_atualizacao = "#data-atualizacao-jatai";
  parametros.cd_geocmu = "5211909";

  return parametros;

}

function getRioVerdeParameters(){

  var parametros ={};

  parametros.colors = [
    "royalblue", corGrafico.confirmados];
  parametros.xTitle = 'Dia/Mês';
  parametros.yTitle = 'Número de casos';
  parametros.idDiv = 'rioverde-tendencias';
  parametros.data_atualizacao = "#data-atualizacao-rioverde";
  parametros.cd_geocmu = "5218805";

  return parametros;
}
