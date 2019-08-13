class nodoLista:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.siguiente = None
        self.anterior = None

class listaSimple:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def estaVacia(self):
        return True if self.primero == None else False

    def agregarInicio(self, x,y):
        nuevoNodo = nodoLista(x,y)
        if(self.estaVacia()):
            self.primero = nuevoNodo
            self.ultimo = self.primero
            return
        nuevoNodo.siguiente = self.primero
        self.primero.anterior = nuevoNodo
        self.primero = nuevoNodo
    
    def agregarFinal(self,x,y):
        nuevoNodo = nodoLista(x,y)
        if(self.estaVacia()):
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
        if(self.estaVacia()):
            print("lista doble vacia")
        else:
            aux = self.primero
            while(aux!= None):
                print("usuario"+str(aux.x)+"Punteo"+str(aux.y))
                
                aux = aux.siguiente
     
    def grafica(self):
        ruta = 'C:\\Users\\Kevin Lam\\Desktop\\Estructuras de Datos\\Practica1\\ListaDoble.dot'
        archivo = open(ruta,'w')
        archivo.write("digraph{\n")
        archivo.write("rankdir=LR;\n")
        archivo.write("labelloc=\"t\";\n")
        archivo.write("subgraph cluster_0{\n")
        archivo.write("style=filled;\n")
        archivo.write("color = lightgrey;\n")
        archivo.write("node[shape=record];\n")
        archivo.write(self.crearNodos())
        archivo.write(self.apuntadores(self.primero))
        archivo.close()            
                
    def crearNodos(self):
        aux = self.primero
        temporal = ""
        while(aux != None):
            temporal += "N"+str(aux.x)+"lam"+str(aux.y)+"[label=\"{ |("+str(aux.x)+","+str(aux.y)+") }\"style = filled, fillcolor = \"orange\"];\n"
            aux = aux.siguiente
        return temporal
    def apuntadores(self,aux):
      
        temporal = ""
        while(aux != None):
            temporal += "N"+str(aux.x)+"lam"+str(aux.y)+"->"+"N"+str(aux.siguiente.)+"lam"+str(aux.siguiente.y)+";\n"
            aux = aux.siguiente
        return temporal
                
            
lista = listaSimple()
lista.agregarInicio(10,57)
lista.agregarInicio(12,58)
lista.agregarInicio(13,59)
lista.agregarInicio(14,60)
print("-----")
lista.grafica()


            
   