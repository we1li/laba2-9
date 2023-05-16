#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def combinations(m, n):
    # базовый случай
    if m == 0 or m == n:
        return 1
    # рекурсивный случай
    return combinations(m, n-1) + combinations(m-1, n-1)


if __name__ == '__main__':
    m = 4
    n = 8
    result = combinations(m, n)
    print(f"Число сочетаний из {n} по {m} равно {result}")
