def find_the_parent(child):
    for p in (Drinks, Pastry, Sweets):
        if issubclass(child, p):
            print(p.__name__)
            break
