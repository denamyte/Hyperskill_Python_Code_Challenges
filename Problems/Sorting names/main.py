def sort_names(names):
    """Sort names by length in descending order."""
    for i in range(len(names)):
        index = i

        for j in range(i + 1, len(names)):
            if len(names[j]) > len(names[index]):
                index = j

        names[i], names[index], = names[index], names[i]

    return names
