class Autor:
    def __init__(self,ID_autor,A_nombre,A_apellido,Biografia):
        #Atributos de la clase Autor y encapsulamiento
        self._ID_autor = ID_autor
        self.__A_nombre = A_nombre
        self.__A_apellido = A_apellido
        self.__Biografia = Biografia

        