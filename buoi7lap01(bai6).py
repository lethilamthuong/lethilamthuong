# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:54:15 2024

@author: LeThiLamThuong-23722951
"""

N = int(input("nhap nam sinh: "))
if 0 <= N <= 202:
    tuoi = 2022 - N
print("so tuoi cua ban la:",tuoi)