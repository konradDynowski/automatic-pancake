def generator(how_many=15):
    n_prev = 0
    yield n_prev
    n = 1
    yield n
    temp = 0
    how_many -= 2
    while how_many > 0:
        how_many -= 1
        temp = n + n_prev
        n_prev = n
        n = temp
        yield n

