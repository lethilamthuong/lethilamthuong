# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:55:50 2024

@author: LeThiLamThuong-23722951
"""
import math
R = float(input("nhap ban kinh cua duong tron:R= "))
if R > 0:
    C = 2 * math.pi * R
    S = math.pi * R**2
else:
    C = V = "Khong xac dinh"
print("chu vi cua hinh tron la:",C)
print("dien tich cua hinh tron la:",S)