# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:36:11 2024

@author: Lethilamthuog-23722951
"""

a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
c = int(input("Nhap so nguyen c: "))
so_max = a
if b > so_max:
    so_max = b
if c > so_max:
    so_max = c
print("so lon nhat la:",so_max)