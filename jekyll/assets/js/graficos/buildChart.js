var corGrafico = {};

corGrafico.confirmados = "red";
corGrafico.descartados = "pink";
corGrafico.investigados = "yellow";
corGrafico.notificados = "green";
corGrafico.isolados = "gray";
corGrafico.internados = "blue";
corGrafico.monitorados = "brown";
corGrafico.recuperados = "purple";
corGrafico.obitos = "black";
corGrafico.excluidos = "orange";

function buildChart(param) {

  var queryString = encodeURIComponent(param.query);
  var query = new google.visualization.Query(param.googleSheet + queryString);
    
  query.send(function(response){
    if (response.isError()) {
      alert('Erro in consulta: ' + response.getMessage() + ' ' + response.getDetailedMessage());
      return ;
    }
    var data = response.getDataTable();

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
  });
}

function buildComparison() {

  var dados = {};

  dados.jatai = {};
  dados.jatai.casos = 6;
  dados.jatai.populacao = 98128;  //População estimada: https://www.jatai.go.gov.br/cidade-jatai/

  dados.rioverde = {};
  dados.rioverde.casos = 13;
  dados.rioverde.populacao = 235647; //População estimada: https://www.rioverde.go.gov.br/historia-cidade/

  dados.goias = {};
  dados.goias.casos = 335;
  dados.goias.populacao = 6003788; //População estimada: https://cidades.ibge.gov.br/brasil/go/panorama

  dados.brasil = {};
  dados.brasil.casos = 33682;
  dados.brasil.populacao = 210147125; //População estimada: https://cidades.ibge.gov.br/brasil/panorama


  var valJatai = (dados.jatai.casos/dados.jatai.populacao)*1000000;
  var valRioverde = (dados.rioverde.casos/dados.rioverde.populacao)*1000000;
  var valGoias = (dados.goias.casos/dados.goias.populacao)*1000000;
  var valBrasil = (dados.brasil.casos/dados.brasil.populacao)*1000000;

  var data = google.visualization.arrayToDataTable([
    ['Contexto', 'Casos por milhão de habitantes', { role: 'style' } ],
    ['Jataí', valJatai, 'blue'],
    ['Rio Verde', valRioverde, 'green'],
    ['Goiás', valGoias, 'yellow'],
    ['Brasil', valBrasil, 'red'],
 ]);

  //Option

  var options = {
      curveType: 'function',
      legend: { position: 'none'},
      isStacked: true,
      pointSize: 5,
      animation:{
        duration: 1000,
        startup: true,
      },
      series: {
        0: { lineDashStyle: [4, 4], pointShape: { type: 'square' }, pointSize: 10 }
      },
      hAxis: {
          title: "Contexto Geográfico"
      },
      vAxis: {    
        title: "Casos por milhão de habitantes",
        viewWindow: { min: 0 }
      }      
    };

    var chart = new google.visualization.ColumnChart(document.getElementById("comparacao-grafico"));
    chart.draw(data, options);

    //Data de atualização informada em cada página
    /*if(param.data_atualizacao != false){
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
    }*/
}