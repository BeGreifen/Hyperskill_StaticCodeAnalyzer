def get_percentage(number: float, round_digits: int = None):
    if round_digits is None:
        return "".join([str(int(number * 100)), "%"])
    return "".join([str(round(number * 100, round_digits)), "%"])
