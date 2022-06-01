"Напишите функцию generate_groups(), которая генерирует (не просто выдает готовый) список всех названий групп в том виде, который используется на сайте ЦАП."
def f1(gr_letter, gr_len):
    return ['И' + letter + 'БО-' + str(n) + '-20' for letter, length in zip(gr_letter, gr_len) for n in range(1, length + 1)]

print(f1(['В', 'К', 'Н', 'М'], [13, 5, 2, 4]))