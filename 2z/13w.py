import os


def f13():
    print("digraph G {")
    for root, dirs, files in os.walk('/Users/zakharden/Downloads/University/Схемотехника'):
        data = root
        str_tr = ''
        for item in reversed(data):
            if (item != "/"):
                str_tr += item
            else:
                break
        p = root.split("/")
        print(p[len(p) - 2] + "->" + str_tr[::-1])
    print("}")


f13()