# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:18:40 2024

@author: BAO KHANH
"""

s="Đại học Quốc gia, Khu phố 6 P. Linh Trung, C. Thủ Đức, Tp. HCM"

s1 = s.split(", ")
for i in s1:
    print(i)
s2=s.replace("P. ,").replace("@. ", ""). replace( "Tp. ", "").split(",")
for u in s2:
    print (u)