from Autor import Autor
class Libro:
    def __init__(self,ISBN,Titulo,ID_autor,Año,N_copias):
        #Herencia simple de Autor
        super().__init__(self, ID_autor)
        #Atributos clase Libro y encapsulamiento
        self.__ISBN = ISBN
        self._Titulo = Titulo
        self._Año = Año
        self.__N_copias = N_copias
    