class Biblioteca:
    def __init__(self,B_nombre,B_direccion,Telefono):
        #Atributos de la clase Biblioteca
        self._B_nombre = B_nombre
        self._B_direccion = B_direccion
        self._Telefono = Telefono
        self.libros_disponibles = [
        "Cien años de soledad", 
        "Don Quijote de la Mancha", 
        "Crimen y castigo", 
        "1984", 
        "Matar a un ruiseñor", 
        "El gran Gatsby", 
        "La metamorfosis", 
        "El nombre de la rosa", 
        "Los miserables", 
        "El señor de los anillos"
        ] #libros disponibles (TITULOS)

        self.libros_prestados = ["La metamorfosis", 
        "Crimen y castigo"
        ] #libros prestados (TITULOS)

#Buscar libro
    def buscar_libro(self, titulo_libro):
        if titulo_libro in self.libros_disponibles: # se busca el titutlo del libro dentro de la lista de titulos disponibles
            return f"El libro '{titulo_libro}' está disponible" # en el caso que este disponible se muestra el mensaje a continuación
        elif titulo_libro in self.libros_prestados: #si el titulo esta prestado muestra el siguiente mensaje
            return f"El libro '{titulo_libro}' está prestado en este momento"
        else:
            return f"El titulo '{titulo_libro}' no esta disponible en Biblioteca" 
        """en el caso de que no este el titulo en libros disponibles 
            ni en prestados, el libro no esta en la bilbioteca"""
# Prestar libro      
    def prestar_libro(self, titulo_libro):
        if titulo_libro in self.libros_disponibles: # se busca el titutlo del libro dentro de la lista de titulos disponibles
            self.libros_disponibles.remove(titulo_libro) # se remueve el titulo del libro de la lista de disponibles
            self.libros_prestados.append(titulo_libro) # guarda el titulo del libro a prestar en la lista de prestados
            return f"Has prestado el libro '{titulo_libro}'."
        elif titulo_libro in self.libros_prestados: # revisa si el libro está en la lista de prestados
            return f"El libro '{titulo_libro}' ya está prestado." #cuyo caso si esta prestado muestra el mensaje
        else:
            return f"El libro '{titulo_libro}' no está disponible en la biblioteca." #en el caso contrario de las demas opciones muestra el mensaje "no esta disponible en esta biblioteca"
#Devolver libro
    def devolver_libro(self, titulo_libro):
        if titulo_libro in self.libros_prestados: #busca el titulo a devolver
            self.libros_prestados.remove(titulo_libro)#si el titulo está prestado lo remueve de libros prestados
            self.libros_disponibles.append(titulo_libro) #agrega el libro a devolver a libros disponisponibles
            return f"Has devuelto el libro '{titulo_libro}'." #mensaje deacuerdo a la accion
        else:
            return f"El libro '{titulo_libro}' no estaba prestado o no pertenece a esta biblioteca."#si el libro no esta prestado ni pertenece a esta biblioteca
        
