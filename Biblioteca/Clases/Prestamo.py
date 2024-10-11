from Usuario import Usuario
from Libro import Libro
class Prestamo:
    def __init__(self,ISBN,Fecha_p,Fecha_e,Fecha_d,N_usuario,Estado_po):
        #Herencia Multiple(class Usuario y class Libro)
        Usuario.__init__(self, N_usuario, Estado_po)
        Libro.__init__(self, ISBN)
        #atributos clase Prestamo y encapsulamiento
        self.__Fecha_p = Fecha_p
        self.__Fecha_e = Fecha_e
        self.__Fecha_d = Fecha_d

        


        