from operator import call


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    """

    :rtype: object
    """
    return data.get(label, {}).get(name, None)


def store(data, *full_names):
    """Stores a name in the dictionary [data]"""
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, '')
        labels = 'first', 'middle', 'last'

        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people is None:
                # Initialize the sub-dictionary and list if not present
                if label not in data:
                    data[label] = {}
                data[label][name] = [full_name]
            else:
                # Append to the existing list
                people.append(full_name)  # type: ignore


storage = {}
init(storage)
store(storage, "Sveti Grin", "Misch Love Pepper", "Toli Grin", "Maja Valeria Grin", "Ann Valeria Brown")

print(storage)
print("People with the middle name 'Valeria':", lookup(storage, 'middle', 'Valeria'))
print("People without any middle name:", lookup(storage, 'middle', ''))

