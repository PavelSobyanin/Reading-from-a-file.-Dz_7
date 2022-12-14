cook_book = {
    'омлет': [
        {'ingridient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingridient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
    'утка по-пекински': [
        {'ingridient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingridient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingridient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingridient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        ],
    'запеченный картофель': [
        {'ingridient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
        {'ingridient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        ],
    'фахитос': [
        {'ingridient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
        {'ingridient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
        {'ingridient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
        {'ingridient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
        {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
        ]}


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()






