# -*- coding: UTF-8 -*-
"""
Se ejecuta en Python 2.7
Por: Carlos Andres Millan
"""

import math
import os
import requests
from colorama import Fore, Back
from datetime import datetime


"""En http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php está la
   estructura de los datos del GeoJSON"""
response = requests.get(
    "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
data = response.json()


def calcula_sismo():
    for sismo in data['features']:
        lugar = sismo['properties']['place']
        mag = sismo['properties']['mag']
        segundos = (sismo['properties']['time']) / 1000
        prof = sismo['geometry']['coordinates']
        # tiempo_sismo es la fecha y hora en que ocurrió el sismo
        tiempo_sismo = datetime.fromtimestamp(segundos)
        tiempo_ahora = datetime.now()
        dif = tiempo_ahora - tiempo_sismo
        horas = dif.seconds // 3600
        minutos = (dif.seconds // 60) % 60
        datos_sismo = "	Mag:" + str(round(mag,1)) + "	prof(km):" + str(prof[2]) + "	Lugar: " + str(lugar) + Back.RESET
        """Utilizo la librería llamada Colorama para mostrar con colores los
        sismos cuya intensidad esté en un rango cualquiera."""
        if mag < 4.0:
            print(Fore.WHITE + "Hace:{0}h:{1}m".format(horas, minutos) + datos_sismo)
            

        elif mag >= 4 and mag < 5.9:
            print(Fore.YELLOW + "Hace:{0}h:{1}m".format(horas, minutos) + datos_sismo)

        elif mag > 6:
            print(Fore.RED + "Hace:{0}h:{1}m".format(horas, minutos) + datos_sismo)

        elif mag > 6 and prof[2] < 30.0:
            print(Fore.WHITE + Back.RED + "Hace:{0}h:{1}m".format(horas, minutos) + datos_sismo)


def limpia_pantalla():
	if os.name == "posix":
		os.system("clear")
	elif os.name == ("ce", "nt", "dos"):
		os.system("cls")


if __name__ == "__main__":
	limpia_pantalla()
	titulo = "INFORMACION DE SISMOS A NIVEL MUNDIAL EN 24 HORAS"
	print titulo.center(69, '=')
	calcula_sismo()
