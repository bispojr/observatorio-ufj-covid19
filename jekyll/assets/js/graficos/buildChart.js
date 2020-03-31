function buildChart(param) {
  var queryString = encodeURIComponent(param.query);

  var query = new google.visualization.Query(param.googleSheet + queryString);
  
  query.send(function (response) {
    if (response.isError()) {
      alert('Erro in consulta: ' + response.getMessage() + ' ' + response.getDetailedMessage());
      return;
    }

    var data = response.getDataTable();

    //Criação do ticks X
    var minX = data.getColumnRange(0).min;
    var maxX = data.getColumnRange(0).max;

    var ticksX = [];
    var stepX = Math.ceil((maxX-minX)/5);
    var offsetX = (maxX-minX)%stepX;
    
    if(offsetX > 0)
    	ticksX.push(minX);

    for(var i=minX+offsetX; i <=maxX; i += stepX){
    	ticksX.push(i);
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
        hAxis: {
        		title: param.xTitle,
        		viewWindow: {min: minX, max: maxX},
        		ticks: ticksX
        	},
        vAxis: {	title: param.yTitle,
    				viewWindow: { min: minY },
  		    ticks: ticksY 
  		}
        
      };

      var chart = new google.visualization.LineChart(document.getElementById(param.idDiv));
      chart.draw(data, options);
  });
}