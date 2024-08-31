# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:17:55 2024

@author: LeThiLamThuong-23722951
"""

hinh = int(input("nhap so de chon hinh(1-vuong, 2-chu nhat, 3-tron): "))
if hinh == 1:
    a = float(input("nhap canh cua hinh vuong: "))
    c = 2 * a
    s = a**2
    print("dien tich la:",s,", chu vi la:",c)
if hinh == 2:
    dai = float(input("nhap chieu dai HCN: "))
    rong = float(input("nhap chieu rong HCN: "))
    c = (dai + rong) * 2
    s = dai * rong
    print("dien tich la:",s,"chu vi la:",c)
if hinh == 3:
    r = float(input("nhap ban kinh hinh tron: "))
    c = 2 * 3.14 * r
    s = 3.14 *( r**2 )
    print("dien tich la:",s,"chu vi la:",c)
    
    