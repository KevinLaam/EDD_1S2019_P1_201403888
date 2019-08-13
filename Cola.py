class nodoCola:
    def __init__(self,nom,punteo):
        self.nom = nom
        self.punteo = punteo
        self.siguiente = None

class cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def estaVacia(self):
        return True if self.primero == None else False

    def agregar(self,nom,punteo):
        nuevoNodo = nodoCola(nom,punteo)
        if(self.estaVacia()):
            self.primero = nuevoNodo
            self.ultimo = self.primero
            return
        nuevoNodo.siguiente = self.ultimo
        self.ultimo = nuevoNodo

    def eliminar(self):
        if(self.estaVacia()):
            print("Cola vacia")
        elif(self.ultimo == self.primero):
            self.primero = None
            self.ultimo = None
        else:    
            aux = self.ultimo
            while(aux!= self.primero):
                if(aux.siguiente== self.primero):
                    aux.siguiente = None
                    self.primero = aux
                    return
                aux = aux.siguiente



    def mostrar(self):
        if(self.estaVacia()):
            print("Cola Vacia")
        else:
            aux = self.ultimo
            while(aux!= None):
                print("usuario"+aux.nom+"Punteo"+str(aux.punteo))
                aux = aux.siguiente
    
    def grafica(self):
        ruta = 'C:\\Users\\Kevin Lam\\Desktop\\Estructuras de Datos\\Practica1\\Cola.dot'
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
        aux = self.ultimo
        temporal = ""
        while(aux != None):
            temporal += "N"+aux.nom+"lam"+str(aux.punteo)+"[label=\"{ |("+aux.nom+","+str(aux.punteo)+") }\"style = filled, fillcolor = \"orange\"];\n"
            aux = aux.siguiente
        return temporal
    def apuntadores(self,aux):

        temporal = ""
        while(aux != None):
            #temporal += "N"+str(aux.x)+"lam"+str(aux.y)+"->"+"N"+str(aux.siguiente.)+"lam"+str(aux.siguiente.)+";\n"
            temporal += "N"+aux.nom+"lam"+str(aux.punteo)+"->"+"N"+aux.siguiente.nom+"lam"+str(aux.siguiente.punteo)+";\n"
            aux = aux.siguiente
        return temporal
                

colita = cola()
colita.agregar("krisha1",10)
colita.agregar("krisha2",10)
colita.agregar("krisha3",10)
colita.agregar("krisha4",10)
print("-------------------------")
colita.mostrar()
colita.grafica()



           
