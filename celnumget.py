#!/usr/bin/python2
# coding:utf-8
#
# Coletar numeros de celular em postagens no facebook
#
# ins3c7, 24 out 2016
#

import time, os, random, re
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

os.system('clear')

bro = webdriver.Chrome()
bro.set_window_size(1090,1050)
bro.set_window_position(830, 30)
bro.get('http://www.facebook.com/')

soup = bs(bro.page_source, "html.parser")

numeros=[]

for tel in soup.findAll('span', attrs= {'class':'UFICommentBody'}):
  num = ''.join(re.findall(r'\d+', tel.text))
    if len(num) > 8 and len(num) < 13:
      numeros.append(num)

with open('agenda.txt', 'a') as f:
	for n in numeros:
		f.write('BEGIN:VCARD\n')
		f.write('VERSION:2.1\n')
		f.write('N:;@@'+ str(n) +';;;\n')
		f.write('FN:Jeferson\n')
		f.write('TEL;CELL:'+ str(n) +'\n')
		f.write('TEL;CELL:'+ str(n) +'\n')
