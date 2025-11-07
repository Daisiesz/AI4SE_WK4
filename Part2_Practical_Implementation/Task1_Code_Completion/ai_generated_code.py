def sort_dicts_by_key(data, key):
    """Sorts a list of dictionaries by the given key."""
    return sorted(data, key=lambda x: x.get(key, None))

# Example usage
if __name__ == "__main__":
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 22}
    ]
    sorted_people = sort_dicts_by_key(people, "age")
    print(sorted_people)
