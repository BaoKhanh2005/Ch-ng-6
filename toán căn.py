# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:02:10 2024

@author: BAO KHANH
"""

import math 
a= float(input("Nhập số a= "))
b= float(input("Nhập số b= "))
A= ((math.pow(a, 1/2)-math.pow(b, 1/2))/(math.pow(a, 1/4)-math.pow(b, 1/4)))-((math.pow(a, 1/2)+math.pow(a*b, 1/4))/(math.pow(a, 1/4)+math.pow(b,1/4)))
print("Kết quả là: ",A)