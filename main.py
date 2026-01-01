# main.py

def process_data(data):
    # Remove duplicates to ensure unique entries
    unique_data = list(set(data))
    return unique_data


def compute_statistics(values):
    # Guard against empty input to avoid ZeroDivisionError
    if not values:
        return {'mean': None, 'max': None, 'min': None}
    # Calculate mean, max, and min in a single pass for efficiency
    total = 0
    maximum = float('-inf')
    minimum = float('inf')
    for v in values:
        total += v
        if v > maximum:
            maximum = v
        if v < minimum:
            minimum = v
    mean = total / len(values)
    return {'mean': mean, 'max': maximum, 'min': minimum}


def main():
    data = [1, 2, 2, 3, 4, 4, 5]
    # Preprocess data before computing statistics
    cleaned_data = process_data(data)
    stats = compute_statistics(cleaned_data)
    print(f"Statistics: {stats}")


if __name__ == "__main__":
    main()
