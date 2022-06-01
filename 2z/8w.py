"Реализуйте генератор случайных данных ФИО. Список распространенных имен позволяется скачать из интернета. Фамилии необходимо генерировать самостоятельно. Впрочем, можете попробовать генерировать и имена."
import random


NameFirst = [ "Ив", "Мар", "Нам", "Рис"]
NameSecond = ["а", "я", "ий", "ср", "иско"]
SurNFirst = ["Грибо", "Молоко", "Тро", "Серо" , "Сыро", "Хлебо"]
SurNSecond = ["ин", "языков", "едов"]
WithDot = ["З.", "В.", "Н.", "А", "Р.", "С.", "Д."]

n = int(input("Введите количество имён: "))

for i in range (n):
    print(random.choice(NameFirst) + random.choice(NameSecond), random.choice(WithDot), random.choice(SurNFirst) + random.choice(SurNSecond))