def createGrid(r, c, at_prev_step):
    at_next_step = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            current_cell = at_prev_step[i][j]
            if current_cell == 'O':
                at_next_step[i][j] = '.'
                if i - 1 >= 0:
                    at_next_step[i - 1][j] = '.'
                if i + 1 <= r - 1:
                    at_next_step[i + 1][j] = '.'
                if j - 1 >= 0:
                    at_next_step[i][j - 1] = '.'
                if j + 1 <= c - 1:
                    at_next_step[i][j + 1] = '.'
    return at_next_step


def bomberMan(n, r, c, initial_grid):

    after_1_det = createGrid(r, c, initial_grid)

    if n % 2 == 0:
        return [['O'] * c for _ in range(r)]
    elif n < 4:
        return initial_grid if n == 1 else after_1_det
    else:
        after_2_det = createGrid(r, c, after_1_det)
        after_3_det = createGrid(r, c, after_2_det)
        return after_2_det if n % 4 == 1 else after_3_det


if __name__ == "__main__":
    r, c, n = input("row, column, n").strip().split(' ')
    r, c, n = [int(r), int(c), int(n)]
    grid = []
    for _ in range(r):
       grid.append(list(str(input("grid items").strip())))
    result = bomberMan(n, r, c, grid)
    for row in result:
        print("".join(row))