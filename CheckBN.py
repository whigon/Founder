# -*- coding: utf-8 -*-

# 检查BN
def check(str_bn, bn):
    str = str_bn[3:]

    if str == '':
        return 0

    if str == bn:
        return 1
    else:
        return -1
