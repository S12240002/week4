# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

alphabets = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'E',
    'f': 'F',
    'g': 'G',
    'h': 'H',
    'i': 'I',
    'j': 'J',
    'k': 'K',
    'l': 'L',
    'm': 'M',
    'n': 'N',
    'o': 'O',
    'p': 'P',
    'q': 'Q',
    'r': 'R',
    's': 'S',
    't': 'T',
    'u': 'U',
    'v': 'V',
    'w': 'W',
    'x': 'X',
    'y': 'Y',
    'z': 'Z'
}

# 輸入小寫英文字母
user_input = input("請輸入小寫英文字母：")

# 將使用者輸入轉換為大寫
upper_case_str = "".join([alphabets.get(char, char) for char in user_input])

# 使用 print 函數顯示結果
print(upper_case_str)

