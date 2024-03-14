# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:45:54 2024

@author: Student
"""

import random

# 建立撲克牌
spades = ['01♠', '02♠', '03♠', '04♠', '05♠', '06♠', '07♠', '08♠', '09♠', '10♠', '11♠', '12♠', '13♠']
hearts = ['01♥', '02♥', '03♥', '04♥', '05♥', '06♥', '07♥', '08♥', '09♥', '10♥', '11♥', '12♥', '13♥']
diamonds = ['01♦', '02♦', '03♦', '04♦', '05♦', '06♦', '07♦', '08♦', '09♦', '10♦', '11♦', '12♦', '13♦']
clubs = ['01♣', '02♣', '03♣', '04♣', '05♣', '06♣', '07♣', '08♣', '09♣', '10♣', '11♣', '12♣', '13♣']
poker = spades + hearts + diamonds + clubs

# 洗牌
random.shuffle(poker)

# 發牌
players = [[] for _ in range(4)]
for _ in range(13):
  for i in range(4):
    players[i].append(poker.pop())

# 整理牌
for player in players:
  print(player)
  player.sort()

print(players)
# 輸出結果
for i in range(4):
  print(f"玩家 {i + 1}：")
  for card in players[i]:
    print(card)