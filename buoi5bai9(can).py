# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:01:31 2024

@author: Le Thi Lam Thuong-23722951
"""
import math
a = int(input("nhap gia tri cua a: "))
b = int(input("nhap gia tri cua b: "))
if a > 0 and b > 0 and a !=b :
    A = (math.pow(a, 0.5)-math.pow(b, 0.5))/(math.pow(a, 0.25)-math.pow(b, 0.25))-(math.pow(a, 0.5)+math.pow(a*b, 0.25))/(math.pow(a, 0.25)+math.pow(b, 0.25))
    print("ket qua cua bieu thuc A la:",A)
else:
    print("khong xac dinh")
    