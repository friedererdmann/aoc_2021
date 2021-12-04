from utils.file_reader import read_file_to_lines


def data_prep(instructions):
    numbers = [int(x) for x in instructions[0].split(",")]
    boards = [[]]
    for line in instructions[1:]:
        if line:
            boards[len(boards)-1] += [int(x) for x in line.split()]
        else:
            boards.append([])
    return numbers, boards


def looping(instructions, early_out=False):
    numbers, boards = data_prep(instructions)
    scores = list()
    for number in numbers:
        for i, board in enumerate(boards):
            if number in board:
                x = board.index(number)
                modulo = x % 5
                board[x] = "x"
                row = board[x - modulo: x - modulo + 5].count("x") == 5
                column = [y for i, y in enumerate(board) if i % 5 == modulo].count("x") == 5
                if row or column:
                    scores.append(sum([z for z in board if isinstance(z, int)]) * number)
                    boards[i] = list()
                    if early_out:
                        return scores
    return scores

def part_one(instructions):
    return looping(instructions, True)[0]


def part_two(instructions):
    return looping(instructions)[-1]


def main():
    file_path = "inputs/day_04.txt"
    instructions = read_file_to_lines(file_path)
    print(part_one(instructions))  # 41503
    print(part_two(instructions))  # 3178


if __name__ == "__main__":
    main()
