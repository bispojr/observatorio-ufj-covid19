google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawJatai() {
      var queryString = encodeURIComponent('SELECT A, D, E, F, G');

      var query = new google.visualization.Query(
          'https://docs.google.com/spreadsheets/d/1nCDjAvdEWVzwJjLhRkkVHiw2SK63SKcYXb7doIUI5VQ/gviz/tq?sheet=Dados&headers=1&tq=' + queryString);
      query.send(drawJataiPasso2);
    }

    function drawJataiPasso2(response) {
      if (response.isError()) {
        alert('Erro in consulta: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
      }

      var data = response.getDataTable();

      var options = {
        	//width: 600,
    		//height: 400,
          curveType: 'function',
          legend: { position: 'top' , maxLines: 2},
          isStacked: true,
          colors: ['red', 'yellow', 'green', 'black', 'blue'],
          vAxis: {	title: 'Número de casos',
      				viewWindow: {
				        min: 0,
				        max: 12
				    },
				    ticks: [0, 2, 4, 6, 8, 10, 12] 
				},
          hAxis: {
          		title: 'Dia (Março)',
          		ticks: [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
          	}
        };

        var chart = new google.visualization.LineChart(document.getElementById('jatai-grafico'));

        chart.draw(data, options);
    }

    function drawMineiros() {
      var queryString = encodeURIComponent('SELECT A, B, C');

      var query = new google.visualization.Query(
          'https://docs.google.com/spreadsheets/d/1MPFPI6nZvoPjSanXFcVqh3TrWDRJ7J5SXbhKkW6p5NY/gviz/tq?sheet=Dados&headers=1&tq=' + queryString);
      query.send(drawMineirosPasso2);
    }

    function drawMineirosPasso2(response) {
      if (response.isError()) {
        alert('Erro in consulta: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
      }

      var dataMineiros = response.getDataTable();

      var optionsMineiros = {
      curveType: 'function',
      legend: { position: 'top' , maxLines: 2},
      isStacked: true,
      colors: ['green', 'brown'],
      vAxis: {	title: 'Número de casos',
  				viewWindow: {
			        min: 0,
			        max: 50
			    },
			    ticks: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50] 
			},
      hAxis: {
      		title: 'Dia (Março)',
      		ticks: [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
      	}
    };

    var chartMineiros = new google.visualization.LineChart(document.getElementById('mineiros-grafico'));

    chartMineiros.draw(dataMineiros, optionsMineiros);
    }

  function drawChart() {
    drawJatai();
    drawMineiros();
    coletaNoticias();
  }
