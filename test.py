#!/usr/bin/env python
# coding: utf-8
#
import schedule
import time
from wxbot import *

class MyWXBot(WXBot):
	def handle_msg_all(self, msg):
		 if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
		     print 1
			#self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
			#self.send_file_msg_by_uid("img/1.png", msg['user']['id'])

	# def schedule(self):
	# 	self.send_msg(u'张三', u'测试')
	# 	time.sleep(1)

def send_group_info(WXBot):
	print 'hello world'
	WXBot.send_group_info()

def main():
	bot = MyWXBot()
	bot.DEBUG = True
	bot.conf['qr'] = 'tty'
	bot.script_run()


if __name__ == '__main__':
	main()
