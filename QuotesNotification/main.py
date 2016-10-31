__author__ = 'Rupesh Choudhary'

import random
from time import sleep
from WindowsBalloonTip import balloon_tip

fw = open('quotes.txt', 'r')
vocab = fw.read()
vocab = vocab.split('\n')


def sendmessage(title, message):
    balloon_tip(title, message)
    return

while True:
    i = random.randint(0, 2002)
    if i % 2 == 0:
        if len(vocab[i]) < 118:
            sendmessage(vocab[i], vocab[i + 1])
            sleep(300)
        else:
            continue
    else:
        continue
