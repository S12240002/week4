# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:56:46 2024

@author: Student
"""

import random

n = int(input("請輸入 n："))
a = int(input("請輸入 a："))
b = int(input("請輸入 b："))

numbers = []
for _ in range(n):
  numbers.append(random.randint(a, b))

numbers = list(set(numbers))

numbers.sort(reverse=True)

print(numbers)