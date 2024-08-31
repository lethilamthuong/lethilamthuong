# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:06:00 2024

@author: Lethilamthuong-23722951
"""

import math
a = float(input("nhap gia tri cua a: "))
b = float(input("nhap gia tri cua b: "))
if a != b:
    A = math.pow(a,1/3)
    B = math.pow(b,1/3)
    C = ((a + b) / (A + B) -(A*B)) / ((A-B)**2)
    print("bieu thuc co gia tri la:",C)
else: 
    print("bieu thuc khong xac dinh")