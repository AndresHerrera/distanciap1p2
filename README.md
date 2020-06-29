# DistanciaP1P2

**Rutina de Ejemplo para el calculo de la distancia euclidiana entre dos puntos en PyWPS 4.0**

### Copy file to pywps processes folder
```bash
$ cp distanciap1p2.py pywps-flask/processes
```

### Add instance to geoprocess list

```python

from processes.distanciap1p2 import DistanciaP1P2

processes = [
	DistanciaP1P2()
]
```

**PyWPS Server needs to be restarted**


### DescribeProcess Operation
```
http://localhost:5000/wps?request=DescribeProcess&service=WPS&identifier=distanciap1p2&version=1.0.0
```

### Execute Operation
```
http://localhost:5000/wps?service=WPS&version=1.0.0&request=Execute&identifier=distanciap1p2&dataInputs=x1=100;y1=200;x2=300;y2=788
```

### Web Implementation

```html
<div id="wps_ejemplo">
	<b>Ejecutar geoproceso (distanciap1p2) en servidor WPS </b><br>
	Punto1 (x): <input type="text" id="p1x" name="p1x"> 
	Punto1 (y): <input type="text" id="p1y" name="p1y"><br>
	Punto2 (x): <input type="text" id="p2x" name="p2x"> 
	Punto2 (y): <input type="text" id="p2y" name="p2y"><br>
	<input type="button" id="wps_ejecuta_p1p2" value="Ejecuta Calculo WPS">
	<div id="resultado_distancia_wps"></div>
</div>
```

```javascript
$("#wps_ejecuta_p1p2").click(function() 
{
	var p1x = $('#p1x').val();
	var p1y = $('#p1y').val();
	var p2x = $('#p2x').val();
	var p2y = $('#p2y').val();
	//Hago la peticion al servidor WPS
	$.get("http://localhost:5000/wps",
	{
		service: 'WPS', 
		version:'1.0.0',
		request:'Execute',
		identifier:'distanciap1p2',
		datainputs:'x1='+p1x+';y1='+p1y+';x2='+p2x+';y2='+p2y+''
	},
	function(data, status)
	{
		if(status=='success')
		{
			//Parse XML content
			console.log(data);
			xmldoc = $.parseXML(data);
			$doc = $(xmldoc);
			var eresponse = $doc.find('wps\\:ExecuteResponse').attr("statusLocation");
			var status= $doc.find('wps\\:Status').text();
			var resultadoExecWPS= $doc.find('wps\\:LiteralData').text();
			var creacionTime = $doc.find('wps\\:Status').attr("creationTime");
			$('#resultado_distancia_wps').html('<br><b>Resultado proceso mediante WPS</b><br>'+resultadoExecWPS+'<br> Creation Time: '+creacionTime);
		}
	},"text");
});
```

## Author: Andres Herrera &copy; 2020

* [@andresherrera](https://twitter.com/andresherrera)