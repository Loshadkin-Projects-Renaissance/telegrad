admin_id = 792414733

emjs = ['🚶', '🚶‍♀️']

h_colors = ['gold', 'orange', 'brown', 'black']
h_lenghts = ['short', 'medium', 'long']

def init_product(food, cost=0, give_desc=False):
    name = 'Не опознано'
    value = 0
    food_desc = 'Неизвестно'
    code = food
    weight = 1
    if food == 'bread':
        name = 'Хлеб'
        value = 1
        food_desc = 'Обычный хлеб. Восстанавливает 1🍗.'
        weight = 2

    elif food == 'sousage':
        name = 'Сосиски'
        value = 4
        food_desc = 'Сосиски из свинины. Восстанавливают 4🍗.'
        weight = 6

    elif food == 'conserves':
        name = 'Рыбные консервы'
        value = 3
        food_desc = 'Дешёвые консервы. Для тех, кто не очень богат. Восстанавливают 3🍗.'
        weight = 5

    obj = {
        'cost': cost,
        'value': value,
        'name': name,
        'code': code,
        'weight': weight
    }
    if give_desc:
        return food_desc
    return obj

streets = {
    'bitard_street': {
        'name': 'Битард-стрит',
        'nearlocs': ['meet_street', 'shop_street'],
        'code': 'bitard_street',
        'homes': ['17', '18', '30'],                                    
        'buildings': {},
        'humans': []
    },

    'new_street': {
        'name': 'Новая',
        'nearlocs': ['meet_street', 'shop_street'],
        'code': 'new_street',
        'homes': ['101', '228'],
        'buildings': {},
        'humans': []
    },

    'shop_street': {
        'name': 'Торговая',
        'nearlocs': ['bitard_street', 'new_street'],
        'code': 'shop_street',
        'homes': ['290', '311', '81'],
        'buildings': {
            'sitniy': {
                'name': 'Сытный',
                'type': 'shop',
                'street': 'shop_street',
                'humans': [],
                'code': 'sitniy',
                'products': {
                    'bread': init_product('bread', 50),
                    'sousage': init_product('sousage', 300),
                    'conserves': init_product('conserves', 150)
                }
            }
        },
        'humans': []
    },

    'meet_street': {
        'name': 'Встречная',
        'nearlocs': ['new_street', 'bitard_street'],
        'code': 'meet_street',
        'homes': [],
        'buildings': {},
        'humans': []
    }

}