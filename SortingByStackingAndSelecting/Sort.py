class PriorityQueue:
    def __init__(self, elements=None):
        self.tab = []
        self.heap_size = 0
        if elements:
            self.tab = elements
            self.heap_size = len(elements)
            self.build_max_heap()

    def is_empty(self):
        return self.heap_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[0]

    def dequeue(self):
        if self.is_empty():
            return None
        max_priority = self.tab[0]
        self.tab[0] = self.tab[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        return max_priority

    def enqueue(self, element):
        if self.heap_size < len(self.tab):
            self.tab[self.heap_size] = element
        else:
            self.tab.append(element)
        self.heap_size += 1
        self.build_max_heap()

    def left(self, idx):
        return 2 * idx + 1

    def right(self, idx):
        return 2 * idx + 2

    def parent(self, idx):
        return (idx - 1) // 2

    def max_heapify(self, idx):
        left_idx = self.left(idx)
        right_idx = self.right(idx)
        largest = idx
        if left_idx < self.heap_size and self.tab[left_idx] > self.tab[idx]:
            largest = left_idx
        if right_idx < self.heap_size and self.tab[right_idx] > self.tab[largest]:
            largest = right_idx
        if largest != idx:
            self.tab[idx], self.tab[largest] = self.tab[largest], self.tab[idx]
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self.max_heapify(i)

    def print_dict(self):
        print('{', end=' ')
        for i in range(self.heap_size):
            print(f'{self.tab[i]}', end=', ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.heap_size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


import random
import time

class Priority_Queue_Element:
    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    def __repr__(self):
        return f'{self.__priority} : {self.__data}'

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority


def shiftSort(lista):
    for i in range(len(lista)):
        swapID = i
        for j in range(i+1, len(lista)):
            if lista[swapID] > lista[j]:
                swapID = j
        lista.insert(i, lista.pop(swapID))
    return lista

def swapSort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


def main():
    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    lista1 = [Priority_Queue_Element(key, value) for key, value in data]

    queue = PriorityQueue(lista1)

    print("Kopiec jako tablica:")
    queue.print_dict()
    print("\nKopiec jako drzewo 2D:")
    queue.print_tree(0, 0)

    posortowane = []
    while not queue.is_empty():
        posortowane.append(queue.dequeue())
    print("\nPosortowana tablica (kopiec):", end=" ")
    print(*posortowane, sep=", ")

    lista2 = []
    for i in range(10000):
        lista2.append(random.randrange(0, 99))


    t_start = time.perf_counter()
    lista21 = PriorityQueue(lista2)
    while not lista21.is_empty():
        lista21.dequeue()
    t_stop = time.perf_counter()
    print("Czas obliczeń (sortowanie przez kopcowanie):", "{:.7f}".format(t_stop - t_start))

    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    print("\nSortowanie ShiftSort:", shiftSort(data))

    t_start = time.perf_counter()
    shiftSort(lista2.copy())
    t_stop = time.perf_counter()
    print("Czas obliczeń (sortowanie przez wybieranie - ShiftSort):", "{:.7f}".format(t_stop - t_start))

    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    print("\nSortowanie SwapSort:", swapSort(data))
    t_start = time.perf_counter()
    swapSort(lista2.copy())
    t_stop = time.perf_counter()
    print("Czas obliczeń (sortowanie przez wybieranie - SwapSort):", "{:.7f}".format(t_stop - t_start))


main()

