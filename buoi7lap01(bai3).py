# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:24:57 2024

@author: LeThiLamThuong-23722951
"""

a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
if b != 0:
    chia_lay_du = a % b
    chia_lay_nguyen = a // b
else:
    chia_lay_du = "khong xac dinh"
    chia_lay_nguyen = "khong xac dinh"
print("Chia lay du cua a và b la:", chia_lay_du)
print("Chia lay nguyen cua a và b la:", chia_lay_nguyen)
    