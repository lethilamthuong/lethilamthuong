# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:52:16 2024

@author: LeThiLamThuong-23722951
"""


#a
a = float(input("Nhap so nguyen a: "))
b = float(input("Nhap so nguyen b: "))
c = float(input("Nhap so nguyen c: "))
so_max = max(a,b,c)
so_min = min(a,b,c)
d = a + b + c - so_max - so_min
print("sap xep theo thu tu tang dan:",so_min,",",d,",",so_max)


#b
N = input("nhap mot so nguyen: ")

if N.isdigit():
    digits = list(N)
    digits.sort()
    sorted_number_str = ''.join(digits)
    print("so sau khi sap xep theo thu tu tang dan la:",sorted_number_str )
else:
    print("so khong hop le")