import sys
from utils.file_reader import read_file_to_lines
from collections import Counter


def data_prep(instructions):
    data = [x.split('|') for x in instructions]
    return data


def part_one(data):
    y = 0
    for x in data:
        codes = x[1].split()
        for code in codes:
            if len(set(code)) < 5 or len(set(code)) == 7:
                y += 1
    return y


def part_two(data):
    y = 0
    digits = dict()
    summary = 0
    for x in data:
        wires = x[0].split()
        wires.sort(key=len)
        one, seven, four = wires[:3]
        eight = wires[-1]
        a = [h for h in seven if h not in one][0]
        letters = [h for h in x[0].replace(" ", "") if h != a]
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
        numbers = x[1].split()
        n_str = ""
        for number in numbers:
            for k,v in digits.items():
                if len(v) == len(number) and all(i in v for i in number):
                    n_str += str(k)
        summary += int(n_str)
    return summary


def main():
    file_path = "inputs/day_08.txt"
    instructions = read_file_to_lines(file_path)
    data = data_prep(instructions)
    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()
