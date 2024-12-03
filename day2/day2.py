from typing import List



def is_report_safe(report: List[int]):
    # all increasing or all decreasing
    # adjacent differ by at least one and at most three
    x = [(i < j and (j - i in range(1,4))) for i,j in zip(report[:], report[1:])]
    y = [(i > j and (i - j in range(1,4))) for i,j in zip(report[:], report[1:])]
    print(x,y)
    if not (all(x) or all(y)):
        return False
    return True


def parse_input(x: str):
    reports = x.split('\n')
    data = []
    for r in reports:
        levels = r.split(' ')
        levels = [int(x) for x in levels]
        data.append(levels)
    return data


def test_example():

    example = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

    data = parse_input(example)

    count = 0
    for report in data:
        if is_report_safe(report):
            count +=1
    assert count == 2


def test_part1():

    with open('input.txt', 'r') as f:
        dat = f.read().strip()

    data = parse_input(dat)

    count = 0
    for report in data:
        if is_report_safe(report):
            count +=1

    assert count == 591



def test_part2():
    pass
