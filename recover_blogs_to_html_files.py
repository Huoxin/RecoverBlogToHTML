#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import string
import time

def getlocation(list,str):
	if list[0].find(str) >= 0:
		return 1
	elif list[1].find(str) >= 0:
		return 2
	else:
		return 3


def get_id(line):
	list = line.split('":"')
        id = list[getlocation(list,"\"id")].split(',')[0].split('"')[0]
	return id

def get_title(line):
	list = line.split('":"')
	title = list[getlocation(list,"\"title")].split(',')[0].split('"')[0]
	return title

def get_body(line):
	list = line.split('\":')
	body = list[getlocation(list,"body")]
	return body

#except_cnt = 0
def get_blog_body_in_single_file_write_in_html(file_name):		
	f = open(file_name, 'r')
#	global except_cnt
	for line in f:				
		blog_id = get_id(line)
		blog_title = get_title(line)
		blog_body = get_body(line)
		blog_file_name = open('./HTML_RESULT/'+blog_id+'.html','a')
		
		#必须转成gb18030才能在HTML里正常显示 XD
		blog_body = blog_body[1:len(blog_body)-3]
		blog_body = blog_body.replace('\\/','/') #清除</\p>中的/
		blog_body = blog_body.replace('\\r\\n','') #清除\r\n
		blog_body = blog_body.replace('\\n','<br />') #清除\r\n
		blog_file_name.write('<h1>'+blog_title.decode('utf-8').encode('gb18030')+'</h1>')
		try:
			blog_file_name.write(blog_body.decode('utf-8').encode('gb18030'))
		except:
#			except_cnt = except_cnt+1
			blog_file_name.write(blog_body)
			blog_file_name.write(blog_body)
		blog_file_name.close()
	f.close()


starttime = time.time()
allfiles = os.listdir('./blog.m/')
for  s_file in allfiles:
	get_blog_body_in_single_file_write_in_html('./blog.m/'+s_file)		

#print except_cnt
