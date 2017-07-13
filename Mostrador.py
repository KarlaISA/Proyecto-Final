# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image,ImageTk

indice=0

class Imagen:
	def __init__ (self,nombre):
		self.nombre=nombre
		self.etiquetas=[]
		self.oculto=False
	def agrega_etiqueta(self,etiqueta):
		self.append(etiqueta)

class Mostrador:
	def __init__ (self):
		self.ventana = Tk()
		self.ventana.title("Mostrador")
		self.ventana.config(bg="black")
		self.ventana.geometry("1100x750")
		
		carga_imagen(self)
		
		carga_etiquetas(self)
		
		self.atras=Button(self.ventana,text="<",relief=FLAT,command=self.cambia_imagen_atras)
		self.atras.grid(row=0,column=0)
		self.adelante=Button(self.ventana,text=">",relief=FLAT,command=self.cambia_imagen_adelante)
		self.adelante.grid(row=0,column=1)
		
		self.cuadro_buscar = Entry(self.ventana)
		self.cuadro_buscar.grid(row=0,column=2)
		self.accion_buscar=Button(self.ventana,text="Buscar",command=self.filtrar)
		self.accion_buscar.grid(row=0,column=3)
		
		self.cuadro_etiquetas = Entry(self.ventana)
		self.cuadro_etiquetas.grid(row=2,column=0)
		self.accion_etiquetar=Button(self.ventana,text="Agregar",command=self.etiqueta_imagen)
		self.accion_etiquetar.grid(row=2,column=1)
		self.accion_guardar=Button(self.ventana,text="Guardar",command=self.guardar_cambios)
		self.accion_guardar.grid(row=2,column=2)
		
		self.ventana.mainloop()
	
	def cambia_imagen_atras(self):
		global indice
		indice=indice-1
		if indice<0:
			indice=len(imagenes)-1
		while imagenes[indice].oculto:
			indice=indice-1
			if indice<0:
				indice=len(imagenes)-1
		
		carga_imagen(self)
		
		carga_etiquetas(self)
		
	def cambia_imagen_adelante(self):
		global indice
		indice=indice+1
		if indice>=len(imagenes):
			indice=0
		while imagenes[indice].oculto:
			indice=indice+1
			if indice>=len(imagenes):
				indice=0
		carga_imagen(self)
		carga_etiquetas(self)

	def etiqueta_imagen(self):
		imagenes[indice].etiquetas.append( self.cuadro_etiquetas.get() )
		self.cuadro_etiquetas.delete(0,END)
	
	def guardar_cambios(self):
		file = open("datos.dat","w")
		for imagen in imagenes:
			file.write(imagen.nombre+"|")
			for etiqueta in imagen.etiquetas:
				file.write(etiqueta+",")
			file.write("\n")
	
	def filtrar(self):
		flag=False
		etiqueta_buscada=self.cuadro_buscar.get()
		for imagen in imagenes:
			if esta_en_etiquetas(etiqueta_buscada,imagen):
				imagen.oculto=False
				flag=True
			else:
				imagen.oculto=True
		if flag!=True:
			for imagen in imagenes:
				imagen.oculto=False
			ventana_emergente("No hubó resultados!")
		else:
			global indice
			indice=0
			while imagenes[indice].oculto:
				indice+=1
			print indice
			carga_imagen(self)
			carga_etiquetas(self)	
			
def ventana_emergente(msj):
	emer=Tk()
	contenido_lista_etiquetas=""
	mensaje=Label(emer,text=msj,width=20,height=10,justify="left")
	mensaje.grid(row=0,column=0)
	
	
	emer.mainloop()
	
def carga_etiquetas(mostrador):
	contenido_lista_etiquetas=""
	for etiqueta in imagenes[indice].etiquetas:
		contenido_lista_etiquetas=contenido_lista_etiquetas+etiqueta+"\n"
	mostrador.lista_etiquetas=Label(mostrador.ventana,text=contenido_lista_etiquetas,width=20,height=30,justify="left")
	mostrador.lista_etiquetas.grid(row=1,column=4)

def carga_imagen(mostrador):
	imagen = Image.open("images/"+imagenes[indice].nombre)
	imagen = imagen.resize((900, 650), Image.ANTIALIAS)
	tk_imagen = ImageTk.PhotoImage(imagen)
	mostrador.marco_imagen = Label(mostrador.ventana,image = tk_imagen)
	mostrador.marco_imagen.image=tk_imagen
	mostrador.marco_imagen.grid(row=1,column=0,columnspan=4)	

def esta_en_etiquetas(texto,imagen):
	for etiqueta in imagen.etiquetas:
		if texto==etiqueta:
			return True
	return False
#MAIN -------------------------------------------------
#nombres_imagenes = os.listdir("images")
imagenes=[]
file = open("datos.dat")
for line in file:
	if line!="_":
		info=line.split('|')
		imagen=Imagen(info[0])
		etiquetas=info[1].split(',')
		for etiqueta in etiquetas:
			if etiqueta!="\n":
				imagen.etiquetas.append(etiqueta)
		imagenes.append(imagen)

mostr=Mostrador()
