class Nodo():
    def __init__(self,usuario):
        self.usuario = usuario
        self.siguiente = None
        self.anterior = None

class ListaCircular():
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def estaVacia(self):
        return True if self.primero == None else False

    def agregarInicio(self, usuario):
        nuevoNodo = Nodo(usuario)
        if(self.estaVacia()):
            self.primero = self.ultimo = nuevoNodo
            return
        nuevoNodo.anterior = self.ultimo
        nuevoNodo.siguiente = self.primero
        self.ultimo.siguiente = nuevoNodo
        self.primero.anterior = nuevoNodo
        self.primero = nuevoNodo
    
    def agregarFinal(self,usuario):
        nuevoNodo = Nodo(usuario)
        if(self.estaVacia()):
            nuevoNodo.siguiente = nuevoNodo
            nuevoNodo.anterior = nuevoNodo
            self.primero = self.ultimo = nuevoNodo
            return
        nuevoNodo.anterior = self.ultimo
        nuevoNodo.siguiente = self.primero
        self.ultimo.siguiente = nuevoNodo
        self.primero.anterior = nuevoNodo
        self.ultimo = nuevoNodo
    
    
    
    def mostrar(self):
        if(self.estaVacia()):
            print("lista circular doble vacia")
        else:
            aux = self.primero
            while(aux.siguiente != self.primero):
                print("usuario"+str(aux.usuario))
                aux = aux.siguiente

circular = ListaCircular()
circular.agregarInicio("kevin")
print("Se agrego el dato")
circular.mostrar()
