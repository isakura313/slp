# положим, нам нужно сделать функцию
# которая не разрешит делать отрицательные ценники

def aplly_discount(product, discount):
    """
    принимает на вход данные о товаре и скидку
    """
    price = int(product['цена'] * (1.0 - discount))
    assert 0.1 <= price <= product['цена']
    return product['имя'], price

kreslo = {'имя': 'кресло', 'цена': 1200}

try:
    print(aplly_discount(kreslo, 1.2))
    # есть запись в бд
except AssertionError:
    print("А дурачок ты какие данные вводишь!")

