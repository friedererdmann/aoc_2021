from utils.file_reader import read_file_to_lines


def data_prep(instructions):
    data = dict()
    for x, line in enumerate(instructions):
        for y, char in enumerate(line):
            data[x, y] = int(char)
    return data


def astar(data, start, goal):
    came_from = {start: data[start]}
    visited = set()

    while True:
        current = min(came_from, key=came_from.get)
        score = came_from[current]
        print(current, data[current], score)
        came_from.pop(current)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            return score - data[start]
        offsets = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        neighbors = [(current[0]+offset[0], current[1]+offset[1]) for offset in offsets]
        for neighbor in neighbors:
            if neighbor in visited or not data.get(neighbor):
                continue
            came_from[neighbor] = score + data[neighbor]



def part_one(data):
    starting_point = (0, 0)
    ending_point = (max([x for x, _ in data.keys()]),max([y for _, y in data.keys()]))
    return astar(data, starting_point, ending_point)


def part_two(data):
    return data


def main():
    file_path = "inputs/day_15.txt"
    instructions = read_file_to_lines(file_path)
    data = data_prep(instructions)
    print(part_one(data))  # 1588, 2170
    # print(part_two(data))  # 2188189693529, 2422444761283


if __name__ == "__main__":
    main()
