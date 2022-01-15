import random


def react_A(letter, a):
    global n
    s = 0
    for i in range(n):
        s += letter[i] * a[i]
    if s > 0:
        return 1
    else:
        return 0


def react_R(letter):
    global a1, a2, w
    s = react_A(letter, a1) * w[0] + react_A(letter, a2) * w[1]
    if s > 0:
        return 1
    else:
        return -1


def teach(letter1, letter2, w, a1, a2):
    reactl1a1 = react_A(letter1, a1)
    reactl1a2 = react_A(letter1, a2)
    reactl2a1 = react_A(letter2, a1)
    reactl2a2 = react_A(letter2, a2)
    if (reactl1a1 == reactl2a1 and reactl1a2 == reactl2a2) or (reactl1a1 == 0 and reactl1a2 == 0) or (reactl2a1 == 0 and reactl2a2 == 0):
        return -1   #если нет смысла обучаться, выходим и начинаем заново
    while react_R(letter1) > 0 or react_R(letter2) < 0:
        if react_R(letter1) > 0:
            w = decrease(w, letter1)
        if react_R(letter2) < 0:
            w = increase(w, letter2)
    print("w: " + str(w))


def increase(w, letter):    #увеличение веса
    global a1, a2
    if react_A(letter, a1) > 0:
        w[0] = w[0] + 1
    if react_A(letter, a2) > 0:
        w[1] = w[1] + 1
    return w


def decrease(w, letter):    #уменьшение веса
    global a1, a2
    if react_A(letter, a1) > 0:
        w[0] = w[0] - 1
    if react_A(letter, a2) > 0:
        w[1] = w[1] - 1
    return w


def test(letter):
    if react_R(letter) == -1:
        print("Похоже на букву 'О'")
    else:
        print("Похоже на букву 'Ц'")


letter1 = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]  #буква 'О'
letter2 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1]  #буква 'Ц'

testletter1 = [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]
testletter2 = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1]
testletter3 = [1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1]
testletter4 = [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0]
testletter5 = [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1]
testletter6 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0]

w = [0, 0]
n = len(letter1)
a1 = [0]*n
a2 = [0]*n
k = 0   # счётчик кол-ва обучений
while teach(letter1, letter2, w, a1, a2) == -1: #учимся, пока обучение не пройдёт успешно
    a1 = []
    a2 = []
    k = k + 1
    for i in range(n):
        a1.append(random.choice([1, 1, -1, -1, 0]))
        a2.append(random.choice([1, 1, -1, -1, 0]))
print('Я обучился с ' + str(k) + '-ой попытки!')

test(testletter1)
test(testletter2)
test(testletter3)
test(testletter4)
test(testletter5)
test(testletter6)