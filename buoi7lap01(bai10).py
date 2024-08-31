# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:19:31 2024

@author: LeThiLamThuong-23722951
"""

N = int(input("nhap bien so xe cua ban: "))
if 1000 <= N < 10000:
    a = N % 1000
    b = a % 100
    c = b % 10
    
    nut1 = N // 1000 + a // 100  + b // 10 + c % 10
    if 10 <= nut1 <= 100:
        nut2 = nut1 // 10 + nut1 % 10
        print("bien so xe cua ban co so nut la:",nut2)
    if nut1 < 10:
        print("bien so xe cua ban co so nut la:",nut1)
else:
    print("bien so khong hop le ( bien so chi co 4 chu so)")

