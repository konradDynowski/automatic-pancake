""" liczenie pól i obwodów dla figur dwuwymiarowych """
MATH_PI = 3.14


def pole_kwadratu(dlugosc_boku):
    """ zwraca pole kwadratu """
    return dlugosc_boku ** 2


def obwod_kwadratu(dlugosc_boku):
    """ zwraca obwod kwadratu """
    return 4 * dlugosc_boku


def pole_prostokata(dlugosc_boku_1, dlugosc_boku_2):
    """ zwraca pole prostokata """
    return dlugosc_boku_1 * dlugosc_boku_2


def obwod_prostokata(dlugosc_boku_1, dlugosc_boku_2):
    """ zwraca obwod prostokata """
    return 2 * dlugosc_boku_1 + 2 * dlugosc_boku_2


def pole_kola(srednica):
    """ zwraca pole kola """
    return srednica ** 2 * MATH_PI / 2


def obwod_kola(srednica):
    """ zwraca obwod kola """
    return MATH_PI * srednica
