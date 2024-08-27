class TreeNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        return self.__search_recursive(self.root, key)

    def __search_recursive(self, node, key):
        if node is None or node.key == key:
            return node.data
        elif key < node.key:
            return self.__search_recursive(node.left, key)
        else:
            return self.__search_recursive(node.right, key)

    def insert(self, key, data):
        self.root = self.__insert_recursive(self.root, key, data)

    def __insert_recursive(self, node, key, data):
        if node is None:
            return TreeNode(key, data)
        if key < node.key:
            node.left = self.__insert_recursive(node.left, key, data)
        elif key > node.key:
            node.right = self.__insert_recursive(node.right, key, data)
        else: 
            node.data = data
        return node

    def delete(self, key):
        self.root = self.__delete_recursive(self.root, key)

    def __delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.__delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self.__delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self.__find_min(node.right)
                node.key = successor.key
                node.data = successor.data
                node.right = self.__delete_recursive(node.right, successor.key)
        return node

    def __find_min(self, node):
        while node.left:
            node = node.left
        return node

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node:
            self.__print_tree(node.right, lvl+5)
            print(lvl*" ", node.key, node.data)
            self.__print_tree(node.left, lvl+5)

    def height(self):
        return self.__height_recursive(self.root)

    def __height_recursive(self, node):
        if node is None:
            return 0
        else:
            left_height = self.__height_recursive(node.left)
            right_height = self.__height_recursive(node.right)
            return max(left_height, right_height) + 1

if __name__ == "__main__":
    bst = BinarySearchTree()

    elements = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for key, value in elements.items():
        bst.insert(key, value)

    bst.print_tree()

    sorted_elements = sorted(elements.items(), key=lambda x: x[0])
    print("Zawartość drzewa:")
    for key, value in sorted_elements:
        print(f"{key} {value},", end=" ")

    print("\nWartość dla klucza 24:", bst.search(24))
    bst.insert(20, "AA")
    bst.insert(6, "M")
    bst.delete(62)
    bst.insert(59, "N")
    bst.insert(100, "P")
    bst.delete(8)
    bst.delete(15)
    bst.insert(55, "R")
    bst.delete(50)
    bst.delete(5)
    bst.delete(24)
    print("Wysokość drzewa:", bst.height())
    print("Zawartość drzewa:")
    bst.print_tree()

