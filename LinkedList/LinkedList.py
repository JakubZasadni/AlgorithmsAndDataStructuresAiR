class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def remove(self):
        if self.head:
            self.head = self.head.next_node

    def remove_end(self):
        if not self.head or not self.head.next_node:
            self.head = None
        else:
            current = self.head
            prev = None
            while current.next_node:
                prev = current
                current = current.next_node
            prev.next_node = None

    def is_empty(self):
        return not self.head

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count

    def get(self):
        return self.head.data if self.head else None

    def destroy(self):
        self.head = None

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)


def main():
    universities_data = [
        ('AGH', 'Kraków', 1919),
        ('UJ', 'Kraków', 1364),
        ('PW', 'Warszawa', 1915),
        ('UW', 'Warszawa', 1915),
        ('UP', 'Poznań', 1919),
        ('PG', 'Gdańsk', 1945)
    ]

    uczelnie = LinkedList()

    for i in range(3):
        uczelnie.append(universities_data[i])
    for i in range(3, 6):
        uczelnie.add(universities_data[i])

    print(uczelnie)
    print(uczelnie.length())
    print()
    uczelnie.remove()
    print(uczelnie.get())
    print()
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.append(universities_data[0])
    uczelnie.remove_end()
    print(uczelnie)
    print(uczelnie.is_empty())


if __name__ == "__main__":
    main()
