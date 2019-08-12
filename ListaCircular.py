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

    def agregar(self, usuario):
        nuevoNodo = Nodo(usuario)
        if(self.estaVacia()):
            self.primero = self.ultimo = nuevoNodo
            self.primero.siguiente = self.primero
            self.primero.anterior = self.ultimo
            print("Se agrego dato1")
            return
        self.ultimo.siguiente = nuevoNodo
        nuevoNodo.anterior = self.ultimo
        nuevoNodo.siguiente = self.primero
        self.ultimo = nuevoNodo
        self.primero.anterior = self.ultimo
        print("Se agrego dato2")
    
    def eliminar(self):
        
    
   
    
    
    
    def mostrar(self):
        aux = self.primero
        if(self.estaVacia() == False):
            while(True):
                print("usuario"+str(aux.usuario))
                aux = aux.siguiente
                if(aux == self.primero):
                    break
        else:
            print("LIsta circular Vacia")

circular = ListaCircular()
circular.agregar("kevin")
circular.agregar("kevin2")
circular.mostrar()