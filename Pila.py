class nodoPila:
    def __init__(self, px,py):
        self.px = px
        self.py = py
        self.abajo = None

class pila:
    def __init__(self):
        self.primero = None
    
    def estaVacia(self):
        return True if self.primero == None else False

    def apilar(self,px,py):
        nuevoNodo = nodoPila(px,py)
        if(self.estaVacia()):
            self.primero = nuevoNodo
            print("inserto dato")
            return
        nuevoNodo.abajo = self.primero
        self.primero = nuevoNodo
        print("inserto dato")

    def desapilar(self):
        if(self.estaVacia()):
            print("La pila esta vacia")
            return
        self.primero = self.primero.abajo

    def mostrar(self):
        aux = self.primero
        if(self.estaVacia()):
            print("Lista vacia")
            return
        while(aux!= None):
            print("posicion en x"+str(aux.px)+"posicion en y"+str(aux.py))
            aux = aux.abajo

pilita = pila()
pilita.apilar(1,1)
pilita.apilar(1,2)
pilita.apilar(1,3)
pilita.apilar(1,4)

pilita.mostrar()

pilita.desapilar()
pilita.desapilar()
pilita.desapilar()
pilita.desapilar()
pilita.mostrar()

contenido = "hola"
ruta = 'C:\\Users\\Kevin Lam\\Desktop\\Estructuras de Datos\\Practica1\\pila.dot'
archivo = open(ruta,'w')
archivo.write(contenido)
archivo.close()            

            
        


