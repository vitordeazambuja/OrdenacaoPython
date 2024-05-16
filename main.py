import random
import time
import matplotlib.pyplot as plt

# Sorts
# Quick Sort
def particiona(V, inicio, final):
    # Aleatoriza o pivo para nao ser chamado varias vezes e estourar a pilha
    pivo_indice = random.randint(inicio,final)
    V[inicio],  V[pivo_indice] = V[pivo_indice], V[inicio]
    # Restante da lógica
    esq = inicio + 1
    dir = final
    pivo = V[inicio]
    while esq <= dir:
        while esq <= final and V[esq] <= pivo:
            esq = esq + 1
        while dir >= inicio and V[dir] > pivo:
            dir = dir - 1
        if esq <= dir:
            V[esq], V[dir] = V[dir], V[esq]
            esq = esq + 1
            dir = dir - 1
    V[inicio], V[dir] = V[dir], V[inicio]
    return dir

def quickSort(V,inicio,fim):
    if fim > inicio:
        pivo = particiona(V,inicio,fim)
        quickSort(V, inicio, pivo - 1)
        quickSort(V, pivo + 1, fim)
    return V

# Merge Sort
def merge(V,inicio,meio,fim):
    t = fim - inicio + 1
    p1 = inicio
    p2 = meio + 1
    fim1 = False
    fim2 = False
    temp = [0 for i in range(t)]
    for i in range(t):
        if(not fim1 and not fim2):
            if(V[p1] < V[p2]):
                temp[i] = V[p1]
                p1 = p1 + 1
            else:
                temp[i] = V[p2]
                p2 = p2 + 1
            if(p1 > meio):
                fim1 = True
            if(p2 > fim):
                fim2 = True
        else:
            if(not fim1):
                temp[i] = V[p1]
                p1 = p1 + 1
            else:
                temp[i] = V[p2]
                p2 = p2 + 1
    k = inicio
    for j in range(t):
        V[k] = temp[j]
        k = k + 1

def mergeSort(V, inicio, fim):
    if (inicio < fim):
        meio = int((inicio + fim)/2)
        mergeSort(V, inicio, meio)
        mergeSort(V, meio + 1, fim)
        merge(V, inicio, meio, fim)
    return V

# Shell Sort
def shellSort(nums):
    h = 1
    n = len(nums)
    
    while h < n / 3:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            c = nums[i]
            j = i
            while j >= h and c < nums[j - h]:
                nums[j] = nums[j - h]
                j = j - h
            nums[j] = c
        h = int(h / 2.2)
    return nums

# Definição dos tamanhos e da array de ordens
tamanhos = [100, 1000, 10000]
ordens = ["cresc", "decresc", "random"]

# Tempos do Quick Sort
temposCrescQuick = []
temposDecrescQuick = []
temposRandomQuick = []

# Tempos do Merge Sort
temposCrescMerge = []
temposDecrescMerge = []
temposRandomMerge = []

# Tempos do Shell Sort
temposCrescShell = []
temposDecrescShell = []
temposRandomShell = []


# Funções de medir o tempo
def medirTempoQuick(array):
    tempo_inicial = time.time()
    ordenado = quickSort(array, 0, len(array)-1)
    tempo_final = time.time()
    return tempo_final - tempo_inicial

def medirTempoMerge(array):
    tempo_inicial = time.time()
    ordenado = mergeSort(array, 0, len(array)-1)
    tempo_final = time.time()
    return tempo_final - tempo_inicial

def medirTempoShell(array):
    tempo_inicial = time.time()
    ordenado = shellSort(array)
    tempo_final = time.time()
    return tempo_final - tempo_inicial

# for
for tamanho in tamanhos:
    # Criação das ordens dentro do for
    array_cresc = list(range(tamanho))
    array_decresc = list(range(tamanho,0,-1))
    array_random = random.sample(range(tamanho*10),tamanho)
    # Medição de tempo do quick sort
    tempo_quick_cresc = medirTempoQuick(array_cresc)
    tempo_quick_decresc = medirTempoQuick(array_decresc)
    tempo_quick_random = medirTempoQuick(array_random)
    # Append na array de tempos do quick sort
    temposCrescQuick.append(tempo_quick_cresc)
    temposDecrescQuick.append(tempo_quick_decresc)
    temposRandomQuick.append(tempo_quick_random)
    # Medição de tempo do merge sort
    tempo_merge_cresc = medirTempoMerge(array_cresc)
    tempo_merge_decresc = medirTempoMerge(array_decresc)
    tempo_merge_random = medirTempoMerge(array_random)
    # Append na array de tempos do merge sort
    temposCrescMerge.append(tempo_merge_cresc)
    temposDecrescMerge.append(tempo_merge_decresc)
    temposRandomMerge.append(tempo_merge_random)
    # Medição de tempo do shell sort
    tempo_shell_cresc = medirTempoShell(array_cresc)
    tempo_shell_decresc = medirTempoShell(array_decresc)
    tempo_shell_random = medirTempoShell(array_random)
    # Append na array de tempos do shell sort
    temposCrescShell.append(tempo_shell_cresc)
    temposDecrescShell.append(tempo_shell_decresc)
    temposRandomShell.append(tempo_shell_random)

# Plotando gráficos para cada condição
fig, axs = plt.subplots(3, figsize=(10, 18))

# Plotando gráfico para a condição crescente
axs[0].plot(tamanhos, temposCrescQuick, marker='o', label='Quick Sort')
axs[0].plot(tamanhos, temposCrescMerge, marker='o', label='Merge Sort')
axs[0].plot(tamanhos, temposCrescShell, marker='o', label='Shell Sort')
axs[0].set_title('Desempenho - Ordem Crescente')
axs[0].set_xlabel('Tamanho do Array')
axs[0].set_ylabel('Tempo (s)')
axs[0].legend()
axs[0].grid(True)

# Plotando gráfico para a condição decrescente
axs[1].plot(tamanhos, temposDecrescQuick, marker='o', label='Quick Sort')
axs[1].plot(tamanhos, temposDecrescMerge, marker='o', label='Merge Sort')
axs[1].plot(tamanhos, temposDecrescShell, marker='o', label='Shell Sort')
axs[1].set_title('Desempenho - Ordem Decrescente')
axs[1].set_xlabel('Tamanho do Array')
axs[1].set_ylabel('Tempo (s)')
axs[1].legend()
axs[1].grid(True)

# Plotando gráfico para a condição aleatória
axs[2].plot(tamanhos, temposRandomQuick, marker='o', label='Quick Sort')
axs[2].plot(tamanhos, temposRandomMerge, marker='o', label='Merge Sort')
axs[2].plot(tamanhos, temposRandomShell, marker='o', label='Shell Sort')
axs[2].set_title('Desempenho - Ordem Aleatória')
axs[2].set_xlabel('Tamanho do Array')
axs[2].set_ylabel('Tempo (s)')
axs[2].legend()
axs[2].grid(True)

plt.subplots_adjust(top=0.95, bottom=0.1, left=0.1, right=0.95, hspace=0.5, wspace=0.5)
plt.show()