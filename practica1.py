class Ejercicio1:
    def __init__(self, a,b):
        self.a = a
        self.b  = b

    def printStar(self):
        #Ejericicio 1
        n = ""
        for i in range(self.a,self.b):
            for j in range(1,i):
                n += "*"
            print(n)
            n = ""

class Ejercicio2:
    def __init__(self, numeros_lista):
        self.numeros_lista = numeros_lista
    
    def ordenarLista(self):
        lista_ordenada = sorted(self.numeros_lista)
        print(lista_ordenada)

    def obtenerPares(self):
        lista_pares = []
        for h in self.numeros_lista:
            if h%2 == 0:
                lista_pares.append(h)
        print(lista_pares)

    def obtenerImpares(self):
        lista_inpares = []
        for i in self.numeros_lista:
            if i%2 != 0:
                lista_inpares.append(i)
        print(lista_inpares)

    def obtenerRepetidos(self):
        dict_repetidos = {}
        for i in self.numeros_lista:
            if not dict_repetidos:
                dict_repetidos[i]=1
            elif not i in dict_repetidos:
                dict_repetidos[i] = 1
            else:
                n = int(dict_repetidos[i])
                dict_repetidos[i] = n+1
        print(dict_repetidos)


if __name__ =="__main__":
    ejercicio1 = Ejercicio1(1,7)
    ejercicio1.printStar()

    lista = [1,2,1,3,2,1,7,3,2,10]
    ejercicio2 = Ejercicio2(lista)
    ejercicio2.ordenarLista()
    ejercicio2.obtenerPares()
    ejercicio2.obtenerImpares()
    ejercicio2.obtenerRepetidos()

    