#filho esquerda 2i
#filho a direita 2i + 1
#pai j/2
import math

class HeapMin:
    def __init__(self):
        self.nos = 0
        self.heap = []
        
    def adiciona_no(self, u):
        self.heap.append(u)
        self.nos += 1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p-1] <= self.heap[f-1]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                f = p
    def mostra_heap(self):
        #print(self.heap)
        print("A estrutura heap é a seguinte:")
        nivel = int(math.log(self.nos, 2))
        a = 0
        for i in range(nivel):
            for j in range(2 ** i):
                print(f'{self.heap[a]}', end = "  ")
                a += 1
            print('')
        for i in range(self.nos-a):
            print(f"{self.heap[a]}", end = "  ")
            a += 1
        print("")
    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f+1 <= self.nos:
                if self.heap[f] < self.heap[f-1]:
                    f += 1
            if self.heap[p-1] <= self.heap[f-1]:
                break
            else:
                self.heap[f-1], self.heap[p-1] = self.heap[p-1], self.heap[f-1] 
                p = f
        return x
    
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]
        
    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso
        
    def mostra_matriz(self):
        print("A matriz de adjacencias é:")
        for i in range(self.vertices):
            print(self.grafo[i])
h = HeapMin()