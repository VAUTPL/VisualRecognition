import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
import time
from pprint import pprint
from decimal import Decimal
from numpy import array


def visual_recognition(foto):
	visual_recognition = VisualRecognitionV3('2016-05-20', api_key='711fd2ddb6a5fca26191e3d9eddc2f9bf8dc89f6')

	with open(join(dirname(__file__), foto), 'rb') as image_file:
		    data=json.dumps(visual_recognition.classify(images_file=image_file, threshold=0.1,
                                            classifier_ids=['Laboratorio50_1483953749']), indent=2, sort_keys=True)
	jsonToPython = json.loads(data)
	#print(data)
	datoslista = json.dumps(jsonToPython)
	data1 = json.loads(datoslista)	 
	lista = []
	lista2 = []
	#nombre=''
	#score=0.00000
	#matriz = [nombre, score]
	for element in data1["images"][0]["classifiers"][0]["classes"]:
	    lista.append(element["class"])
	    lista.append(element["score"])
	    lista2.append(element["score"])
	    #matriz.append(element["score"],element["class"])
	print lista   
	print 'el nro mayor es: ', mayor(lista2)
	#if (mayor(lista)>=0.997000):
		#print 'Abrir Puerta'
	exit()
#metodo que si el porcetnaje esta dentro del rango para abrir la puerta
def mayor(lista):
    if lista ==[]:
        return("error")
    elif len(lista) == 1:
        return(lista)
    lista_nueva = 0
    while lista != []:
        primero = lista[0]
        if lista_nueva > primero:
            lista_nueva = lista_nueva
        else:
            lista_nueva =primero
        lista = lista[1:]
    return(lista_nueva)

