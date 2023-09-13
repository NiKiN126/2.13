#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_shop():
    """
    Данная функция добавляет пары
    ключ-значение в словарь
    для каждого товара
    """
    name = input("Название магазина ")
    product = input("Товар ")
    price = int(input("Цена "))
    return{
        'name': name,
        'product': product,
        'price': price,
    }
