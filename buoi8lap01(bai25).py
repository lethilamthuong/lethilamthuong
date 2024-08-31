# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:18:26 2024

@author: LeThiLamThuong-23722951
"""

a = input("nhap 1 chu cai: ")
if a.islower():
    b = a.upper()
    print("chu cai sau khi doi la:",b)
if  a.isupper():
    b = a.lower()
    print("chu cai sau khi doi la:",b)