ALPHABET = 'abcdefghijklmnopqrstuvwx '

def main():
    table = make_matrix(5, 5)

    print(f'Matrix: {table}')

    acc = 0
    for x in range(5):
        for y in range(5):
            table[x][y] = ALPHABET[acc]
            acc += 1

    print(table)
    
    """
    fill_matrix(table, ALPHABET)

    print(f'Filled matrix: {table}')
    """


def make_matrix(x, y):
    matrix = [[' '] * x for _ in range(y)]
    return matrix

"""
def fill_matrix(matrix, filler):
    acc = 0

    for x in range(len(matrix[x])):
        for y in range(len(matrix[y])):
            matrix[x][y] = filler[acc]

    return matrix
"""
main()



















