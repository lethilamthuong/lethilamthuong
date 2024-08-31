# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:04:23 2024

@author: Lethilamthuong-23722951
"""

a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
c = int(input("Nhap so nguyen c: "))
d = int(input("Nhap so nguyen d: "))
so_min = a
if b < a:
    so_min = b
if c < so_min:
    so_min = c
if d < so_min:
    so_min = d
print("so nguyen be nhat la:",so_min)
    
    


    
    
    
        
        