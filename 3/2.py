import math


def is_gear_ratio(lines, line_no, col_no):
    """
    Take a 9x9 surrounding an asterisk and calculate the number of unique part numbers.

    Return the coordinates of each found part number.
    """
    num_coords = []
    for i, line in enumerate(lines[line_no - 1 : line_no + 2]):
        start = max(col_no - 1, 0)
        end = min(col_no + 2, len(line))
        line_segment = line[start:end]

        j = 0
        while j < len(line_segment):
            if line_segment[j].isdigit():
                num_coords.append((line_no - 1 + i, start + j))
                while j < len(line_segment) and line_segment[j].isdigit():
                    j += 1
            else:
                j += 1

    return num_coords


def calculate_ratio(coords, lines):
    """
    Given the coordinates of the numbers comprising a ratio, calculate their product.

    Expand left and right from the given coordinate to find the whole number.
    """
    res = []
    for num_coord in coords:
        row, col = num_coord

        l, r = col, col
        while l > -1 and lines[row][l].isdigit():
            l -= 1
        while r < len(lines[1]) and lines[row][r].isdigit():
            r += 1

        res.append(int("".join(lines[row][l + 1 : r])))

    return math.prod(res)


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    blank_line = ["." * len(lines[0])]
    lines = blank_line + lines + blank_line

    res = 0
    for line_no, line in enumerate(lines):
        for col_no, char in enumerate(line):
            if char == "*":
                num_coord = is_gear_ratio(lines, line_no, col_no)
                if len(num_coord) == 2:
                    res += calculate_ratio(num_coord, lines)

    print(res)
