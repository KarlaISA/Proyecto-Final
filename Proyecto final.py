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


#Comprobamos si carpetas dentro de la carpeta:
def comprobar_carpeta(path_carpeta):
  path_carpetas = []
  path_carpetas.append(path_carpeta)
  elementos_carpeta = os.listdir(path_carpeta)
  for i in elementos_carpeta:
    if os.path.isdir(path_carpeta+"/"+i)==True:
        path_carpetas.append(path_carpeta+"/"+i)
  return path_carpeta


#
def nom_files(path_carpeta):
    nom_img_temp = os.listdir(path_carpeta)
    nom_img = []
    for i in nom_img_temp:
        if os.path.isdir(path_carpeta + "/"+i)==False:
            nom_img.append(i)
    return nom_img
