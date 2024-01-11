# TASK: Problema celor 8 turnuri: să se scrie un program care plasează 8 turnuri pe tabla de șah, fără
# ca acestea să se atace reciproc.
# 8x8

import random

MAX = 8

# rezolvarea easy peasy - banala
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
def simple_place_rooks(n):
    return [(i, i) for i in range(n)]


def place_rooks_random_start(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Plasarea random a primului turn/nebun
    first_rook_row = random.randint(0, n - 1)
    first_rook_col = random.randint(0, n - 1)
    board[first_rook_row][first_rook_col] = 1

    placed_rooks = [(first_rook_row, first_rook_col)]

    l_board = range(n)

    for i in l_board:
        for j in l_board:
            # trecem peste pozitie:
            # 1. Pozitia este deja ocupata de un nebun/turn
            # 2. Daca se afla pe un rand si/sau coloana unde aria de attack este deja existenta
            if board[i][j] == 1 or any(i == r[0] or j == r[1] for r in placed_rooks):
                continue

            board[i][j] = 1 # daca este available pozitaa plasam pionul
            placed_rooks.append((i, j))

            break # no more room :)

    return placed_rooks


simple_placed_rooks = simple_place_rooks(MAX)
print("Simple Way: -> ", simple_placed_rooks)

random_start_solution = place_rooks_random_start(MAX)
print("Random Start Way: -> ", random_start_solution)
