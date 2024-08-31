# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:02:00 2024

@author: Lenovo
"""

a = float(input("nhap gia tri cua he so a: "))
b = float(input("nhap gia tri cua he so b: "))
c = float(input("nhap gia tri cua he so c: "))
if a == 0:
    if b == 0:
        print("phuong trinh co vo so nghiem")
    else:
        print("phuong trinh vo nghiem")
else: 
    delta = b**2 - 4*a*c
    if delta == 0:
        x = -b/(2*a)
        print("phuong trinh co nghiem kep la:",x)
    if delta > 0:
        x1 = (-b - (delta ** 2)) / (2*a)
        x2 = (-b + (delta ** 2)) / (2*a)
        print("phuong trinh co 2 nghiem phan biet x1=",x1,", x2=",x2)
    else:
        print("phuong trinh vo nghiem")