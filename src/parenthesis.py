
def parenthesis(left, right, result):
    if left == 0 and right == 0:
        return

    choice_1 = []
    choice_2 = []

    if left > 0:
        choice_1 = [elem + '(' for elem in result]
        parenthesis(left - 1, right + 1, choice_1)

    if right > 0:
        choice_2 = [elem + ')' for elem in result]
        parenthesis(left, right - 1, choice_2)

    result.clear()
    result += choice_1 + choice_2

    return

if __name__ == '__main__':
    result = ['']
    parenthesis(4, 0, result)
    print(result)

