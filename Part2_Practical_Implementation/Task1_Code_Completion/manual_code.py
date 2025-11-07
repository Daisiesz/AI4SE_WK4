def sort_dicts_by_key(data_list, sort_key):
    """
    Sort a list of dictionaries by a specified key.

    Parameters:
        data_list (list): List of dictionaries to sort.
        sort_key (str): Key name to sort by.

    Returns:
        list: A new list of dictionaries sorted by the given key.
    """
    try:
        return sorted(data_list, key=lambda item: item[sort_key])
    except KeyError:
        print(f"Error: Key '{sort_key}' not found in one or more dictionaries.")
        return data_list
    except TypeError:
        print("Error: Invalid data format. Expected a list of dictionaries.")
        return []

# Example usage
if __name__ == "__main__":
    records = [
        {"name": "Eve", "score": 80},
        {"name": "Dan", "score": 95},
        {"name": "Frank", "score": 70}
    ]
    result = sort_dicts_by_key(records, "score")
    print(result)
