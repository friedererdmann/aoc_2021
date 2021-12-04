from utils.file_reader import read_file_to_lines


def data_prep(instructions):
    numbers = [int(x) for x in instructions[0].split(",")]
    boards = [[]]
    for line in instructions[1:]:
        if line:
            boards[len(boards)-1].append([int(x) for x in line.split()])
        else:
            boards.append([])
    return numbers, boards


def looping(instructions, early_out=False):
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
                        if line.count("x") == len(line) or [l[k] for l in board].count("x") == len(line):
                            summary = sum([sum([x for x in y if isinstance(x, int)]) for y in board])
                            scores.append(summary*number)
                            if early_out:
                                return scores
                            boards[i] = list()
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
