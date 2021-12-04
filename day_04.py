from utils.file_reader import read_file_to_lines


def data_prep(instructions):
    numbers = [int(x) for x in instructions[0].split(",")]
    boards = list()
    board = list()
    for line in instructions[1:]:
        if line:
            board.append([int(x) for x in line.split()])
        else:
            if board:
                boards.append(board)
                board = list()
    if board:
        boards.append(board)

    return numbers, boards


def looping(instructions):
    numbers, boards = data_prep(instructions)
    scores = list()
    for number in numbers:
        for i, board in enumerate(boards):
            for j, line in enumerate(board):
                for k, entry in enumerate(line):
                    if entry == number:
                        line[k] = "x"
                        board[j] = line
                        boards[i] = board
                        if line.count("x") == len(line) or [l[k] for l in board].count("x") == 5:
                            summary = sum([sum([x for x in y if isinstance(x, int)]) for y in board])
                            scores.append(summary*number)
                            boards[i] = []
    return scores


def part_one(instructions):
    return looping(instructions)[0]


def part_two(instructions):
    return looping(instructions)[-1]


def main():
    file_path = "inputs/day_04.txt"
    instructions = read_file_to_lines(file_path)
    print(part_one(instructions))  # 41503
    print(part_two(instructions))  # 3178


if __name__ == "__main__":
    main()
