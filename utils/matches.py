def matches(data, dictionary:list):
    for element in dictionary:
        print(f"Element: {element}; data: {data}")
        if element in dictionary:
            return True
        else:
            return False