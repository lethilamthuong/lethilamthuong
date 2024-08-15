# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:27:44 2024

@author: LeThiLamThuong
"""

import math
a = float(input("Nhap do dai canh a: "))
b = float(input("Nhap do dai canh b: "))
c = float(input("Nhap do dai canh c: "))
def kiem_tra_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

def phan_loai_tam_giac(a, b, c):
    if not kiem_tra_tam_giac(a, b, c):
        return "Khong phai la tam giac"
    
    if a == b == c:
        return "Tam giac đeu"
    elif a == b or a == c or b == c:
        if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
            return "Tam giac vuong can"
        else:
            return "Tam giac can"
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        return "Tam giac vuong"
    else:
        return "Tam giac thuong"
loai_tam_giac = phan_loai_tam_giac(a, b, c)
print(loai_tam_giac)