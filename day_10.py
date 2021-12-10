from utils.file_reader import read_file_to_lines


def data_prep(instructions):
    data = instructions
    return data


def part_one(data):
    score = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    pairs = ["[]","()", "{}", "<>"]
    track = {
        "[": 0,
        "(": 0,
        "{": 0,
        "<": 0,
        "]": 0,
        ")": 0,
        "}": 0,
        ">": 0,
    }
    currently_open = list()
    wrong_end = None
    summary = 0
    for line in data:
        wrong_end = None
        for char in line:
            if wrong_end:
                break
            for open, close in pairs:
                if char == open:
                    currently_open.append(char)
                if char == close:
                    if currently_open[-1] != open:
                        wrong_end = char
                        break
                    else:
                        currently_open.pop( )
        if wrong_end:
            summary += score[wrong_end]

    return summary


def part_two(data):
    score = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    pairs = ["[]","()", "{}", "<>"]
    track = {
        "[": 0,
        "(": 0,
        "{": 0,
        "<": 0,
        "]": 0,
        ")": 0,
        "}": 0,
        ">": 0,
    }
    
    wrong_end = None
    scores = list()
    for line in data:
        currently_open = list()
        summary = 0
        wrong_end = None
        for char in line:
            if wrong_end:
                break
            for open, close in pairs:
                if char == open:
                    currently_open.append(char)
                if char == close:
                    if currently_open[-1] != open:
                        wrong_end = char
                        break
                    else:
                        currently_open.pop( )
        if wrong_end:
            continue
        # print(currently_open)
        currently_open.reverse()
        
        closing = list()
        for char in currently_open:
            for open, close in pairs:
                if char == open:
                    closing.append(close)
                    summary *= 5
                    summary += score[close]
                    break
        scores.append(summary)
    scores.sort()
    
    return scores[len(scores)//2]


def main():
    file_path = "inputs/day_10.txt"
    instructions = read_file_to_lines(file_path)
    data = data_prep(instructions)
    print(part_one(data))  # 491
    print(part_two(data))  # 1075536


if __name__ == "__main__":
    main()
