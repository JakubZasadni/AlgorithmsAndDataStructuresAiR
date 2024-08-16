class PriorityQueue:
    def __init__(self):
        self.tab = []
        self.heap_size = 0

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


class PriorityElement:
    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    def __repr__(self):
        return f'{self.__priority} : {self.__data}'

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority


if __name__ == "__main__":
    kolejka = PriorityQueue()

    dane = "GRYMOTYLA"
    priorytety = [7, 5, 1, 2, 5, 3, 4, 8, 9]

    for data, priority in zip(dane, priorytety):
        element = PriorityElement(data, priority)
        kolejka.enqueue(element)

    print()
    kolejka.print_tree(0, 0)
    print()
    kolejka.print_dict()

    usuniety_element = kolejka.dequeue()
    print(usuniety_element)

    kolejny_element = kolejka.peek()
    print(kolejny_element)

    print()
    kolejka.print_dict()

    print(usuniety_element)

    print()
    while not kolejka.is_empty():
        usuniety_element = kolejka.dequeue()
        print(usuniety_element)

    print()
    kolejka.print_dict()
