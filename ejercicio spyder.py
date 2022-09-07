# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
numeros=[1,2,3,4,12,5,11,8,7,10]

arreglo=[20,"hola",3,"aleja",1,2,3,4]

letras=['A','B','C','D','E','b','e']

arregloslice=arreglo[1:-1]

letras.sort()

arregloextendido=numeros

arregloextendido.extend(letras)

print(letras)

letras.sort(key=str.lower)

letras

vocales=['A','E','I','O','U','a','e','i','o','u']

vocales.sort(key=str.lower)

vocales
