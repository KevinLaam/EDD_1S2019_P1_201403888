class nodoLista:
    def __init__(self,nombre,score):
        self.nombre = nombre
        self.score = score
        self.siguiente = None
        self.anterior = None

class listaSimple:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def estaVacia():
        return True if self.primero == None else False

    def agregarInicio(self, nombre,score):
        nuevoNodo = nodoLista(nombre,score)
        if(self.estaVacia):
            self.primero = nuevoNodo
            self.ultimo = self.primero
            return
        nuevoNodo.siguiente = self.primero
        self.primero.anterior = nuevoNodo
        self.primero = nuevoNodo
    
    def agregarFinal(self,nombre,score)
        nuevoNodo = nodoLista(nombre,score)
        if(self.estaVacia())
            self.primero = nuevoNodo
            self.ultimo = self.primero
            return
        self.ultimo.siguiente = nuevoNodo
        nuevoNodo.anterior = self.ultimo
        self.ultimo = nuevoNodo


    def eliminarFinal(self):
        if(self.estaVacia()):
            print("Lista vacia")
        elif(self.ultimo == self.primero):
            self.primero = None
            self.ultimo = None
        else:   
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            
    def eliminarInicio(self):
        if(self.estaVacia()):
            print("Lista vacia")
        elif(self.ultimo == self.primero):
            self.primero = None
            self.ultimo = None
        else:   
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            
    def mostrar(self):
        
            
   