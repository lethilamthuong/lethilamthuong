# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:50:05 2024

@author: LeThiLamThuong-23722951
"""

a = float(input("nhap gia tri cua he so a: "))
b = float(input("nhap gia tri cua he so b: "))
if a == 0:
    if b == 0:
        print("phuong trinh co vo so nghiem")
    else:
        print("phuong trinh vo nghiem")
else:
    x= -b/a
    print("phuong trinh co nghiem la x=",x)