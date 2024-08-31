# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:58:53 2024

@author: LeThiLamThuong-23722951
"""

a = int(input("Nhap ngay: "))
b = int(input("Nhap thang: "))
c = int(input("Nhap nam: "))
if 1 <= a <= 31 and 1 <= b <= 12:
    #a
    print(a,"/",b,"/",c)
    #b
    t = c%100 
    if t < 10:
        t= 10 + t
    print(a,"/",b,"/",t)
    #c
    print(c,"/",b,"/",a)