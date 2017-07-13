# -*- coding: utf-8 -*-

import os

nombres_imagenes = os.listdir("images")
f = open ("datos.dat", "w")
for nombre in nombres_imagenes:
	f.write(nombre+"|\n")
f.write("_")
f.close()