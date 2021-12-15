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
            current_value = came_from.get(neighbor)
            if not current_value or score + data[neighbor] < current_value:
                came_from[neighbor] = score + data[neighbor]


def part_one(data):
    starting_point = (0, 0)
    ending_point = (max([x for x, _ in data.keys()]),max([y for _, y in data.keys()]))
    return astar(data, starting_point, ending_point)


def part_two(data):
    large_data = dict()
    for i in range(5):
        for j in range(5):
            for k,v in data.items():
                value = v + i + j
                while value > 9:
                    value = value - 9
                index_x = k[0] + (i*100)
                index_y = k[1] + (j*100)
                large_data[(index_x, index_y)] = value
                print((index_x, index_y), value, i, j)

    starting_point = (0, 0)
    ending_point = (max([x for x, _ in large_data.keys()]),max([y for _, y in large_data.keys()]))
    return astar(large_data, starting_point, ending_point)


def main():
    file_path = "inputs/day_15.txt"
    instructions = read_file_to_lines(file_path)
    data = data_prep(instructions)
    print(part_one(data))  # 1588, 2170
    print(part_two(data))  # 2188189693529, 2422444761283


if __name__ == "__main__":
    main()
