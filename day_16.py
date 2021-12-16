from math import prod
from utils.file_reader import read_file_to_lines


def data_prep(instructions):
    line = instructions[0]
    binary = ""
    for char in line:
        binary += format(int(char, 16), "04b")
    binary = binary
    return binary


def decode_binary(data):
    operator = {
        0: lambda x: sum(x),
        1: lambda x: prod(x),
        2: lambda x: min(x),
        3: lambda x: max(x),
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1])
    }
    # print(data)
    index = 0
    sum_package_version = 0
    value = []
    package_version = int(data[index:index+3], 2)
    package_type = int(data[index+3:index+6], 2)
    sum_package_version += package_version
    print("Package Version", package_version, data[index:index+3])
    print("Package Type", package_type, data[index+3:index+6])
    index += 6
    if package_type == 4:
        b_number = ""
        while True:
            package = data[index:index+5]
            b_number += package[1:]
            index += 5
            if package[0] == "0":
                break
        number = int(b_number, 2)
        print("Number", number, b_number)
        return sum_package_version, index, number
    else:
        next_bit = data[index]

        print("Next bit", next_bit)
        index += 1
        length = 15
        if next_bit == "0":
            length = 15
            length_in_bits = int(data[index:index+length],2)
            print("Length in bits", length_in_bits, data[index:index+length])
            #print("Bit layout:", data[index+length:index+length+length_in_bits])
            index += length
            cache_index = index + length_in_bits - 6
            while index < cache_index:
                s_packages, r_index, r_value = decode_binary(data[index:index + length_in_bits])
                value.append(r_value)
                sum_package_version += s_packages
                index += r_index
        elif next_bit == "1":
            length = 11
            number_of_subpackages = int(data[index:index+length],2)
            print("Number of subpackages", number_of_subpackages, data[index:index+length])
            index += length
            for i in range(number_of_subpackages):
                s_packages, r_index, r_value = decode_binary(data[index:])
                value.append(r_value)
                sum_package_version += s_packages
                index += r_index

    return sum_package_version, index, operator[package_type](value)


def part_one(data):
    return decode_binary(data)


def part_two(data):
    return None


def main():
    file_path = "inputs/day_16.txt"
    instructions = read_file_to_lines(file_path)
    # instructions = ["38006F45291200"]
    # instructions = ["EE00D40C823060"]
    # instructions = ["8A004A801A8002F478"]
    # instructions = ["620080001611562C8802118E34"]
    # instructions = ["C0015000016115A2E0802F182340"]
    # instructions = ["A0016C880162017C3686B18A3D4780"]
    data = data_prep(instructions)
    print(part_one(data))  # 981, 299227024091
    # print(part_two(data))


if __name__ == "__main__":
    main()
