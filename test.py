backpack = {}


def bu(**items):
    for item in items:
        backpack[item] = items.get(item)
    return backpack


def value_func(**values):
    for value in values:
        return value

d = {'sword': 10, 'apple': 5}
bu(**d)
print backpack
