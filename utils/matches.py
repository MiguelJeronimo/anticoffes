def matches(data, dictionary:list):
    for element in dictionary:
        if element in data:
            print(f"Element: {element}; data: {data}")
            return True
    return False
