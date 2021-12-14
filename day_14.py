from timeit import timeit
from utils.file_reader import read_file_to_lines
from collections import Counter


def data_prep(instructions):
    element = instructions[0]
    rules = {a: b for a, b in [x.split(" -> ") for x in instructions[2:]]}
    return element, rules


def part_one(data):
    length = 10
    element, rules = data
    element = [x for x in element]
    for i in range(length):
        for j in range(len(element)-1):
            key = element[j*2] + element[j*2+1]
            element.insert((j*2)+1, rules[key])
    c = Counter(element)
    most = max(c, key=c.get)
    least = min(c, key=c.get)
    return element.count(most)-element.count(least)


def part_two(data):
    length = 40
    element, rules = data
    count = {x: 0 for x in rules.keys()}
    for j in range(len(element)-1):
        key = element[j:j+2]
        count[key] += 1
    #prep done
    for i in range(length):
        new_count = {x: 0 for x in rules.keys()}
        for key, value in count.items():
            if value > 0:
                key_one = key[0] + rules[key]
                key_two = rules[key] + key[1]
                new_count[key_one] += value
                new_count[key_two] += value
        count = new_count.copy()
    new_element = ""
    counter = {x: 0 for x in rules.values()}
    for key, value in count.items():
        counter[key[0]] += value
    counter[element[-1]] += 1
    c = Counter(counter)
    most = max(c, key=c.get)
    least = min(c, key=c.get)
    return counter[most]-counter[least]


def main():
    file_path = "inputs/day_14.txt"
    instructions = read_file_to_lines(file_path)
    data = data_prep(instructions)
    print(part_one(data))  # 1588, 2170
    print(part_two(data))  # 2188189693529, 2422444761283


if __name__ == "__main__":
    main()
