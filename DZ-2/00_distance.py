#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

msk = sites['Moscow']
lnd = sites['London']
prs = sites['Paris']

msk_lnd = ((msk[0] - lnd[0]) ** 2 + (msk[1] - lnd[1]) ** 2) ** .5
msk_prs = ((msk[0] - prs[0]) ** 2 + (msk[1] - prs[1]) ** 2) ** .5
prs_lnd = ((prs[0] - lnd[0]) ** 2 + (prs[1] - lnd[1]) ** 2) ** .5

distances['Moscow'] = {}
distances['Moscow']['London'] = msk_lnd
distances['Moscow']['Paris'] = msk_prs

distances['London'] = {}
distances['London']['Moscow'] = msk_lnd
distances['London']['Paris'] = prs_lnd

distances['Paris'] = {}
distances['Paris']['Moscow'] = msk_prs
distances['Paris']['London'] = prs_lnd

# TODO здесь заполнение словаря


pprint(distances)




