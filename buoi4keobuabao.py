# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:50:23 2024

@author: LeThiLamThuong
"""
import random
luachon = ('keo', 'bua', 'bao')
nguoichoi = input("lua chon(keo-bua-bao)")
may = random.choice(luachon)
print(f"ban chon: {nguoichoi}")
print(f"may chon: {may}")
if nguoichoi == may:
    print("hoa")
elif may == "bua" and nguoichoi == "keo" or\
     may == "keo" and nguoichoi == "bao" or\
     may == "bao" and nguoichoi == "bua":
         print("may thang")
else:
    print("may thua")