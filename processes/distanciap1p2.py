#
# Author: Andres Herrera
# Mail: fabio.herrera@correounivalle.edu.co
# Abstract: Calcula la distancia euclidiana entre dos puntos
# Version: 1.0 for PyWPS 4.0
# 

from math import sqrt
from pywps import Process, LiteralInput,  LiteralOutput

class DistanciaP1P2(Process):
    def __init__(self):
        inputs = [ LiteralInput('x1', 'Punto1 Coordenada X', data_type='float') ,
        LiteralInput('y1', 'Punto1 Coordenada Y', data_type='float' ), 
        LiteralInput('x2', 'Punto2 Coordenada X', data_type='float' ),  
        LiteralInput('y2', 'Punto2 Coordenada Y', data_type='float') ]
        
        outputs = [LiteralOutput('resultado', 'Resultado Calculo', data_type='float' )]

        super(DistanciaP1P2, self).__init__(
            self._handler,
            identifier='distanciap1p2',
            version='None',
            title='Distancia entre P1 y P2',
            abstract='Calcula la distancia euclidiana entre dos puntos',
            profile='',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        #bloque para realizar los calculos
        x1a= float(request.inputs['x1'][0].data)
        y1a= float(request.inputs['y1'][0].data)
        x2a= float(request.inputs['x2'][0].data)
        y2a= float(request.inputs['y2'][0].data)
        mdx = ((x1a + x2a)/2)
        mdy = ((y1a + y2a)/2)
        distanciaP1P2 = sqrt( pow(( mdx - x1a),2)  + pow(( mdy - y1a),2) )
        response.outputs['resultado'].data = float(distanciaP1P2)
        return response
    