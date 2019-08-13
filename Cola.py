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

    def agregar(self,nombre,punteo):
        nuevoNodo = nodoCola(nombre,punteo)
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
                    

colita = cola()
colita.agregar("krisha1",10)
colita.agregar("krisha2",10)
colita.agregar("krisha3",10)
colita.agregar("krisha4",10)
print("-------------------------")
colita.mostrar()
colita.eliminar()

colita.eliminar()

colita.eliminar()

colita.eliminar()
print("------------------------")
colita.mostrar()
colita.agregar("marcos",2)
colita.mostrar()



contenido = "
digraph D{
rankdir=LR;
labelloc="t";
subgraph cluster_0{
style=filled;
color = lightgrey;
node[shape=record];
Nodofunciono[label="{funciono,100| }"style = filled, fillcolor = "purple:blue"];
NodoNULL[label="NULL}"style = filled, fillcolor = "purple:blue"];
Nodofunciono->NodoNULL;
label = "Cola";
}
}
"
ruta = 'C:\\Users\\Kevin Lam\\Desktop\\Estructuras de Datos\\Practica1\\pila.dot'
archivo = open(ruta,'w')
archivo.write(contenido)
archivo.close()            
