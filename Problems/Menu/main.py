menu = {
    'pizza': 'Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy',
    'salad': 'Caesar salad, Green salad, Tuna salad, Fruit salad',
    'soup': 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'
}
dishes = menu.get(input())
print(dishes if dishes is not None else "Sorry, we don't have it in the menu")
