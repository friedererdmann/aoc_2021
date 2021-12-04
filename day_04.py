from utils.file_reader import read_file_to_lines


def data_prep(instructions):
    numbers = instructions[0].split(",")
    boards = list()
    board = list()
    for line in instructions[2:]:
        if line:
            board.append(line.strip().replace("  ", " ").split(" "))
        else:
            boards.append(board)
            board = list()
    boards.append(board)

    for board in boards:
        for line in board:
            print(line)
    return numbers, boards


def part_one(instructions):
    numbers, boards = data_prep(instructions)
    winner = None
    final = 0
    for number in numbers:
        if winner: break
        final = number
        for i, board in enumerate(boards):
            if winner: break
            for j, line in enumerate(board):
                if winner: break
                for k, entry in enumerate(line):
                    if winner: break
                    if entry == number:
                        # print(board, line, entry)
                        line[k] = "x"
                        board[j] = line
                        boards[i] = board
                        if line.count("x") == len(line):
                            winner = board
                        if [l[k] for l in board].count("x") == 5:
                            winner = board

    print(winner)
    summary = sum([sum([int(x) for x in line if x.isdigit()]) for line in winner])
    print(summary, int(final), summary*int(final))


def part_two(instructions):
    numbers, boards = data_prep(instructions)
    winner = None
    final = 0
    for number in numbers:
        if winner: break
        final = number
        for i, board in enumerate(boards):
            if winner: break
            for j, line in enumerate(board):
                if winner: break
                for k, entry in enumerate(line):
                    if winner: break
                    if entry == number:
                        # print(board, line, entry)
                        line[k] = "x"
                        board[j] = line
                        boards[i] = board
                        if line.count("x") == len(line) or [l[k] for l in board].count("x") == 5:
                            summary = sum([sum([int(x) for x in y if x.isdigit()]) for y in board])
                            print(summary, int(final), summary*int(final))
                            boards[i] = []


def main():
    file_path = "inputs/day_04.txt"
    instructions = read_file_to_lines(file_path)
    print(part_one(instructions))  # 4006064 # 198
    print(part_two(instructions))  # 5941884 # 230


if __name__ == "__main__":
    main()
