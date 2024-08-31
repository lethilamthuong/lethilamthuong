# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:12:50 2024

@author: LeThiLamThuong-23722951
"""

h = int(input("nhap gio: "))
m = int(input("nhap phut: "))
s = int(input("nhap giay: "))
if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
    print("gio, phut, giay hop le")
else:
    print("gio, phut, giay khong hop le")