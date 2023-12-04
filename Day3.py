def get_numbers(lines):
    numbers = []
    for line_index, line in enumerate(lines):
        number_start = 0
        while number_start < len(line):
            number = " "
            char = line[number_start]
            if char.isdigit():
                number = char
                number_end = number_start + 1
                while line[number_end].isdigit():
                    number += line[number_end]
                    number_end += 1
                numbers.append([int(number), [line_index, number_start, number_end]])
            number_start += len(number)
    return numbers


def get_symbols(lines):
    numbers = get_numbers(lines)
    result = []
    for number in numbers:
        # define search rectangle
        if number[1][0] == 0:
            line_indexes = [number[1][0], number[1][0] + 1]
        elif number[1][0] == len(lines)-1:
            line_indexes = [number[1][0] - 1, number[1][0]]
        else:
            line_indexes = [number[1][0] - 1, number[1][0], number[1][0] + 1]
        if not number[1][1] == 0:
            start = number[1][1] - 1
        else:
            start = number[1][1]

        if not number[1][2] == 0:
            end = number[1][2] + 1
        else:
            end = number[1][1]
        rect = [line_indexes, start, end]
        # lookup symbol in rect
        for line_index in line_indexes:
            line = lines[line_index]
            for char_index in range(rect[1], rect[2]):
                char = line[char_index]
                if not char.isdigit() and not char == "." and not char == "\n":
                    result.append([number[0], True, [line_index, char_index]])
                else:
                    result.append([number[0], False, []])
    return result


def sum_parts(lines):
    s = 0
    numbers = get_symbols(lines)
    for number in numbers:
        if number[1]:
            s += number[0]
    return s


def sum_gears(lines):
    s = 0
    numbers = get_symbols(lines)
    symbols = [number[2] for number in numbers if not number[2] == []]
    gears = {}
    for number in numbers:
        if symbols.count(number[2]) == 2:
            if not gears.get(str(number[2])):
                gears[str(number[2])] = [number[0]]
            else:
                gears[str(number[2])].append(number[0])
    for gear in gears.values():
        s += (gear[0] * gear[1])
    return s


if __name__ == "__main__":
    with open("day3.txt", "r") as f:
        content = f.readlines()
    print(sum_parts(content))
    print(sum_gears(content))
