#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf8

# Загружаем файл с кодировкай utf8
import codecs

f=open('./keyboard.conf','r',1,'utf-8','ignore')
# codecs.decode(
#         f,
#         'utf8',
#         'ignore'
#     )
# codecs.encode(f,'cp1251','ignore')
lines = f.readlines()
for l in lines:
    print(l)