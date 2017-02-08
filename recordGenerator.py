# python 3.4
# TODO: generate US phone numbers in a variety of formats
import random


def generateNumber():
    """
        phone number types:
        0: xxx xxx xxxx
        1: xxx-xxx-xxxx
        2: (xxx) xxx xxxx
        3: (xxx) xxx-xxxx
        4: xxx.xxx.xxxx
        5: (xxx) xxx.xxxx
        6: xxxxxxxxxx

    :return:
    """

    numType = 2      #random.randint(0, 6)
    number = []
    if numType == 0:
        for i in range(2):
            for k in range(3):
                number.append(random.randint(0, 9))
            number.append(' ')
        for i in range(4):
            number.append((random.randint(0, 9)))
    elif numType == 1:
        for i in range(2):
            for k in range(3):
                number.append(random.randint(0, 9))
            number.append('-')
        for i in range(4):
            number.append((random.randint(0, 9)))
    elif numType == 2:
        number.append('(')
        for i in range(3):
            number.append(random.randint(0, 9))

        number.append(')')
        number.append(' ')

        for i in range(3):
            number.append(random.randint(0, 9))

        number.append(' ')

        for i in range(4):
            number.append(random.randint(0, 9))

    #print(number)
    """
    for digit in number:
        print(digit, end='', flush=True)
    """


generateNumber()
