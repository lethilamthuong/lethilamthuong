# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:04:08 2024

@author: LeThiLamThuong-23722951
"""

h = float(input("nhap vao chieu cao cua ban(m): "))
m = float(input("nhap vao can nang cua ban(kg): "))
if h > 0 and m > 0: 
    BMI = m / ( h**2 )
else:
    BMI = "khong xac dinh"
print("chi so BMI la:",BMI)