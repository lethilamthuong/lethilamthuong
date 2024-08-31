# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:18:51 2024

@author: LeThiLamThuong-23722951
"""

a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
tong = a + b
hieu = a - b
tich =  a * b
if b != 0:
    thuong = a / b
    thuong_lam_tron = round(thuong, 3)
else:
    thuong_lam_tron = "khong xac dinh"
print("tong cua a va b la:",tong)
print("hieu cua a va b la:",hieu)
print("tich cua a va b la:",tich)
print("Thuong cua a và b la:", thuong_lam_tron)