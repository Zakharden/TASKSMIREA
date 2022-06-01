
"""Преобразование Барроуза-Уилера используется в задачах сжатия данных и в области биоинформатики. Реализуйте прямое и обратное преобразование и оцените результаты с использованием RLE-кодирования.
"""

def f11(s):
    n = len(s)
    a = [""] * n
    for i in range(n):
        a[i] = [""] * n
    for i in range(n):
        for j in range(n):
            a[i][j] = s[-len(s) + i + j]
    a.sort()
    s1 = ""
    num = a.index(list(s))
    for i in range(n):
        s1 += a[i][n - 1]
    return [s1, num]


def f12(sn):
    s1 = sn[0]
    n1 = sn[1]
    n = len(s1)
    a = [""] * n
    for i in range(n):
        a[i] = [""] * n
    for i in range(n):
        for j in range(n):
            a[j][n - i - 1] = s1[j]
        a.sort()
    return a[n1]


from itertools import groupby


def rle_encode(data):
    return [(k, len(list(g))) for k, g in groupby(data)]


s = "Сегодня именно тот день, когда я решил сдать все задачи по Python."
sn = (f11(s))
print(sn[0])
print(*f12(sn), sep="")
print(rle_encode(s))
print(rle_encode(sn[0]))