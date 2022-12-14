with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        cook_book_name = line.strip()
        dishes_count = int(file.readline())
        dishes = []
        for _ in range(dishes_count):
            emp = file.readline().strip().split(' | ')
            name, quantity, measure = emp
            dishes.append({'ingredient_name': name,
                           'quantity': int(quantity),
                           'measure': measure})
        file.readline()
        cook_book[cook_book_name] = dishes
    print(cook_book)