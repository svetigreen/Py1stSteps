import random


# state: a tuple of states so far
# nextX: suggested horizontal position (x coordinate, or column) of the next queen
def conflict(state, nextX):
    nextY = len(state)  # nextY is the vertical position (y coordinate, or row) of the next queen
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


solution4 = list(queens(4))
print('4 Queens:', solution4)
print('# of solutions for 4 Queens:', len(solution4))
prettyprint(solution4[0])
print('# of solutions for 8 Queens:', len(list(queens())))
prettyprint(random.choice(list(queens())))
