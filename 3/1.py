def adjacent_symbol(lines, line_no, lo, hi):
    for line in lines[line_no - 1 : line_no + 2]:
        line_segment = line[max(lo - 1, 0) : min(hi + 1, len(line))]
        for char in line_segment:
            if char != "." and not char.isdigit():
                return True
    return False


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    blank_line = ["." * len(lines[0])]
    lines = blank_line + lines + blank_line

    lo, hi, res = 0, 0, 0
    for line_no, line in enumerate(lines):
        i = 0
        while i < len(line):
            if line[i].isdigit():
                lo, hi = i, i + 1
                while hi < len(line) and line[hi].isdigit():
                    hi += 1
                if adjacent_symbol(lines, line_no, lo, hi):
                    res += int(line[lo:hi])
                i = hi
            else:
                i += 1

    print(res)
