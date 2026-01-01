def load_data(filepath):
    """
    Load data from a CSV file.

    Parameters
    ----------
    filepath : str
        Path to the CSV file.

    Returns
    -------
    list
        List of data rows.
    """
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            # Split each line by comma and strip whitespace
            data.append(line.strip().split(','))
    return data


def process_data(data):
    """
    Process the loaded data.

    Parameters
    ----------
    data : list
        List of data rows.

    Returns
    -------
    dict
        Dictionary with processed results.
    """
    result = {}
    # Example complex logic: count occurrences of each value in the first column
    for row in data:
        key = row[0]
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Process CSV data.")
    parser.add_argument('--input', required=True, help='Input CSV file path')
    parser.add_argument('--output', required=True, help='Output file path')
    args = parser.parse_args()

    # Load and process data
    data = load_data(args.input)
    results = process_data(data)

    # Save results to output file
    import json
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
