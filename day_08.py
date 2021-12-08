import sys
from utils.file_reader import read_file_to_lines
from collections import Counter


def data_prep(instructions):
    data = [(a.split(), b.split()) for a, b in [x.split('|') for x in instructions]]
    return data


def part_one(data):
    # get the sum of "easy" digits (unique amount of LED segments) in all the input data
    return sum([1 for _, signals in data for led in signals if len(led) < 5 or len(led) == 7])


def part_two(data):
    y = 0
    digits = dict()
    summary = 0
    for wires, signals in data:
        wires.sort(key=len)
        one, seven, four = wires[:3]
        eight = wires[-1]
        a = [h for h in seven if h not in one][0]
        letters = [x for x in "".join([h for h in wires]).replace(a, "")]
        for k, v in Counter(letters).items():
            if v == 6:
                b = k
            if v == 4:
                e = k
            if v == 8:
                c = k
            if v == 9:
                f = k
        d = [h for h in four if h not in [b, c, f]][0]
        g = [h for h in eight if h not in [a, b, c, d, e, f]][0]
        digits[0] = [a,b,c,e,f,g]
        digits[1] = [c,f]
        digits[2] = [a,c,d,e,g]
        digits[3] = [a,c,d,f,g]
        digits[4] = [b,c,d,f]
        digits[5] = [a,b,d,f,g]
        digits[6] = [a,b,d,e,f,g]
        digits[7] = [a,c,f]
        digits[8] = [a,b,c,d,e,f,g]
        digits[9] = [a,b,c,d,f,g]
        n_str = ""
        for number in signals:
            for k, v in digits.items():
                if len(v) == len(number) and all(i in v for i in number):
                    n_str += str(k)
        summary += int(n_str)
    return summary


def main():
    file_path = "inputs/day_08.txt"
    instructions = read_file_to_lines(file_path)
    data = data_prep(instructions)
    print(part_one(data))  # 352
    print(part_two(data))  # 936117


if __name__ == "__main__":
    main()
