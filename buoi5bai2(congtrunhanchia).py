# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:18:35 2024

@author: Le Thi Lam Thuong-23722951
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
tong = a + b
hieu = a - b
tich =  a * b
if b != 0:
    thuong = a / b
    chia_lay_du = a % b
    chia_lay_nguyen = a // b
    thuong_lam_tron = round(thuong, 3)
    
else:
    thuong_lam_tron = "khong xac dinh"
    chia_lay_du = "khong xac dinh"
    chia_lay_nguyen = "khong xac dinh"
    
print("tong cua a va b la:",tong)
print("hieu cua a va b la:",hieu)
print("tich cua a va b la:",tich)
print("Thuong cua a và b la:", thuong_lam_tron)
print("Chia lay du cua a và b la:", chia_lay_du)
print("Chia lay nguyen cua a và b la:", chia_lay_nguyen)