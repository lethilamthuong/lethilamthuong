# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:11:26 2024

@author: Lenovo
"""

nhapvao= input("nhap vao gio phut giay theo dang hh/mm/ss: ")
hh, mm, ss= map(int,nhapvao.split("/"))
if 0 <= hh <=24 and 0 <= mm <= 60 and 0 <= ss <=60:
    so_giay = hh * 3600 + mm * 60 + ss
    print("so giay la:",so_giay)
else:
    print("vui long nhap lai gio phut giay theo dinh dang")
    