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
    summary = 0
    for wires, signals in data:
        # collect known digits
        wires.sort(key=len)
        one, seven, four = wires[:3]
        eight = wires[-1]
        # derive which letter the led element a is mapped to
        a = [letter for letter in seven if letter not in one][0]
        # get a flat list of the usage of all other letters mapped
        led_strips = [letter for wire in wires for letter in wire if letter != a]
        for letter, count in Counter(led_strips).items():
            # we know b, c, e and f have unique amounts so we can map them directly
            if count == 6:
                b = letter
            if count == 4:
                e = letter
            if count == 8:
                c = letter
            if count == 9:
                f = letter
        # deduct d must be the element used in four that is not found yet
        d = [letter for letter in four if letter not in [b, c, f]][0]
        # deduct g must be the last remaining element
        g = [letter for letter in eight if letter not in [a, b, c, d, e, f]][0]
        # map the displayed digit to the correct elements making up the display
        digits = {
            0: [a, b, c, e, f, g],
            1: [c, f],
            2: [a, c, d, e, g],
            3: [a, c, d, f, g],
            4: [b, c, d, f],
            5: [a, b, d, f, g],
            6: [a, b, d, e, f, g],
            7: [a, c, f],
            8: [a, b, c, d, e, f, g],
            9: [a, b, c, d, f, g]
        }
        # match the numbers to the known digits and sum them up
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
