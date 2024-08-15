# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:25:35 2024

@author: Le
"""

import math
a = float (input("Nhap gia tri cua a:"))
b = float (input("Nhap gia tri cua b:"))
c = float (input("Nhap gia tri cua c:"))
if a == 0:
    if b == 0:
        if c == 0:
            print("phuong trinh co vo so nghiem.")
        else:
            print("phuong trinh vo nghiem.")
    else:
        x = -c/b
        print (f"nghiem cua phuong trinh la: x = {x}")
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math. sqrt(delta)) / (2 * a)
        print(f"phuong trinh co hai nghiem phan biet: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print (f"phuong trinh co nghiem kep: x = {x}")
    else:
        print("phuong trinh vo nghiem.")