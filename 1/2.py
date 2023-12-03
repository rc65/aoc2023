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
    lo, hi = 0, 1

    while lo < len(line):
        if str.isdigit(line[lo]):
            return line[lo]

        word = ''.join(line[lo:hi])
        word_rev = word[::-1]
        if word in number_string or word_rev in number_string:
            if word in number_strings:
                return number_strings[word]
            if word_rev in number_strings:
                return number_strings[word_rev]
            hi += 1
        else:
            lo += 1
            hi = lo + 1


with open('input.txt', 'r') as f:
    _sum = 0
    for line in f.readlines():
        line = line.strip()
        first = find_number(line)
        last = find_number(line[::-1])
        line_sum = int(first + last)
        print(line, line_sum)
        _sum += line_sum

    print(_sum)
