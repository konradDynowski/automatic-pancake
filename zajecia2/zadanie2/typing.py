def average(list_of_floats):
    av = 0.0
    try:
        av = sum([float(float_element) for float_element in list_of_floats]) / len(list_of_floats)
    except ValueError:
        return None
    return av