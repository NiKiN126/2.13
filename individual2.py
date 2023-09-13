#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import packet.shop as s
import packet.display as d
import packet.select as sel


def main():
    """
    главная функция программы
    """
    shops = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            shop = s.get_shop()
            shops.append(shop)
            if len(shops) > 1:
                shops.sort(key=lambda item: item.get('product', ''))
        elif command == 'list':
            d.display_shops(shops)
        elif command.startswith('select '):
            selected = sel.select_shops(shops)
            d.display_shops(selected)
        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить магазин;")
            print("select - показать товары из заданного магазина;")
            print("list - вывести список магазинов;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
