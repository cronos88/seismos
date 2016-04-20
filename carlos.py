# -*- coding: UTF-8 -*-
"""
Se ejecuta en Python 2.7
Por: Carlos Andres Millan
"""

import requests, os
from datetime import datetime
from colorama import init
from colorama import Fore, Back, Style

init()
os.system('cls')
response = requests.get("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
data = response.json()

#En http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php está la estructura
#de los datos del GeoJSON

for sismo in data['features']:
	lugar = sismo['properties']['place']
	mag = sismo['properties']['mag']
	segundos = (sismo['properties']['time'])/1000
	tiempo_sismo = datetime.fromtimestamp(segundos)
	tiempo_ahora = datetime.now()
	dif = tiempo_ahora - tiempo_sismo
	prof = sismo['geometry']['coordinates']
	
    #Utilizo la librería llamada Colorama para mostrar con colores los sismos cuya intensidad esté en un rango cualquiera."""
	if mag<4.0:
	    print(Fore.WHITE+"Hace:{0}h:{1}m".format(dif.seconds//3600, (dif.seconds//60)%60)+" 	Mag:"+str(mag)+ "  "+"Lugar: "+str(lugar)+Back.RESET)
	    
	elif mag>=4 and mag <5.9:
	    print(Fore.YELLOW+"Hace:{0}h:{1}m".format(dif.seconds//3600, (dif.seconds//60)%60)+" 	Mag:"+str(mag)+ "  "+"Lugar: "+str(lugar)+Back.RESET)
	    
	elif mag>6:
		print(Fore.RED+"Hace:{0}h:{1}m".format(dif.seconds//3600, (dif.seconds//60)%60)+" 	Mag:"+str(mag)+ "  "+"Lugar: "+str(lugar)+Back.RESET)

	elif mag>6 and prof[2] < 30.0:
		print(Fore.WHITE+Back.RED+"Hace:{0}h:{1}m".format(dif.seconds//3600, (dif.seconds//60)%60)+"    Mag:"+str(mag)+ "  "+"Lugar: "+str(lugar)+Back.RESET)
