import csv
from matplotlib import pyplot as plt


def f11():
    with open('/Users/zakharden/PycharmProjects/TASKSMIREA/3z/games.csv', encoding='utf8') as f:
        arr = list(csv.reader(f, delimiter=';'))

    gamesyrs = []
    genres = []
    gamesyrsCount = []
    genresCount = []
    genres1 = []
    genres2 = []
    genres3 = []
    genresCount1 = []
    genresCount2 = []
    genresCount3 = []
    for i in range(0, len(arr)):
        genres.append(arr[i][1])
        if arr[i][3] != 'не издана':
            gamesyrs.append(int(arr[i][3]))
            if int(arr[i][3]) < 1990:
                genres1.append(arr[i][1])
            if 2000 > int(arr[i][3]) > 1989:
                genres2.append(arr[i][1])
            if 2010 > int(arr[i][3]) > 1999:
                genres3.append(arr[i][1])

    uniqyears = list(set(gamesyrs))
    uniqGenres = list(set(genres))
    uniqGenres1 = list(set(genres1))
    uniqGenres2 = list(set(genres2))
    uniqGenres3 = list(set(genres3))
    print(uniqyears)
    print(uniqGenres)

    for i in range(0, len(uniqyears)):
        gamesyrsCount.append(gamesyrs.count(uniqyears.__getitem__(i)))
    for i in range(0, len(uniqGenres)):
        genresCount.append(genres.count(uniqGenres.__getitem__(i)))
    for i in range(0, len(uniqGenres1)):
        genresCount1.append(genres1.count(uniqGenres1.__getitem__(i)))
    for i in range(0, len(uniqGenres2)):
        genresCount2.append(genres2.count(uniqGenres2.__getitem__(i)))
    for i in range(0, len(uniqGenres3)):
        genresCount3.append(genres3.count(uniqGenres3.__getitem__(i)))

    plt.bar(uniqyears, gamesyrsCount)
    plt.show()

    plt.bar(uniqGenres, genresCount)
    plt.show()

    plt.bar(uniqGenres1, genresCount1)
    plt.show()

    plt.bar(uniqGenres2, genresCount2)
    plt.show()

    plt.bar(uniqGenres3, genresCount3)
    plt.show()


f11()