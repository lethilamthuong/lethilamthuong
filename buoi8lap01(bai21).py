# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:36:22 2024

@author: LeThiLamThuong-23722951
"""

a = int(input("Nhap so nguyen bat ky: "))
so_chu = {0: "Khong", 1: "Mot", 2: "Hai", 3: "Ba", 4: "Bon", 5: "Nam", 6: "Sau", 7: "Bay", 8: "Tam", 9: "Chin"}
if 0 <= a <= 9:
    print("gia tri cua so nguyen la:",so_chu[a])
else:
    print("khong doc duoc")
    

