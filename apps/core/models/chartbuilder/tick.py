import datetime
import math
from pprint import pprint

class Tick():
    """
    Classe para criar os pontos no gráfico

    methods:
        getTicks
    """
    def getTicks(dados, cols):
        """
        Função para gerar os pontos de um gráfico

        args:
            dados
            cols

        return:
            Dict com os pontos para o gráfico
                - tickX
                - tickY
        """
        
        listData = []
        for row in dados:
            listData.append(row["Data"])

        #Criação do ticks X
        minX = min(listData)
        maxX = max(listData)

        # Converte em dias
        diffDias = maxX-minX
        diffDias = math.ceil(diffDias.total_seconds() / (60 * 60 * 24))

        ticksX = []
        stepX = math.ceil(diffDias/5)
        offsetX = diffDias%stepX

        if offsetX > 0:
            ticksX.append(minX)

        i = offsetX
        while i <= diffDias:
            val = minX + datetime.timedelta(days=i)
            ticksX.append(val)
            i += stepX

        v = []
        for t in ticksX:
            v.append(str(t.strftime("%d-%b-%Y")))

        ticksX = v
    
        #Criação do ticks Y
        minY = 0

        i = 1
        maxY = -1
        numCols = len(cols) -1
        while i <= numCols:
            listCol = []
            for row in dados:
                val = row[ cols[i] ]
                if val == None:
                    val = 0
                listCol.append(val)
            #pprint(listCol)
            maxY = max(max(listCol), maxY)
            i += 1         

        ticksY = []
        stepY = math.ceil((maxY-minY)/5)

        stepGold = [1, 5, 10, 20, 50, 100, 200, 500]
        i = 0
        size = len(stepGold)
        while i < size:
            if stepY <= stepGold[i]:
                stepY = stepGold[i]
                break
            i += 1
       
        lastValue = 0
        i = minY
        while i < maxY:
            ticksY.append(i)
            lastValue = i
            i += stepY

        ticksY.append(lastValue + stepY)

        ticks = {
            "tickX": ticksX,
            "tickY": ticksY
        }

        return ticks