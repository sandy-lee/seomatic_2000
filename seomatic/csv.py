def csv(path=None, has_header=False, number_rows=1):
    """
     :param path: path to csv to import (string)
     :param has_header: boolean for if csv has a header row to be ignored or not (bool)
     :param number_rows: how many rows to return (int)
     :return: required rows from CSV (list)
     """
    import csv
    result = []
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        if has_header:
            next(csv_reader)
            for counter, row in enumerate(csv_reader):
                result.append(row)
                if counter == (number_rows - 1):
                    return result
        else:
            for counter, row in enumerate(csv_reader):
                result.append(row)
                if counter == (number_rows - 1):
                    return result
