def script(check, x, y):
    '''
    КОД ПОВЕДЕНИЯ ПЕРСОНАЖА ИГРОКА
    X, Y+1 - СТЕНА СНИЗУ
    X, Y-1 - СТЕНА СВЕРХУ
    X+1, Y - СТЕНА СПРАВА
    X-1, Y - СТЕНА СЛЕВА
    '''

    if check("gold", x, y) != 0: return "take"

    if check("level") == 1:
        if check("gold", x, y) == 0 and check("gold", x, y+1) == 0: return "right"
        if check("gold", x, y+1) != 0: return "down"

    if check("level") == 2:
        if check("gold", x+1,y) != 0:  return "right"
        if check("gold", x+2, y) != 0: return "right"
        if check("gold", x, y+1) != 0: return "down"
        if check("gold", x+1, y) == 0: return "up"

    if check("level") == 3:
        if check("wall", x, y+1) == True and check("wall", x-1, y) == False: return "left" #left
        if check("wall", x-1, y) == True and check("wall", x, y-1) == False: return "up" #up
        if check("wall", x+1, y) == True and check("wall", x, y+1) == False: return "down" #down
        if check("wall", x, y-1) == True and check("wall", x+1, y) == False: return "right" #right
        if check("wall", x, y+1) == False and check("wall", x+1, y) == False:
            if check("wall", x-1, y+1) == True:
                return "left"
            if check("wall", x-1, y-1) == True:
                return "up"
            if check("wall", x+1, y+1) == True:
                return "down"
            if check("wall", x+1, y-1) == True:
                return "right"

    if check("level") == 4:
        if check("wall", x, y - 1) == True and check("wall", x + 1, y) == False: return "right"
        if check("wall", x - 1, y) == True and check("gold", x + 6, y - 3) != 0 and check("wall", x + 2, y) == True: return "right"
        if check("gold", x, y + 4) != 0 and check("wall", x + 1, y + 4) == True: return "down"
        if check("wall", x + 1, y) == True and check("wall", x, y + 1) == False: return "down"
        if check("wall", x - 1, y) == True and check("wall", x, y - 1) == False: return "up"
        if check("wall", x, y + 1) == True and check("wall", x - 1, y) == False and check("wall", x + 1, y) == False and check("wall", x, y - 2) == True: return "up"
        if check("wall", x, y + 1) == True and check("wall", x - 1, y) == False: return "left"
        if check("wall", x, y + 1) == False and check("gold", x + 1, y) == False:
            if check("wall", x + 1, y - 1) == True:
                return "right"
            if check("wall", x + 1, y + 1) == True:
                return "down"
            if check("wall", x - 1, y + 1) == True:
                return "left"
            if check("wall", x - 1, y - 1) == True:
                return "up"
    return "pass"