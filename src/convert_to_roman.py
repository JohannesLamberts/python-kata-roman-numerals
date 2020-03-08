import math
numbers_file = open("./src/numbers.txt", "r")
numbers_file_lines = numbers_file.readlines()[0:100]

dictionary = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C'
}

arabic_steps = list(dictionary.keys())
arabic_steps_reverse = list(dictionary.keys())
arabic_steps_reverse.reverse()

subtractors = {
    5: 1,
    10: 1,
    50: 10,
    100: 10,
}

# def is_multiplicable(arabic):
#     return (math.log10(arabic) % 1) == 0

def next_arabic_step(arabic):
    return next(step for step in arabic_steps if step >= arabic)

def previous_arabic_step(arabic):
    return next(step for step in arabic_steps_reverse if step <= arabic)

def convert_to_roman(arabic):
    if arabic == 0:
        return ''
    if arabic == 1:
        return 'I'

    next_step = next_arabic_step(arabic)
    next_step_subtractor = subtractors[next_step]

    if arabic >= (next_step - next_step_subtractor) and arabic < next_step:
        return convert_to_roman(next_step_subtractor) + convert_to_roman(next_step)

    previous_step = previous_arabic_step(arabic)

    char = dictionary[previous_step]
    times = int(arabic / previous_step)
    rest = arabic % previous_step

    if times > 3:
        return convert_to_roman(previous_step) + convert_to_roman(arabic + previous_step)

    return char * times + convert_to_roman(rest)
    


numbers_file_lines_split = [line.split(" \t")[0:2] for line in numbers_file_lines]

all_succeeded = True

for [arabic, roman] in numbers_file_lines_split:
    converted = convert_to_roman(int(arabic))
    correct = converted == roman
    sign = 'x'
    if correct:
        sign = '/'
    print(arabic, '->', roman, " \t", converted, ' \t', sign)
    all_succeeded = all_succeeded and correct

assert all_succeeded, "at least one failed"

numbers_file.close()
