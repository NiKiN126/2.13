#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def display_shops(shops):
    """
    Отображает данные о товаре в виде таблицы и
    Сортирует данные, по названию маганзина
    """
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 8,
        '-' * 20
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "No",
            "Название.",
            "Товар",
            "Цена"
        )
    )
    print(line)
    for idx, shop in enumerate(shops, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(

                idx,
                shop.get('name', ''),
                shop.get('product', ''),
                shop.get('price', 0)

            )
        )
        print(line)
