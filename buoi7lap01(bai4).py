# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:29:05 2024

@author: LeThiLamThuong-23722951
"""

N = int(input("Nhập số nguyên dương N có 2 chữ số: "))
if 10 <= N <= 99:
  
    chu_so_don_vi = N % 10
    chu_so_chuc = N // 10
    tong = chu_so_chuc + chu_so_don_vi
else:
    tong = "khong xac dinh"
print("tong cac chu so cua N la:",chu_so_chuc,"+",chu_so_don_vi,"=",tong)