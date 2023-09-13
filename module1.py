#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(a, b):
    x = (a * b) - (a / b)

    def fout(a, b):
        return f"Для значений {a}, {b} функция f(a, b) = {x}"
    return fout(a, b)
