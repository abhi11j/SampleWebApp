def normalize(values):
    """
    Normalize a list of numerical values to the range [0, 1].

    Parameters
    ----------
    values : list of float
        List of values to normalize.

    Returns
    -------
    list of float
        Normalized values.
    """
    min_val = min(values)
    max_val = max(values)
    # Avoid division by zero if all values are the same
    if min_val == max_val:
        return [0.0 for _ in values]
    return [(v - min_val) / (max_val - min_val) for v in values]
