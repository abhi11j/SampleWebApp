class DataProcessor:
    """
    DataProcessor handles loading and processing of data files.
    """
    def __init__(self, config):
        """
        Initialize the DataProcessor with configuration.

        Parameters
        ----------
        config : dict
            Configuration dictionary for processing options.
        """
        self.config = config

    def load_data(self, filepath):
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
                # Split line by comma and strip whitespace
                row = [item.strip() for item in line.split(',')]
                data.append(row)
        return data

    def process_data(self, data):
        """
        Process the loaded data according to configuration.

        Parameters
        ----------
        data : list
            List of data rows.

        Returns
        -------
        list
            Processed data.
        """
        processed = []
        for row in data:
            # Example: filter out rows with missing values
            if all(row):  # Only keep rows with no empty values
                processed.append(row)
        return processed
