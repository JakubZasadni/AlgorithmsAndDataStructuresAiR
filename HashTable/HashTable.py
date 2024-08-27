class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __str__(self):
        return f"{self.key}:{self.value}"

class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.table = [None for _ in range(size)]
        self.c1 = c1
        self.c2 = c2
    
    def hash_function(self, key):
        if isinstance(key, str):
            key = sum(ord(char) for char in key)
        return key % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        new_element = Element(key, value)
        for i in range(self.size):
            probe = (index + self.c1*i + self.c2*i*i) % self.size
            if self.table[probe] is None or self.table[probe].key == key:
                self.table[probe] = new_element
                return
        print("Brak miejsca")

    def search(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            probe = (index + self.c1*i + self.c2*i*i) % self.size
            if self.table[probe] is None:
                return None
            if self.table[probe].key == key:
                return self.table[probe].value
        return None

    def remove(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            probe = (index + self.c1*i + self.c2*i*i) % self.size
            if self.table[probe] is None:
                print("Brak danej")
                return
            if self.table[probe].key == key:
                self.table[probe] = None
                return

    def __str__(self):
        return "{" + ", ".join([str(self.table[i]) for i in range(self.size) if self.table[i] is not None]) + "}"

def test_hash_table_linear(size=13, c1=1, c2=0):
    h = HashTable(size, c1, c2)
    for i, letter in enumerate("ABCDEFGHIJKLM"):
        key = i + 1 if i + 1 < 6 else (18 if i == 5 else (31 if i == 6 else i + 1))
        h.insert(key, letter)
    
    print(h)
    
    print(h.search(5))
    print(h.search(14))
    
    h.insert(5, 'Z')
    print(h.search(5))
    
    h.remove(5)
    print(h)
    
    print(h.search(31))
    
    h.insert('test', 'W')
    print(h)

def test_hash_table_quadratic(size=13, c1=0, c2=1):
    h = HashTable(size, c1, c2)
    for i, letter in enumerate("ABCDEFGHIJKLM"):
        key = i + 1 if i + 1 < 6 else (18 if i == 5 else (31 if i == 6 else i + 1))
        h.insert(key, letter)
    print(h)

def test_multiples_of_13_linear(size=13, c1=1, c2=0):
    h = HashTable(size, c1, c2)
    for i, letter in enumerate("ABCDEFGHIJKLM"):
        h.insert(13*(i+1), letter)
    print(h)

def test_multiples_of_13_quadratic(size=13, c1=0, c2=1):
    h = HashTable(size, c1, c2)
    for i, letter in enumerate("ABCDEFGHIJKLM"):
        h.insert(13*(i+1), letter)
    print(h)

def main():

    test_hash_table_linear()
    test_hash_table_quadratic()
    test_multiples_of_13_linear()
    test_multiples_of_13_quadratic()

if __name__ == "__main__":
    main()


    
