# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:32:04 2024

@author: LeThiLamThuong
"""

so_km = float(input("Nhap so km di chuyen: "))
if so_km <= 1:
    tong_tien = so_km * 20000
elif so_km <= 3:
    tong_tien = so_km * 13000
elif so_km <= 8:
    tong_tien = 3 * 13000 + (so_km - 3) * 12000
else:
    tong_tien = 3 * 13000 + 5 * 12000 + (so_km-8) * 10000

if tong_tien > 100000:
    tong_tien = 0.92 * tong_tien
    
print("Tong so tien phai tra:", tong_tien, "dong")