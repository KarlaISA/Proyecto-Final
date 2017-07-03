#Proyecto Final
#Karla Ivonne Serrano Arevalo
#Luis Carlos Castro

#aqui inicializamos las variables nombre y etiqueta
class Imagen:
    def __init__(self,nombre, etiqueta):
        self.nombre = nombre 
        self.etiqueta = etiqueta
    
    def setNombre(self, nombre):
        self.nombre = nombre 
        
    def getNombre(self):
        return self.nombre
    
    def setEtiqueta(self, etiqueta):
        self.etiqueta = etiqueta
       
    def mostrar_imagen(self):
       return Imagen


#Para comprobar si hay algina carpeta dentro de las carpetas y siga buscando:
def comprobar_carpeta(path_carpeta):
  path_carpetas = []
  path_carpetas.append(path_carpeta)
  elementos_carpeta = os.listdir(path_carpeta)
  for i in elementos_carpeta:
    if os.path.isdir(path_carpeta+"/"+i)==True:
        path_carpetas.append(path_carpeta+"/"+i)
  return path_carpeta

def nom_files(path_carpeta):
    nom_img_temp = os.listdir(path_carpeta)
    nom_img = []
    for i in nom_img_temp:
        if os.path.isdir(path_carpeta + "/"+i)==False:
            nom_img.append(i)
    return nom_img

def crear_ob_img(nom_img,path_carpeta):
    num = 1
    ob_img = []
    for i in nom_img:
        imagen = Imagen()
        imagen.nom = i
        imagen.ruta = path_carpeta + '/' + i
        imagen.num = num
        ob_img.append(imagen)
        num = num + 1
    return ob_img


def tag(numID,tag,ob_img):
    if tag != '':
        for i in ob_img:
            if i.num == numID:
                i.tags.append(tag)

#aqui es la interfaz del programa
from Tkinter import *
import Image, ImageTk, os

class directorio:
 def __init__(self, master=None):
   self.master = master
   self.frame = Frame(master, width=400, height=450, bg='blue50',
     relief=RAISED, bd=4)

   self.lbl = Label(self.frame)
   self.lbl.place(relx=0.5, rely=0.48, anchor=CENTER)
   
   self.images = []
   images = os.listdir("images")

   xpos = 0.05
   for i in range(10):
     Button(self.frame, text='%d'%(i+1), bg='gray10',
     fg='white', command=lambda s=self, img=i: \
     s.getImg(img)).place(relx=xpos, rely=0.99, anchor=S)
     xpos = xpos + 0.08
     self.images.append(images[i])

   Button(self.frame, text='Done', command=self.exit,
     bg='red', fg='yellow').place(relx=0.99, rely=0.99, anchor=SE)
   self.frame.pack()
   self.getImg(0)

 def getImg(self, img):
   self.masterImg = Image.open(os.path.join("images",
   		self.images[img]))
   self.masterImg.thumbnail((400, 400))
   self.img = ImageTk.PhotoImage(self.masterImg)
   self.lbl['image'] = self.img

 def exit(self):
   self.master.destroy()

root = Tk()
root.title('Album de Imagenes')
scrapbook = directorio(root)
root.mainloop()
