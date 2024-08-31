# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:39:11 2024

@author: LeThiLamThuong-23722951
"""

A = input("nhap vao gio phut giay thu nhat theo dang hh/mm/ss: ")
B = input("nhap vao gio phut giay thu hai theo dang hh/mm/ss: ")
hh, mm, ss= map(int,A.split("/"))
HH, MM, SS= map(int,B.split("/"))
if 0 <= hh <=23 and 0 <= mm <= 59 and 0 <= ss <= 59 and 0 <= HH <=23 and 0 <= MM <= 59 and 0 <= SS <=59:
   T = (hh + HH)*3600+(mm + MM)*60+ss+SS
   gio1 = T // 3600
   phut1 = gio1 // 60
   giay1 = T % 60
   print("tong la:",gio1,"/",phut1,"/",giay1)
   H = (hh - HH)*3600+(mm - MM)*60+ss-SS
   gio2 = H // 3600
   phut2 = gio2 // 60
   giay2 = H % 60
   print("hieu cua gio thu nhat voi thu hai la:",gio2,"/",phut2,"/",giay2)
else:
    print("khong hop le")
   