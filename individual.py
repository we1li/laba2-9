#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def power_recursive(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power_recursive(x, abs(n))
    else:
        return x * power_recursive(x, n - 1)

if __name__ == '__main__':
    x = float(input("Введите значение x: "))
    n = int(input("Введите значение n: "))

    result = power_recursive(x, n)
    print("Результат:", result)
