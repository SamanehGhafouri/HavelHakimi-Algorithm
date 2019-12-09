from havel_hakimi_algorithm import hha
from display_graph import display_graphic_graph


def main_ui_logic():

    # user initial prompt logic
    print("Enter the sequence of numbers please: ")
    user_input = input(">> ")

    # user sequence input processing
    sequence = [int(val) for val in user_input.split(',')]
    adjacency_lst, is_graphic = hha(None, sequence.copy())

    # user post prompt logic
    if is_graphic:
        print(f"The provided sequence is GRAPHIC!!! Yay.")
        display_graphic_graph(adjacency_lst)
    else:
        print(f"The degree sequence, {sequence}, is not graphic. :(")


if __name__ == '__main__':

    # print(hha(['A', 'B', 'C', 'D', 'E'], [4, 3, 2, 2, 1]))
    # print(hha(None, [4, 4, 3, 2, 2, 2, 2, 1]))
    # print(hha(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], [4, 4, 3, 2, 2, 2, 2, 1]))
    # print(hha(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], [4, 3, 3, 2, 2, 2, 2, 1]))
    # print(hha(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], [4, 4, 3, 3, 2, 2, 2, 2, 1]))
    # adjacency_lst, _ = hha(None, [4, 4, 3, 2, 2, 2, 2, 1])
    # display_graphic_graph(adjacency_lst)

    # print(hha(None, [2, 2, 2, 2, 2, 2, 2]))

    main_ui_logic()
