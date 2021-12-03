from utils.file_reader import read_file_to_lines


def part_one(instructions):
    gamma_rate = ""
    epsilon_rate = ""

    length = len(instructions[0])

    most_common = {k: 0 for k in range(length)}

    for line in instructions:
        for idx, bit in enumerate(line):
            match bit:
                case "1":
                    most_common[idx] += 1
                case "0":
                    most_common[idx] -= 1

    for idx in range(length):
        if most_common[idx] > 0:
            gamma_rate += str(1)
            epsilon_rate += str(0)
        else:
            gamma_rate += str(0)
            epsilon_rate += str(1)

    return int(gamma_rate, base=2) * int(epsilon_rate, base=2)


def part_two(instructions):
    oxygen_rate = ""
    scrubber_rate = ""

    length = len(instructions[0])

    def remove_items(f_list, itteration, switch = 1):
        n_list = list()
        one = 0

        for line in f_list:
            bit = line[itteration]
            match bit:
                case "1":
                    one += 1
                case "0":
                    one -= 1

        for line in f_list:
            bit = line[itteration]
            if switch:
                if one >= 0:
                    if bit == "1":
                        n_list.append(line)
                else:
                    if bit == "0":
                        n_list.append(line)
            else:
                if one < 0:
                    if bit == "1":
                        n_list.append(line)
                else:
                    if bit == "0":
                        n_list.append(line)

        return n_list

    oxygen = instructions
    for idx in range(length):
        oxygen = remove_items(oxygen, idx)
        if len(oxygen) == 1:
            break

    scrubber = instructions
    for idx in range(length):
        scrubber = remove_items(scrubber, idx, 0)
        if len(scrubber) == 1:
            break

    oxygen_rate = oxygen[0]
    scrubber_rate = scrubber[0]
    return int(oxygen_rate, base=2) * int(scrubber_rate, base=2)


def main():
    file_path = "inputs/day_03.txt"
    instructions = read_file_to_lines(file_path)
    print(part_one(instructions))  # 4006064
    print(part_two(instructions))  # 5941884


if __name__ == "__main__":
    main()
