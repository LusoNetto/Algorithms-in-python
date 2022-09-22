#filho esquerda 2i
#filho a direita 2i + 1
#pai j/2
import math

class HeapMax:
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
            if self.heap[p-1] >= self.heap[f-1]: # <= HeapMin
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
                if self.heap[f] > self.heap[f-1]: # < se HeapMin
                    f += 1
            if self.heap[p-1] >= self.heap[f-1]:
                break
            else:
                self.heap[f-1], self.heap[p-1] = self.heap[p-1], self.heap[f-1] 
                p = f
        return x
    def tamanho(self):
        return self.nos
    def maiorElemento(self):
        if self.nos != 0:
            return self.heap[0]
        return "A arvore esta vazia"
    def filhoEsquerda(self, i):
        if self.nos >= 2*i:
            return self.heap[2*i-1]
        return "Esse nó não tem filho"
    def filhoDireita(self, i):
        if self.nos >= 2*i+1:
            return self.heap[2*i]
        return "Esse nó não tem filho a direita!"
    def pai(self, i):
        return self.heap(i//2)
h = HeapMax()

h.adiciona_no(17)
h.adiciona_no(36)
h.adiciona_no(25)
h.adiciona_no(7)
h.adiciona_no(3)
h.adiciona_no(100)
h.adiciona_no(1)
h.adiciona_no(2)
h.adiciona_no(19)

h.mostra_heap()

elementoMax = h.remove_no()
print(f"O elemento maximo é {elementoMax}")

h.mostra_heap()

print(f"Tamanho: {h.tamanho()}")
print(f"Filho a esquerda de 25: {h.filhoEsquerda(4)}")
print(f"Filho a direita de 25: {h.filhoDireita(4)}")