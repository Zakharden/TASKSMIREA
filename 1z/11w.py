def fast_mul_gen(y):
    func = f"mul_{y}"
    print(f"def {func}(x):")
    print("\tres = 0")
    while y > 1:
        if y % 2:
            print("\tres = res + x")
        print("\tx = x + x")
        y //= 2
    print("\tres = res + x")
    print("\treturn res")


def main():
    x = int(input("Введите значение для примера работы функции: "))
    print()
    fast_mul_gen(x)

main()