#!/usr/bin/python2
# -*- coding: utf-8 -*-
# @Time    : 1/11/21 5:00 PM
# @Author  : 0xFE
# Using for :merge two sorted list

def merge(l1, l2):
    res = []
    i = 0
    j = 0
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            i += 1
            res.append(l1[0])
            del l1[0]

        else:
            j += 1
            res.append(l2[0])
            del l2[0]

    res = res + l1
    res = res + l2
    return res


print merge([1, 5, 8], [2, 4, 6, 7])
