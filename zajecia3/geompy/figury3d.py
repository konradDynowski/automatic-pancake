""" liczenie pól i obwodów dla figur dwuwymiarowych """
MATH_PI = 3.14


def objetosc_szescianu(dlugosc_boku):
    """ zwraca objetosc szescianu """
    return dlugosc_boku ** 3


def powierzchnia_szescianu(dlugosc_boku):
    """ zwraca powierzchnia szescianu """
    return 6 * dlugosc_boku ** 2


def objetosc_prostopadloscianu(dlugosc_boku_1, dlugosc_boku_2, dlugosc_boku_3):
    """ zwraca objetosc prostopadloscianu """
    return dlugosc_boku_1 * dlugosc_boku_2 * dlugosc_boku_3


def powierzchnia_prostopadloscianu(dlugosc_boku_1, dlugosc_boku_2,
                                   dlugosc_boku_3):
    """ zwraca powierzchnia prostopadloscianu """
    return float(2 * dlugosc_boku_1 * dlugosc_boku_2
                 + 2 * dlugosc_boku_2 * dlugosc_boku_3
                 + 2 * dlugosc_boku_1 * dlugosc_boku_3)


def objetosc_kuli(srednica):
    """ zwraca objetosc kuli """
    return srednica ** 3 * MATH_PI / 6


def powierzchnia_kuli(srednica):
    """ zwraca powierzchnia kuli """
    return MATH_PI * srednica ** 2
