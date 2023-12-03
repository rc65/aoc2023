number_strings = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}

number_string = "zeroonetwothreefourfivesixseveneightnine"

def find_number(line):

    for char in line:
        if str.isdigit(char):
            return char


with open('input.txt', 'r') as f:
    _sum = 0
    for line in f.readlines():
        line = line.strip()
        first = find_number(line)
        last = find_number(line[::-1])
        line_sum = int(first + last)
        _sum += line_sum

    print(_sum)
