class Nodo():
    def __init__(self,usuario):
        self.usuario = usuario
        self.siguiente = None
        self.anterior = None

class ListaCircular():
    def __init__(self):
        primero = None
        ultimo = None
    
    def estaVacia():
        return True if primero.siguiente == None else False

    def agregarInicio(self, usuario):
        nuevoNodo = Nodo(usuario)
        if(self.estaVacia()):
            self.nuevoNodo.siguiente = nuevoNodo
            self.nuevoNodo.anterior = nuevoNodo
            self.primero = self.ultimo = nuevoNodo
            return
        nuevoNodo.anterior = self.ultimo
        nuevoNodo.siguiente = self.primero
        self.ultimo.siguiente = nuevoNodo
        self.primero.anterior = nuevoNodo
        self.primero = nuevoNodo

circular = ListaCircular()
circular.agregarInicio("kevin")
print("Se agrego el dato")

