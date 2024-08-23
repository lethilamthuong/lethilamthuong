# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:32:45 2024

@author: LeThiLamThuong-
"""

import random
def random_number(start, end):
  return random.randint(start, end)
a = int(input("Nhap so nho nhat : "))
b = int(input("Nhap so lon nhat : "))
print("Số ngẫu nhiên:", random_number(a, b))