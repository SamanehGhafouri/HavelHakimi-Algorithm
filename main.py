from havel_hakimi_algorithm import hha

if __name__ == '__main__':

    print(hha(['A', 'B', 'C', 'D', 'E'], [4, 3, 2, 2, 1]))
    print(hha(None, [4, 4, 3, 2, 2, 2, 2, 1]))
    print(hha(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], [4, 4, 3, 2, 2, 2, 2, 1]))
    print(hha(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], [4, 3, 3, 2, 2, 2, 2, 1]))
    print(hha(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], [4, 4, 3, 3, 2, 2, 2, 2, 1]))
