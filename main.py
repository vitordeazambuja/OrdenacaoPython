import random
import time

# Sorts
# Quick Sort
def particiona(V,inicio,final):
    esq = inicio + 1
    dir = final
    pivo = V[inicio]
    while(esq < dir):
        while(esq <= final and V[esq] <= pivo):
            esq = esq + 1
        while(dir >= 0 and V[dir] > pivo):
            dir = dir - 1
        if(esq <= dir):
            aux = V[esq]
            V[esq] = V[dir]
            V[dir] = aux
    V[inicio] = V[dir]
    V[dir] = pivo
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

# Definição dos tamanhos
tamanhos = [100, 1000, 10000]

# for
for tamanho in tamanhos:
    # Criação das ordens dentro do for
    array_cresc = list(range(tamanho))
    array_decresc = list(range(tamanho,0,-1))
    array_random = random.sample(range(tamanho*10),tamanho)