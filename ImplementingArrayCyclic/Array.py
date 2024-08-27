class Queue:
    def __init__(self):
        self.size = 5
        self.tab = [None] * self.size
        self.read_index = 0
        self.write_index = 0

    def is_empty(self):
        return self.read_index == self.write_index

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[self.read_index]

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.tab[self.read_index]
        self.tab[self.read_index] = None
        self.read_index = (self.read_index + 1) % self.size
        return data

    def enqueue(self, data):
        next_write_index = (self.write_index + 1) % self.size
        if next_write_index == self.read_index:
            new_size = self.size * 2
            new_tab = [None] * new_size
            for i in range(self.size - 1):  
                new_tab[i] = self.tab[(self.read_index + i) % self.size]
            self.read_index = 0  
            self.write_index = self.size - 1  
            self.size = new_size  
            self.tab = new_tab  
            
        self.tab[self.write_index] = data
        self.write_index = (self.write_index + 1) % self.size

    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        i = self.read_index
        while i != self.write_index:
            items.append(self.tab[i])
            i = (i + 1) % self.size
        return str(items)

    def print_tab(self):
        print(self.tab)


def main():
    
    queue = Queue()
    for i in range(1, 5):
        queue.enqueue(i)
    print(queue.dequeue())  
    print(queue.peek())     
    print(queue)          
    for i in range(5, 9):
        queue.enqueue(i)
    queue.print_tab()      
    while not queue.is_empty():
        print(queue.dequeue(), end=' ')  
    print('\n',queue)

if __name__ == "__main__":
    main()
