from Libro import Libro #importe de class Libro
from Editorial import Editorial #importe de class Editorial
class Detalle_libro:
    def __init__(self,ISBN,Genero,Formato,N_pag, ID_editorial):
        #Herencia multiple
        Libro.__init__(self, ISBN)
        Editorial.__init__(self, ID_editorial)
        #Atributos clase Detalle_libro y encapsulamiento
        self.__Genero = Genero
        self.__Formato = Formato
        self.__N_pag = N_pag
        
        