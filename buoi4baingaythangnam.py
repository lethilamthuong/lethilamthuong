# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:08:36 2024

@author: LeThiLamThuong
"""

nhapvao= input("nhap vao ngay thang nam: ")
dd, mm, yyyy= map(int,nhapvao.split("/"))

if yyyy % 4 == 0 and yyyy % 100 !=0 or yyyy % 400 == 0:
    print("nam nhuan")
else:
    print("nam khong nhuan")
if mm == 4 or mm == 6 or mm ==9 or mm ==11:
    songaymax=30
if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    songaymax=31
if dd < 1 and dd > songaymax:
    False
if mm < 1 and mm > 12:
    False
    print("thoi gian nhap khong hop le")
else:
    print("thoi gian nhap hop le")
    