def average(list_of_floats: list[float]) -> float | None:
    av = 0.0
    try:
        av = sum([float(float_element) for float_element in list_of_floats]) / len(list_of_floats)
    except ValueError:
        return None
    return av
