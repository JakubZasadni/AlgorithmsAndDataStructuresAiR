class Macierz:
    def __init__(self, arg, fill_value=0):
        if isinstance(arg, tuple):
            self.rows, self.cols = arg
            self.data = [[fill_value] * self.cols for _ in range(self.rows)]
        else:
            self.data = arg
            self.rows, self.cols = len(arg), len(arg[0])

    def __add__(self, other):
        if self.size() != other.size():
            raise ValueError("Wymiary macierzy musza sie zgadzac")
        return Macierz([[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)])

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Liczba kolumn musi być równa liczbie wierszy")
        result = [[sum(x * y for x, y in zip(row, col)) for col in zip(*other.data)] for row in self.data]
        return Macierz(result)

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        return "\n".join("| " + "   ".join(map(str, row)) + " |" for row in self.data)

    def size(self):
        return self.rows, self.cols


def transpose(matrix):
    return Macierz(list(map(list, zip(*matrix))))


if __name__ == "__main__":
    m1 = Macierz([[1, 0, 2], [-1, 3, 1]])
    print(m1, '\n')

    transposed_matrix = transpose(m1)
    print(transposed_matrix, '\n')

    m2 = Macierz((2, 3), fill_value=1)
    print(m2)

    sum_matrix = m1 + m2
    print(sum_matrix, '\n')

    m3 = Macierz([[3, 1], [2, 1], [1, 0]])
    product_matrix = m1 * m3
    print(product_matrix)
