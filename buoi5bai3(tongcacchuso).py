# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:41:39 2024

@author: Le Thi Lam Thuong-23722951
"""

N = int(input("Nhập số nguyên dương N có 2 chữ số: "))
if 10 <= N <= 99:
  
    chu_so_don_vi = N % 10
    chu_so_chuc = N // 10
    tong = chu_so_chuc + chu_so_don_vi
print("tong cac chu so cua N la:",tong)
