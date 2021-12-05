import profile
from utils.file_reader import read_file_to_lines


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "(x={0},y={1})".format(self.x, self.y)


class Line:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.width = self._width()
        self.height = self._height()
        self.top_left = self._top_left()
        self.h_dir = self._h_dir()
        self.w_dir = self._w_dir()

    def _width(self):
        return abs(self.A.x - self.B.x) + 1

    def _height(self):
        return abs(self.A.y - self.B.y) + 1

    def _top_left(self):
        return Point(min(self.A.x, self.B.x), min(self.A.y, self.B.y))

    def _h_dir(self):
        return 1 if self.A.x < self.B.x else -1

    def _w_dir(self):
        return 1 if self.A.y < self.B.y else -1

    def __repr__(self):
        return "(A={0},B={1})".format(self.A, self.B)


class Grid:
    def __init__(self):
        self.grid = dict()

    def add_point(self, x, y):
        if x not in self.grid:
            self.grid[x] = dict()
        if y not in self.grid[x]:
            self.grid[x][y] = 0
        self.grid[x][y] += 1

    def get_two_or_more(self):
        two_or_more = 0
        for line in self.grid.values():
            for row in line.values():
                if row > 1:
                    two_or_more += 1
        return two_or_more

    def horizontal_line(self, line):
        if line.height == 1:
            for x in range(line.top_left.x, line.top_left.x + line.width):
                self.add_point(x, line.top_left.y)
        elif line.width == 1:
            for y in range(line.top_left.y, line.top_left.y + line.height):
                self.add_point(line.top_left.x, y)
        return self

    def diagonal_line(self, line):
        if line.width == line.height:
            for x in range(line.width):
                self.add_point(line.A.x + line.h_dir * x, line.A.y + line.w_dir * x)
        return self

    def __repr__(self):
        string = ""
        x = max([value for values in self.grid.values() for value in values]) + 1
        y = len(self.grid.values())
        for column in range(y):
            for line in range(x):
                string += " {0}".format(self.grid.get(line, dict()).get(column, "."))
            string += "\n"
        return string


def data_prep(instructions):
    lines = []
    for line in instructions:
        lines.append(Line(*[Point(int(a.split(",")[0]), int(a.split(",")[1])) for a in [x for x in line.split(" -> ")]]))
    return lines


def part_one(lines, grid):
    for line in lines:
        grid.horizontal_line(line)
    return grid


def part_two(lines, grid):
    for line in lines:
        grid.diagonal_line(line)
    return grid


def main():
    file_path = "inputs/day_05.txt"
    instructions = read_file_to_lines(file_path)
    lines = data_prep(instructions)
    grid = Grid()
    grid = part_one(lines, grid)
    print(grid.get_two_or_more())
    grid = part_two(lines, grid)
    print(grid.get_two_or_more())


if __name__ == "__main__":
    profile.run("main()", sort="cumulative")
