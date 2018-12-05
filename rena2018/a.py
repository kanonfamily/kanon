# -*- coding:utf-8 -*-
from linepy import *
from akad.ttypes import Message
import json, time, random, tempfile, os, sys, urllib, threading, codecs, datetime, socket

reload(sys)
sys.setdefaultencoding('utf-8')

client = LineClient(id = "", passwd = "")



tracer = LinePoll(client)
profile = client.getProfile()
channel = LineChannel(client)
#print "http://line.me/ti/p/%s" % client._client.reissueUserTicket(0,3)

BOT = [client]

bots = [profile.mid]

def te(text):
    try:
        b = text.encode("hex")
        a = b.encode("base64")
        s = a.encode("hex")
        g = s.encode("base64")
        return g.replace("\n","")
    except Exception as e:
        print e

def td(text):
    try:
        b = text.decode("base64")
        a = b.decode("hex")
        s = a.decode("base64")
        g = s.decode("hex")
        return g
    except Exception as e:
        print e


tran = {
    "gim" : False,
    "post" : [],
    "BL" : {},
    "mut" : {},
    "ab" : True,
    "db" : False
}

_pro = {
    'PI' : {},  #画像保護
    'PK' : {},  #蹴り保護
    'PN' : {},  #名前保護
    'PU' : {},  #URL保護
    'PA' : {},  #招待保護
}


_set = {
    "havePs" : [],
}


haveP = []
xx=open('op.ad','r').read()
xt=xx.split('\n')
for aa in xt:
    try:
        if aa == "":
            pass
        else:
            haveP.append(aa)
    except Exception as er:
        print er
        pass


master = [""]




print "\n\n############################    Done    ############################ "


def ADDF(op):
    try:
        client.findAndAddContactsByMid(op.param1)
        client.sendText(op.param1, "追加ありがとう")
        time.sleep(0.5)
    except Exception as e:
        print e

tracer.addOpInterrupt(5, ADDF)


def autocomment():
    lastpostid = []
    while True:
        time.sleep(0.1)
        try:
            home_id = channel.getFeed(postLimit=10, commentLimit=1, likeLimit=1, order='TIME')["result"]["feeds"][0]["post"]["postInfo"]["homeId"]
            post_id = channel.getFeed(postLimit=10, commentLimit=1, likeLimit=1, order='TIME')["result"]["feeds"][0]["post"]["postInfo"]["postId"]
            if post_id in lastpostid:
                pass
            elif home_id not in user:
                pass
            else:
                try:
                    channel.like(home_id, post_id, likeType=1001)
                except:
                    pass
                
                lastpostid.append(post_id)
                if len(lastpostid) > 128:
                    del lastpostid[0:3]
                else:
                    pass
        except:
            pass
b=threading.Thread(target=autocomment)
b.setDaemon(True)
b.start()

while True:
    user = master + _set["havePs"]
    tracer.trace()