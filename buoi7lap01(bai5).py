# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:34:21 2024

@author: LeThiLamThuong-23722951
"""

time_str = input("nhap vao gio,phut,giay theo dinh dang hh:mm:ss: ")
gio, phut, giay = map(int, time_str.split(':'))
if phut <= 60 and giay <= 60:
    tong_so_giay = gio * 3600 + phut * 60 + giay
else:
    tong_so_giay = "khong xac dinh"

print("tong so giay la:",tong_so_giay)
