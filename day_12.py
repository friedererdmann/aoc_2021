from collections import Counter
from utils.file_reader import read_file_to_lines

START = "start"
END = "end"


def data_prep(instructions):
    data = [x.split("-") for x in instructions]
    return data


def forward(data, start, paths=None, full_path=None, visited=None):
    all_paths = list()
    if not full_path:
        full_path = list()
    full_path.append(start)
    if not paths:
        paths = list()
    if not visited:
        visited = list()
    possibilities = [path for path in data if start in path]
    for path in possibilities:
        next = 1 - path.index(start)
        target = path[next]
        direction = [start, target]
        if direction[1] == END:
            # print(full_path, END)
            all_paths.append(full_path)
            continue
        if direction not in paths and target not in visited:
            if target.islower() and target in full_path:
                continue
            paths.append(direction)
            if start.islower():
                visited.append(start)
            all_paths += forward(data, target, paths, full_path, visited)
            if visited:
                visited.pop(-1)
            if paths:
                paths.pop(-1)
            if full_path:
                full_path.pop(-1)
    return all_paths


def forward_two(data, start, full_path=None, visited=None, twice=False):
    all_paths = list()
    if not full_path:
        full_path = list()
    full_path.append(start)
    if not visited:
        visited = list()
    possibilities = [path for path in data if start in path]
    for path in possibilities:
        next = 1 - path.index(start)
        target = path[next]
        direction = [start, target]
        if target == END:
            c = Counter(full_path[1:])
            lower = [count for item, count in c.items() if item.islower()]
            items = lower.count(2)
            if items > 1:
                continue
            all_paths.append([*full_path, END])
            continue
        if target == START:
            continue
        if target.islower() and full_path.count(target) > 1:
            continue
        if start.islower():
            visited.append(start)
        all_paths += forward_two(data, target, full_path, visited, twice)
        if visited:
            visited.pop(-1)
        if full_path:
            full_path.pop(-1)
    return all_paths


def part_one(data):
    paths = forward(data, START)
    return len(paths)


def part_two(data):
    paths = forward_two(data, START)
    ruled = list()
    for path in paths:
        c = Counter(path[1:-1])
        lower = [count for item, count in c.items() if item.islower()]
        items = lower.count(2)
        # print(lower)
        if items < 2:
            ruled.append(path)
    return len(ruled)


def main():
    file_paths = ["inputs/day_12.txt","inputs/day_12_2.txt","inputs/day_12_3.txt","inputs/day_12_original.txt"]
    print(10, 19, 226, 4549)
    print(36, 103, 3509)
    for file_path in file_paths:
        instructions = read_file_to_lines(file_path)
        data = data_prep(instructions)
        print(part_one(data))  # 10, 19, 226, 4549
        print(part_two(data))  # 36, 103, 3509, 120535


if __name__ == "__main__":
    main()
