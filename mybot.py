import agobo
import sys
import time
import random
import datetime
import telepot
import os

"""
A simple bot that accepts two commands:
- /roll : reply with a random integer between 1 and 6, like rolling a dice.
- /time : reply with the current time, like a clock.
- /go
INSERT TOKEN below in the code, and run:
$ python diceyclock.py
Ctrl-C to kill.
"""
speed = 80
agobo.init()
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command
    if command == '/rolldoris':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/go':
        agobo.forward(speed)
        bot.sendMessage(chat_id, str('going forward'))
    elif command == '/stop':
        agobo.stop()
        bot.sendMessage(chat_id, str('stopped'))
    elif command == '/back':
        agobo.reverse(speed)
        bot.sendMessage(chat_id, str('going backward'))
    elif command == '/play':
        os.system("omxplayer example.mp3")

bot = telepot.Bot('200791253:AAHtxaLnAmV9T8OI6Br8VcpxSwQPBhDZLpA')
bot.message_loop(handle)
print 'I am listening ...'
while 1:
    time.sleep(10)
