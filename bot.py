import sys
import time
import random
import datetime
import telepot
import subprocess

def handle(msg):
	chat_ids = msg['chat']['id']
	command = msg['text']
	chat_id ='YOURCHATID'
	
	print 'Command received: %s' % command
		
	if command == 'Enable VNC server':
		risp=subprocess.check_output("vncserver", shell=True)
		bot.sendMessage(chat_id, 'Fatto.')
	elif command == 'Disable VNC server':
		subprocess.check_output("vncserver -kill :1", shell=True)
		bot.sendMessage(chat_id, 'Fatto.')
	elif command == '/start':
		bot.sendMessage(chat_ids, 'This bot responds only to its owner.')
	elif command == 'Time':
		bot.sendMessage(chat_id, str(datetime.datetime.now()))
	elif (command == 'Help' or command == 'help'):
		bot.sendMessage(chat_id, 'Text me one of the following commands:')
		bot.sendMessage(chat_id, 'Time')
		bot.sendMessage(chat_id, 'Uptime')
		bot.sendMessage(chat_id, 'Free ram')
		bot.sendMessage(chat_id, 'Free ram 2')
		bot.sendMessage(chat_id, 'Free space')
		bot.sendMessage(chat_id, 'Enable/Disable VNC server')
		bot.sendMessage(chat_id, 'Enable/Disable test2 dir')
		bot.sendMessage(chat_id, 'Command X (executes X command in linux shell and returns output)')
		bot.sendMessage(chat_id, 'Commands X && Y && ... (executes independents comands and returns output)')
		bot.sendMessage(chat_id, 'Commands X & Y & ... (executes dependents comands and returns output)')
		bot.sendMessage(chat_id, '!! X && Y ... (executes independents comands and returns output)')
		bot.sendMessage(chat_id, '!! X & Y ... (executes dependents comands and returns output)')
		bot.sendMessage(chat_id, 'Reboot')
	if (a.find('Command')==0 and a.find('reboot')==-1):
		a=a.replace('Command ','')
		bot.sendMessage(chat_id, 'Eseguo...')
		risp=subprocess.check_output(a, shell=True)
		bot.sendMessage(chat_id, risp)
	elif (a.find('Commands')==0 and a.find('reboot')==-1):
		a=a.replace('Commands ','')
		bot.sendMessage(chat_id, 'Running...')
		risp=subprocess.check_output(a, shell=True)
		bot.sendMessage(chat_id, risp)
	elif (a.find('!!')==0 and a.find('reboot')==-1):
		a=a.replace('!!','')
		bot.sendMessage(chat_id, 'Running...')
		risp=subprocess.check_output(a, shell=True)
		bot.sendMessage(chat_id, risp)
	elif command == 'Enable test2 dir':
		risp=subprocess.check_output("sudo chmod 777 /var/www/test2", shell=True)
		bot.sendMessage(chat_id, 'Fatto.')
	elif command == 'Disable test2 dir':
		risp=subprocess.check_output("sudo chmod 000 /var/www/test2", shell=True)
		bot.sendMessage(chat_id, 'Fatto.')
	elif command == 'Free ram 2':
		risp=subprocess.check_output("free -h", shell=True)
		bot.sendMessage(chat_id, risp)
	elif command == 'Free ram 2':
		risp=subprocess.check_output("vmstat -s", shell=True)
		bot.sendMessage(chat_id, risp)
	elif command == 'Free space':
		risp=subprocess.check_output("df -H", shell=True)
		bot.sendMessage(chat_id, risp)
	elif command == 'Uptime':
		risp=subprocess.check_output("uptime", shell=True)
		bot.sendMessage(chat_id, risp)
	elif command == 'Riavvia':
		bot.sendMessage(chat_id, 'Rebooting...')
		risp=subprocess.check_output("sudo reboot", shell=True)
	else:
		if chat_ids != chat_id:
			bot.sendMessage(chat_ids, 'Error. Please retry.')

bot = telepot.Bot('TOKEN')
bot.notifyOnMessage(handle)
print 'Listening...'
limon93='YOURCHATID'
bot.sendMessage(limon93,'Server booted, ready to go!')
while 1:
    time.sleep(10)
