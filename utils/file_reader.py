from typing import List


def read_file_to_lines(input_path: str) -> List[str]:
    with open(input_path, 'r') as file_handler:
        return [x.rstrip() for x in file_handler.readlines()]


def get_list_of_ints_from_file(input_path: str) -> List[int]:
    return [int(i) for i in read_file_to_lines(input_path)]
