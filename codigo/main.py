import copy
import random

class no:
    def __init__(self, estado):
        self.estado = estado
        self.filho = []

    def movimento(self):
        for i in range(3):
            for j in range(3):
                if i != j:
                    if self.estado[i]:
                        temp = copy.deepcopy(self.estado)
                        valor = temp[i].pop()
                        temp[j].append(valor)

                        if temp not in self.filho:
                            self.filho.append(no(temp))

    def bfs(self, objetivo, fila):
        if self.estado == objetivo:  # Estado final atingido 
            print("Cheguemo no objetivo meu patrão")    # UX 
            return True

        for atual in self.filho:
            if atual.estado not in fila:
                print("SUCESSO", atual.estado)
                atual.movimento()
                temp = copy.deepcopy(atual.estado)
                fila.append(temp)
                resultado = atual.bfs(objetivo, fila)

                if resultado:
                    return resultado

                return self.bfs(objetivo, fila)

        print("FALHA")
        return False

valores = [[['A'], ['B'], ['C']], [['A', 'B'], ['C'], []], [['A', 'C'],
            ['B'], []], [['B', 'C'], ['A'], []], [['A', 'B', 'C'], [], []]]

inicio = random.choice(valores)

random.shuffle(inicio)

for i in inicio:
    random.shuffle(i)

print("Estado inicial", inicio)

# Inicializando o Grafo
raiz = no(inicio)
raiz.movimento()

objetivo = [[], ['C', 'B', 'A'], []]    # Onde queremos chegar

fila = []

raiz.bfs(objetivo, fila)