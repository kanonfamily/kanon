# -*- coding:utf-8 -*-
from linepy import *
from akad.ttypes import Message
import json, time, random, tempfile, os, sys, urllib, threading, codecs, datetime, socket

reload(sys)
sys.setdefaultencoding('utf-8')

client = LineClient(id = "", passwd = "")
kicker1 = LineClient(id = "", passwd = "")
kicker2 = LineClient(id = "", passwd = "")
kicker3 = LineClient(id = "", passwd = "")
kicker4 = LineClient(id = "", passwd = "")
kicker5 = LineClient(id = "", passwd = "") 


tracer = LinePoll(client)
profile = client.getProfile() ; profile_1 = kicker1.getProfile()
profile_2 = kicker2.getProfile() ; profile_3 = kicker3.getProfile()
profile_4 = kicker4.getProfile() ; profile_5 = kicker5.getProfile()

channel = LineChannel(client) ; channel_1 = LineChannel(kicker1)
channel_2 = LineChannel(kicker2) ; channel_3 = LineChannel(kicker3)
channel_4 = LineChannel(kicker4) ; channel_5 = LineChannel(kicker5)
#print "http://line.me/ti/p/%s" % client._client.reissueUserTicket(0,3)

BOT = [client, kicker1, kicker2, kicker3, kicker4, kicker5]

bots = [profile.mid, profile_1.mid, profile_2.mid, profile_3.mid, profile_4.mid, profile_5.mid]

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

_set["havePs"] = haveP


f=codecs.open('mut.json','r','utf-8')
tran["mut"] = json.load(f)

f=codecs.open('bl.json','r','utf-8')
tran["BL"] = json.load(f)

f=codecs.open('po.json','r','utf-8')
tran["post"] = json.load(f)

f = codecs.open('inv.json','r','utf-8')
_pro["PA"] = json.load(f)

f = codecs.open('url.json','r','utf-8')
_pro["PU"] = json.load(f)

f = codecs.open('name.json','r','utf-8')
_pro["PN"] = json.load(f)

f = codecs.open('kick.json','r','utf-8')
_pro["PK"] = json.load(f)

f = codecs.open('image.json','r','utf-8')
_pro["PI"] = json.load(f)

gname = {}
gname = _pro["PN"]

master = ["u31ad96d62d0ac545338782d4f7f6cf6b"]




print "\n\n############################    Done    ############################ "

def PRO(op):
    try:

        if op.param2 in BOT:
            pass

        else:
            if op.param3 == "1":

                def np():
                    del _pro['PN'][op.param1]
                    f=codecs.open('name.json','w','utf-8')
                    json.dump(_pro["PN"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    _pro['PN'][op.param1] = client.getGroup(op.param1).name
                    f=codecs.open('name.json','w','utf-8')
                    json.dump(_pro["PN"], f, sort_keys=True, indent=4,ensure_ascii=False)

                if op.param1 in _pro['PN']:
                    if op.param2 in bots:
                        np()
                    elif op.param2 in user:
                        np()
                    else:
                        G = client.getGroup(op.param1)
                        G.name = gname[op.param1]
                        client.updateGroup(G)
                        botr = random.choice(BOT)
                        botr.sendText(op.param1, "名前の変更は禁止されているんだよ！？")
                        botr.kickoutFromGroup(op.param1, [op.param2])

            if op.param3 == "2":
                def ip():
                    del _pro['PI'][op.param1]
                    f=codecs.open('image.json','w','utf-8')
                    json.dump(_pro["PI"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    os.remove("image\\gp\\" + op.param1 + '.png')
                    group = client.getGroup(op.param1)
                    url = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    urllib.urlretrieve(url, "image\\gp\\" + op.param1 + ".png")
                    _pro['PI'][op.param1] = True
                    f=codecs.open('image.json','w','utf-8')
                    json.dump(_pro["PI"], f, sort_keys=True, indent=4,ensure_ascii=False)


                if op.param1 in _pro['PI']:
                    if op.param2 in bots:
                        ip()
                    elif op.param2 in user:
                        ip()
                    else:
                        botr = random.choice(BOT)
                        botr.updateGroupPicture(op.param1, "image\\gp\\" + op.param1 + '.png')
                        botr.sendText(op.param1, "画像の変更は禁止されているんだよ！？")
                        botr.kickoutFromGroup(op.param1, [op.param2])

            if op.param3 == "4":
                if op.param1 in _pro['PU']:
                    botr = random.choice(BOT)
                    if op.param2 in bots:
                        pass
                    elif op.param2 in user:
                        pass
                    else:
                        G = client.getGroup(op.param1)
                        if G.preventJoinByTicket == True:
                            pass
                        else:               
                            G.preventJoinByTicket = True
                            botr.updateGroup(G)
                        botr.kickoutFromGroup(op.param1, [op.param2])


    except Exception as e:
        print e
tracer.addOpInterrupt(11,PRO)

def ACP(op):
    try:

        if client.getProfile().mid in op.param3:
            if op.param2 in user:
                client.acceptGroupInvitation(op.param1)
                G = client.getGroup(op.param1)
                if G.preventJoinByTicket == False:
                    pass
                else:
                    G.preventJoinByTicket = False
                    client.updateGroup(G)
                Ti = client.reissueGroupTicket(op.param1)
                for _bot in [kicker1, kicker2, kicker3, kicker4, kicker5]:
                    _bot.acceptGroupInvitationByTicket(op.param1, Ti)
                we = random.choice([client, kicker1, kicker2, kicker3, kicker4, kicker5])
                if G.preventJoinByTicket == True:
                    pass
                else:
                    G.preventJoinByTicket = True
                    we.updateGroup(G)

                _mid = "NGU3YTU1N2E0ZDdhNGQ3ODRlNmE0NTMyNGU0NDRkMzU0ZDdhNTkzMjRlNDQ0ZDMyNGQ3YTQ5MzI0ZTQ0NGQ3NzRlNmE0NTMyNGQ3YTRkMzE0ZDdhNTE3YTRlNTQ0ZDdhNGQ3YTRkN2E0ZjQ0NGQzMzRkN2E2NzdhNGQ2YTU5MzA0ZDdhNTEzMjRlNmE0ZDMzNGU2YTU5N2EwYTRlNmE1OTdhNGU2YTU5N2E0ZTZhNTk3OTBh"
                client.sendText(op.param1, "招待ありがとう！\nレナたんを使用するには、licenseが必要だよ...ごめんね\n作者から購入してね！")
                time.sleep(0.5)
                client.sendContact(op.param1, td(_mid))
                time.sleep(0.5)
                client.sendText(op.param1, "↑作者だよ！\n困ったこととか、用事がある人、仲良くしたい人は追加してね！")

            else:
                client.rejectGroupInvitation(op.param1)

        if op.param3 in tran['BL']:
            if op.param2 in BOT:
                pass
            elif op.param2 in user:
                client.sendText(op.param1, u'招待中にブラックリストユーザーがいます\n気を付けてください。')
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                for ca in InviterX:
                    bot=random.choice(BOT)
                    bot2=random.choice(BOT)
                    try:
                        bot.cancelGroupInvitation(op.param1, [ca])
                        time.sleep(0.5)
                    except:
                        try:
                            bot2.cancelGroupInvitation(op.param1, [ca])
                            time.sleep(0.5)
                        except:
                            pass

        if op.param1 in _pro['PA']:
            if op.param2 in user:
                pass
            elif op.param2 in BOT:
                pass
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                for ca in InviterX:
                    bot=random.choice(BOT)
                    bot2=random.choice(BOT)
                    try:
                        bot.cancelGroupInvitation(op.param1, [ca])
                        time.sleep(0.5)
                    except:
                        try:
                            bot2.cancelGroupInvitation(op.param1, [ca])
                            time.sleep(0.5)
                        except:
                            pass
                botr = random.choice(BOT)
                botr.sendText(op.param1, '現在招待は禁止されているんだよ！？')
                botr.kickoutFromGroup(op.param1, [op.param2])

    except Exception as e:
        print e

tracer.addOpInterrupt(13, ACP)


def ADDF(op):
    try:
        _mid = "NGU3YTU1N2E0ZDdhNGQ3ODRlNmE0NTMyNGU0NDRkMzU0ZDdhNTkzMjRlNDQ0ZDMyNGQ3YTQ5MzI0ZTQ0NGQ3NzRlNmE0NTMyNGQ3YTRkMzE0ZDdhNTE3YTRlNTQ0ZDdhNGQ3YTRkN2E0ZjQ0NGQzMzRkN2E2NzdhNGQ2YTU5MzA0ZDdhNTEzMjRlNmE0ZDMzNGU2YTU5N2EwYTRlNmE1OTdhNGU2YTU5N2E0ZTZhNTk3OTBh"
        client.findAndAddContactsByMid(op.param1)
        client.sendText(op.param1, "追加ありがとう！\nレナたんを使用するには、licenseが必要だよ...ごめんね\n作者から購入してね！")
        time.sleep(0.5)
        client.sendContact(op.param1, td(_mid))
        time.sleep(0.5)
        client.sendText(op.param1, "↑作者だよ！\n困ったこととか、用事がある人、仲良くしたい人は追加してね！")
    except Exception as e:
        print e

tracer.addOpInterrupt(5, ADDF)



def KICK(op):
    try:
        if op.param3 in profile.mid:
            def clientK():
                bot = random.choice([kicker1, kicker2, kicker3, kicker4, kicker5])
                G = bot.getGroup(op.param1)
                if G.preventJoinByTicket == False:
                    Ticket = bot.reissueGroupTicket(op.param1)
                    client.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    bot.updateGroup(G)
                else:
                    G.preventJoinByTicket = False
                    bot.updateGroup(G)
                    Ticket = bot.reissueGroupTicket(op.param1)
                    client.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    bot.updateGroup(G)
            if op.param2 in user:
                clientK()
            elif op.param2 in bots:
                clientK()
            else:
                bot = random.choice([kicker1, kicker2, kicker3, kicker4, kicker5])
                g = bot.getGroup(op.param1)
                if g.preventJoinByTicket == False:
                    Ticket = bot.reissueGroupTicket(op.param1)
                    client.acceptGroupInvitationByTicket(op.param1,Ticket)
                    g.preventJoinByTicket = True
                    bot.updateGroup(g)
                else:
                    g.preventJoinByTicket = False
                    bot.updateGroup(g)
                    Ticket = bot.reissueGroupTicket(op.param1)
                    client.acceptGroupInvitationByTicket(op.param1,Ticket)
                    g.preventJoinByTicket = True
                    bot.updateGroup(g)
                bot.kickoutFromGroup(op.param1, [op.param2])
                if op.param2 in tran["BL"]:
                    pass
                else:
                    tran["BL"][op.param2] = True
                    f=codecs.open('bl.json','w','utf-8')
                    json.dump(tran["BL"], f, sort_keys=True, indent=4,ensure_ascii=False)

        """##############################################################################"""

        if op.param3 in profile_1.mid:
            def K1():
                bot = random.choice([kicker2, kicker3, kicker4, kicker5])
                G = bot.getGroup(op.param1)
                if G.preventJoinByTicket == False:
                    Ticket = bot.reissueGroupTicket(op.param1)
                    kicker1.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    bot.updateGroup(G)
                else:
                    G.preventJoinByTicket = False
                    bot.updateGroup(G)
                    Ticket = bot.reissueGroupTicket(op.param1)
                    kicker1.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    bot.updateGroup(G)
            if op.param2 in user:
                K1()
            elif op.param2 in bots:
                K1()
            else:
                try:
                    kicker2.kickoutFromGroup(op.param1, [op.param2])
                    G = kicker2.getGroup(op.param1)
                    if G.preventJoinByTicket == True:
                        G.preventJoinByTicket = False
                        kicker2.updateGroup(G)
                    Ticket = kicker2.reissueGroupTicket(op.param1)
                    kicker1.acceptGroupInvitationByTicket(op.param1, Ticket)
                    G.preventJoinByTicket = True
                    kicker2.updateGroup(G)
                except:
                    try:
                        kicker3.kickoutFromGroup(op.param1, [op.param2])
                        G = kicker3.getGroup(op.param1)
                        if G.preventJoinByTicket == True:
                            G.preventJoinByTicket = False
                            kicker3.updateGroup(G)
                        Ticket = kicker3.reissueGroupTicket(op.param1)
                        kicker1.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kicker3.updateGroup(G)
                    except:
                        try:
                            kicker4.kickoutFromGroup(op.param1, [op.param2])
                            G = kicker4.getGroup(op.param1)
                            if G.preventJoinByTicket == True:
                                G.preventJoinByTicket = False
                                kicker4.updateGroup(G)
                            Ticket = kicker4.reissueGroupTicket(op.param1)
                            kicker1.acceptGroupInvitationByTicket(op.param1, Ticket)
                            G.preventJoinByTicket = True
                            kicker4.updateGroup(G)
                        except:
                            try:
                                kicker5.kickoutFromGroup(op.param1, [op.param2])
                                G = kicker5.getGroup(op.param1)
                                if G.preventJoinByTicket == True:
                                    G.preventJoinByTicket = False
                                    kicker5.updateGroup(G)
                                Ticket = kicker5.reissueGroupTicket(op.param1)
                                kicker1.acceptGroupInvitationByTicket(op.param1, Ticket)
                                G.preventJoinByTicket = True
                                kicker5.updateGroup(G)
                            except:
                                pass
                if op.param2 in tran["BL"]:
                    pass
                else:
                    tran["BL"][op.param2] = True
                    f=codecs.open('bl.json','w','utf-8')
                    json.dump(tran["BL"], f, sort_keys=True, indent=4,ensure_ascii=False)

        """##############################################################################"""

        if op.param3 in profile_2.mid:
            def K2():
                bot = random.choice([kicker1, kicker3, kicker4, kicker5])
                G = bot.getGroup(op.param1)
                if G.preventJoinByTicket == False:
                    Ticket = bot.reissueGroupTicket(op.param1)
                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    bot.updateGroup(G)
                else:
                    G.preventJoinByTicket = False
                    bot.updateGroup(G)
                    Ticket = bot.reissueGroupTicket(op.param1)
                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    bot.updateGroup(G)
            if op.param2 in user:
                K2()
            elif op.param2 in bots:
                K2()
            else:
                try:
                    kicker3.kickoutFromGroup(op.param1, [op.param2])
                    G = kicker3.getGroup(op.param1)
                    if G.preventJoinByTicket == True:
                        G.preventJoinByTicket = False
                        kicker3.updateGroup(G)
                    Ticket = kicker3.reissueGroupTicket(op.param1)
                    kicker2.acceptGroupInvitationByTicket(op.param1, Ticket)
                    G.preventJoinByTicket = True
                    kicker3.updateGroup(G)
                except:
                    try:
                        kicker4.kickoutFromGroup(op.param1, [op.param2])
                        G = kicker4.getGroup(op.param1)
                        if G.preventJoinByTicket == True:
                            G.preventJoinByTicket = False
                            kicker4.updateGroup(G)
                        Ticket = kicker4.reissueGroupTicket(op.param1)
                        kicker2.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kicker4.updateGroup(G)
                    except:
                        try:
                            kicker5.kickoutFromGroup(op.param1, [op.param2])
                            G = kicker5.getGroup(op.param1)
                            if G.preventJoinByTicket == True:
                                G.preventJoinByTicket = False
                                kicker5.updateGroup(G)
                            Ticket = kicker5.reissueGroupTicket(op.param1)
                            kicker2.acceptGroupInvitationByTicket(op.param1, Ticket)
                            G.preventJoinByTicket = True
                            kicker5.updateGroup(G)
                        except:
                            try:
                                kicker1.kickoutFromGroup(op.param1, [op.param2])
                                G = kicker1.getGroup(op.param1)
                                if G.preventJoinByTicket == True:
                                    G.preventJoinByTicket = False
                                    kicker1.updateGroup(G)
                                Ticket = kicker1.reissueGroupTicket(op.param1)
                                kicker2.acceptGroupInvitationByTicket(op.param1, Ticket)
                                G.preventJoinByTicket = True
                                kicker1.updateGroup(G)
                            except:
                                pass
                if op.param2 in tran["BL"]:
                    pass
                else:
                    tran["BL"][op.param2] = True
                    f=codecs.open('bl.json','w','utf-8')
                    json.dump(tran["BL"], f, sort_keys=True, indent=4,ensure_ascii=False)

        """##############################################################################"""

        if op.param3 in profile_3.mid:
            def K3():
                bot = random.choice([kicker1, kicker2, kicker4, kicker5])
                G = bot.getGroup(op.param1)
                if G.preventJoinByTicket == False:
                    Ticket = bot.reissueGroupTicket(op.param1)
                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    bot.updateGroup(G)
                else:
                    G.preventJoinByTicket = False
                    bot.updateGroup(G)
                    Ticket = bot.reissueGroupTicket(op.param1)
                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    bot.updateGroup(G)
            if op.param2 in user:
                K3()
            elif op.param2 in bots:
                K3()
            else:
                try:
                    kicker4.kickoutFromGroup(op.param1, [op.param2])
                    G = kicker4.getGroup(op.param1)
                    if G.preventJoinByTicket == True:
                        G.preventJoinByTicket = False
                        kicker4.updateGroup(G)
                    Ticket = kicker4.reissueGroupTicket(op.param1)
                    kicker3.acceptGroupInvitationByTicket(op.param1, Ticket)
                    G.preventJoinByTicket = True
                    kicker4.updateGroup(G)
                except:
                    try:
                        kicker5.kickoutFromGroup(op.param1, [op.param2])
                        G = kicker5.getGroup(op.param1)
                        if G.preventJoinByTicket == True:
                            G.preventJoinByTicket = False
                            kicker5.updateGroup(G)
                        Ticket = kicker5.reissueGroupTicket(op.param1)
                        kicker3.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kicker5.updateGroup(G)
                    except:
                        try:
                            kicker1.kickoutFromGroup(op.param1, [op.param2])
                            G = kicker1.getGroup(op.param1)
                            if G.preventJoinByTicket == True:
                                G.preventJoinByTicket = False
                                kicker1.updateGroup(G)
                            Ticket = kicker1.reissueGroupTicket(op.param1)
                            kicker3.acceptGroupInvitationByTicket(op.param1, Ticket)
                            G.preventJoinByTicket = True
                            kicker1.updateGroup(G)
                        except:
                            try:
                                kicker2.kickoutFromGroup(op.param1, [op.param2])
                                G = kicker2.getGroup(op.param1)
                                if G.preventJoinByTicket == True:
                                    G.preventJoinByTicket = False
                                    kicker2.updateGroup(G)
                                Ticket = kicker2.reissueGroupTicket(op.param1)
                                kicker3.acceptGroupInvitationByTicket(op.param1, Ticket)
                                G.preventJoinByTicket = True
                                kicker2.updateGroup(G)
                            except:
                                pass
                if op.param2 in tran["BL"]:
                    pass
                else:
                    tran["BL"][op.param2] = True
                    f=codecs.open('bl.json','w','utf-8')
                    json.dump(tran["BL"], f, sort_keys=True, indent=4,ensure_ascii=False)

        """##############################################################################"""

        if op.param3 in profile_4.mid:
            def K4():
                bot = random.choice([kicker1, kicker2, kicker3, kicker5])
                G = bot.getGroup(op.param1)
                if G.preventJoinByTicket == False:
                    Ticket = bot.reissueGroupTicket(op.param1)
                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    bot.updateGroup(G)
                else:
                    G.preventJoinByTicket = False
                    bot.updateGroup(G)
                    Ticket = bot.reissueGroupTicket(op.param1)
                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    bot.updateGroup(G)
            if op.param2 in user:
                K4()
            elif op.param2 in bots:
                K4()
            else:
                try:
                    kicker5.kickoutFromGroup(op.param1, [op.param2])
                    G = kicker5.getGroup(op.param1)
                    if G.preventJoinByTicket == True:
                        G.preventJoinByTicket = False
                        kicker5.updateGroup(G)
                    Ticket = kicker5.reissueGroupTicket(op.param1)
                    kicker4.acceptGroupInvitationByTicket(op.param1, Ticket)
                    G.preventJoinByTicket = True
                    kicker5.updateGroup(G)
                except:
                    try:
                        kicker1.kickoutFromGroup(op.param1, [op.param2])
                        G = kicker1.getGroup(op.param1)
                        if G.preventJoinByTicket == True:
                            G.preventJoinByTicket = False
                            kicker1.updateGroup(G)
                        Ticket = kicker1.reissueGroupTicket(op.param1)
                        kicker4.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kicker1.updateGroup(G)
                    except:
                        try:
                            kicker2.kickoutFromGroup(op.param1, [op.param2])
                            G = kicker2.getGroup(op.param1)
                            if G.preventJoinByTicket == True:
                                G.preventJoinByTicket = False
                                kicker2.updateGroup(G)
                            Ticket = kicker2.reissueGroupTicket(op.param1)
                            kicker4.acceptGroupInvitationByTicket(op.param1, Ticket)
                            G.preventJoinByTicket = True
                            kicker2.updateGroup(G)
                        except:
                            try:
                                kicker3.kickoutFromGroup(op.param1, [op.param2])
                                G = kicker3.getGroup(op.param1)
                                if G.preventJoinByTicket == True:
                                    G.preventJoinByTicket = False
                                    kicker3.updateGroup(G)
                                Ticket = kicker3.reissueGroupTicket(op.param1)
                                kicker4.acceptGroupInvitationByTicket(op.param1, Ticket)
                                G.preventJoinByTicket = True
                                kicker3.updateGroup(G)
                            except:
                                pass
                if op.param2 in tran["BL"]:
                    pass
                else:
                    tran["BL"][op.param2] = True
                    f=codecs.open('bl.json','w','utf-8')
                    json.dump(tran["BL"], f, sort_keys=True, indent=4,ensure_ascii=False)

        """##############################################################################"""

        if op.param3 in profile_5.mid:
            def K5():
                bot = random.choice([kicker1, kicker2, kicker3, kicker4])
                G = bot.getGroup(op.param1)
                if G.preventJoinByTicket == False:
                    Ticket = bot.reissueGroupTicket(op.param1)
                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    bot.updateGroup(G)
                else:
                    G.preventJoinByTicket = False
                    bot.updateGroup(G)
                    Ticket = bot.reissueGroupTicket(op.param1)
                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    bot.updateGroup(G)
            if op.param2 in user:
                K5()
            elif op.param2 in bots:
                K5()
            else:
                try:
                    kicker1.kickoutFromGroup(op.param1, [op.param2])
                    G = kicker1.getGroup(op.param1)
                    if G.preventJoinByTicket == True:
                        G.preventJoinByTicket = False
                        kicker1.updateGroup(G)
                    Ticket = kicker1.reissueGroupTicket(op.param1)
                    kicker5.acceptGroupInvitationByTicket(op.param1, Ticket)
                    G.preventJoinByTicket = True
                    kicker1.updateGroup(G)
                except:
                    try:
                        kicker2.kickoutFromGroup(op.param1, [op.param2])
                        G = kicker2.getGroup(op.param1)
                        if G.preventJoinByTicket == True:
                            G.preventJoinByTicket = False
                            kicker2.updateGroup(G)
                        Ticket = kicker2.reissueGroupTicket(op.param1)
                        kicker5.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kicker2.updateGroup(G)
                    except:
                        try:
                            kicker3.kickoutFromGroup(op.param1, [op.param2])
                            G = kicker3.getGroup(op.param1)
                            if G.preventJoinByTicket == True:
                                G.preventJoinByTicket = False
                                kicker3.updateGroup(G)
                            Ticket = kicker3.reissueGroupTicket(op.param1)
                            kicker5.acceptGroupInvitationByTicket(op.param1, Ticket)
                            G.preventJoinByTicket = True
                            kicker3.updateGroup(G)
                        except:
                            try:
                                kicker4.kickoutFromGroup(op.param1, [op.param2])
                                G = kicker4.getGroup(op.param1)
                                if G.preventJoinByTicket == True:
                                    G.preventJoinByTicket = False
                                    kicker4.updateGroup(G)
                                Ticket = kicker4.reissueGroupTicket(op.param1)
                                kicker5.acceptGroupInvitationByTicket(op.param1, Ticket)
                                G.preventJoinByTicket = True
                                kicker4.updateGroup(G)
                            except:
                                pass
                if op.param2 in tran["BL"]:
                    pass
                else:
                    tran["BL"][op.param2] = True
                    f=codecs.open('bl.json','w','utf-8')
                    json.dump(tran["BL"], f, sort_keys=True, indent=4,ensure_ascii=False)

        else:
            if op.param1 in _pro['PK']:
                botr = random.choice(BOT)
                if op.param2 in bots:
                    pass
                elif op.param2 in user:
                    pass
                else:
                    try:
                        botr.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        try:
                            botr_ = random.choice(BOT)
                            botr_.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            pass
                    try:
                        botr.findAndAddContactsByMid(op.param3)
                    except:
                        try:
                            boter_ = random.choice(BOT)
                            boter.findAndAddContactsByMid(op.param3)
                        except:
                            pass
                    try:
                        botr.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            botr__ = random.choice(BOT)
                            botr__.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass

            if op.param3 in user:
                botr = random.choice(BOT)
                if op.param2 in bots:
                    try:
                        botr.findAndAddContactsByMid(op.param3)
                    except:
                        try:
                            botrr = random.choice(BOT)
                            botrr.findAndAddContactsByMid(op.param3)
                        except:
                            pass
                    try:
                        botr.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            botrr_ = random.choice(BOT)
                            botrr.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass
     
                elif op.param2 in user:
                    try:
                        botr.findAndAddContactsByMid(op.param3)
                    except:
                        try:
                            botrr = random.choice(BOT)
                            botrr.findAndAddContactsByMid(op.param3)
                        except:
                            pass
                    try:
                        botr.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            botrr_ = random.choice(BOT)
                            botrr.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass
                else:
                    try:
                        botr.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        try:
                            botrr = random.choice(BOT)
                            botrr.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            pass
                    try:
                        botr.findAndAddContactsByMid(op.param3)
                    except:
                        try:
                            botrr = random.choice(BOT)
                            botrr.findAndAddContactsByMid(op.param3)
                        except:
                            pass
                    try:
                        botr.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            botrr_ = random.choice(BOT)
                            botrr.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass



    except Exception as e:
        print e

tracer.addOpInterrupt(19, KICK)

def SENDM(op):
    msg = op.message
    
    if msg.contentType == 0:
        try:
            if msg.text in (["ミュートオン"]):
                if msg.to in tran['mut']:
                    pass
                else:
                    tran['mut'][msg.to] = True
                    f=codecs.open('mut.json','w','utf-8')
                    json.dump(tran["mut"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    client.sendText(msg.to, "ミュートを有効にしたよ")

            elif msg.text in (["ミュートオフ"]):
                if msg.to in tran['mut']:
                    del tran['mut'][msg.to]
                    f=codecs.open('mut.json','w','utf-8')
                    json.dump(tran["mut"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    client.sendText(msg.to, "ミュートを解除したよ")

            if msg.to in tran['mut']:
                pass

            elif msg.text == "mid":
                if msg._from in user:
                    client.sendText(msg.to, te(msg._from))

            elif msg.text == "gid":
                if msg._from in user:
                    client.sendText(msg.to, te(msg.to))

            elif msg.text == "help":
                if msg._from in user:
                    client.sendFile(msg.to, "help.txt")

            elif msg.text == "bye":
                if msg._from in user:
                    for _bot in [client, kicker1, kicker2, kicker3, kicker4, kicker5]:
                        _bot.leaveGroup(msg.to)

            elif msg.text == "test":
                if msg._from in user:
                    client.sendText(msg.to, "正常に動いてる！！")

            elif msg.text == "test2":
                if msg._from in master:
                    for bo in [client, kicker1, kicker2, kicker3, kicker4, kicker5]:
                        bo.sendText(msg.to, "正常に動いてる！！")

            elif msg.text == "gurl":
                if msg._from in user:
                    g = client.getGroup(msg.to)
                    if g.preventJoinByTicket == False:
                        client.sendText(msg.to, "参加可能だよ！\nline://ti/g/" + client._client.reissueGroupTicket(msg.to))
                    else:
                        client.sendText(msg.to, "参加できないよ！？\nline://ti/g/" + client._client.reissueGroupTicket(msg.to))
            
            elif msg.text == "url:on":
                if msg._from in user:
                    bot = random.choice([client, kicker1, kicker2, kicker3, kicker4, kicker5])
                    g = bot.getGroup(msg.to)
                    if g.preventJoinByTicket == False:
                        client.sendText(msg.to, '既に許可状態だよ！')
                    else:
                        g.preventJoinByTicket = False
                        bot.updateGroup(g)
                        client.sendText(msg.to, 'URL招待を許可したよ！')
           
            elif msg.text == "url:off":
                if msg._from in user:
                    bot = random.choice([client, kicker1, kicker2, kicker3, kicker4, kicker5])
                    g = bot.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        client.sendText(msg.to, '既に拒否状態だよ！。')
                    else:
                        g.preventJoinByTicket = True
                        bot.updateGroup(g)
                        client.sendText(msg.to, 'URL招待を拒否したよ！')



            elif msg.text == "bot":
                if msg._from in user:
                    G = client.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    client.updateGroup(G)
                    Ti = client.reissueGroupTicket(msg.to)
                    for _bot in [kicker1, kicker2, kicker3, kicker4, kicker5]:
                        _bot.acceptGroupInvitationByTicket(msg.to, Ti)
                    bot = random.choice([kicker1, kicker2])
                    G = bot.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    bot.updateGroup(G)
                    
            elif msg.text == "グル画変更":
                if msg._from in user:
                    tran["gim"] = [msg.to]
                    client.sendText(msg.to, 'グル画にする写真を送信してね')

            elif  msg.text == "me":
                if msg._from in user:
                    contact = client.getContact(msg._from)
                    md = ""
                    md += "[名前]\n" + contact.displayName
                    md += "\n\n[一言]\n" + contact.statusMessage
                    md += "\n\n[mid]\n" + te(contact.mid)
                    md += "\n\n[トプ画]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus
                    md += "\n\n[ホーム画]\n" + channel.getProfileCoverURL(msg._from)
                    client.sendText(msg.to, md)

            
            elif "権限追加" in msg.text:
                if msg._from in master:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            if (target in haveP):
                                client.sendText(msg.to,"既に権限者だよ！")
                            else:
                                haveP.append(target)
                                f = open('op.ad','w')
                                for i in haveP:
                                    f.write(i + "\n")
                                f.close()
                                client.sendText(msg.to, "追加したよ！")
                                _set["havePs"] = haveP
                        except:
                            pass

            elif "権限削除" in msg.text:
                if msg._from in master:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            haveP.remove(target)
                            f = open('op.ad','w')
                            for i in haveP:
                                f.write(i + "\n")
                            f.close()
                            client.sendText(msg.to,"削除したよ！")
                            _set["havePs"] = haveP
                        except:
                            client.sendText(msg.to,"権限者じゃないよ！")


            elif "権限確認" in msg.text:
                if msg._from in master:
                    if haveP == []:
                        client.sendText(msg.to,"権限者はいないよ。。。")
                    else:
                        mc = "以下が権限者だよ！\n\n"
                        for mi_d in haveP:
                            try:
                                mc += "・" +client.getContact(mi_d).displayName + "\n"
                            except Exception as error:
                                client.sendText(msg.to,str(error))
                        client.sendText(msg.to,mc)

            elif "画像保護オン" in msg.text:
                if msg._from in user:
                    if msg.to in _pro['PI']:
                        client.sendText(msg.to, '既に画像保護はオンだよ！')
                    else:
                        client.sendText(msg.to, '画像保護をオンにしたよ！')
                        group = client.getGroup(msg.to)
                        url = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                        urllib.urlretrieve(url, "image\\gp\\" + msg.to + ".png")
                        _pro['PI'][msg.to] = True
                        f=codecs.open('image.json','w','utf-8')
                        json.dump(_pro["PI"], f, sort_keys=True, indent=4,ensure_ascii=False)
    
    
            elif "画像保護オフ" in msg.text:
                if msg._from in user:
                    if msg.to in _pro['PI']:
                        client.sendText(msg.to, '画像保護をオフにしたよ！')
                        os.remove("image\\gp\\" + msg.to + '.png')
                        del _pro['PI'][msg.to]
                        f=codecs.open('image.json','w','utf-8')
                        json.dump(_pro["PI"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    else:
                        client.sendText(msg.to, '既に画像保護はオフだよ！')


            elif "名前保護オン" in msg.text:
                if msg._from in user:
                    if msg.to in _pro['PN']:
                        client.sendText(msg.to, '既に名前保護はオンだよ！')
                    else:
                        _pro['PN'][msg.to] = client.getGroup(msg.to).name
                        f=codecs.open('name.json','w','utf-8')
                        json.dump(_pro["PN"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        client.sendText(msg.to, '名前保護をオンにしたよ！')
    
    
            elif "名前保護オフ" in msg.text:
                if msg._from in user:
                    if msg.to in _pro['PN']:
                        client.sendText(msg.to, '名前保護をオフにしたよ！')
                        del _pro['PN'][msg.to]
                        f=codecs.open('name.json','w','utf-8')
                        json.dump(_pro["PN"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    else:
                        client.sendText(msg.to, '既に名前保護はオフだよ！')


            elif "URL保護オン" in msg.text:
                if msg._from in user:
                    if msg.to in _pro['PU']:
                        client.sendText(msg.to, '既にURL保護はオンだよ！')
                    else:
                        _pro['PU'][msg.to] = True
                        f=codecs.open('url.json','w','utf-8')
                        json.dump(_pro["PU"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        bot = random.choice(BOT)
                        G = bot.getGroup(msg.to)
                        G.preventedJoinByTicket = True
                        bot.updateGroup(G)
                        client.sendText(msg.to, 'URL保護をオンにしたよ！')
            
    
            elif "URL保護オフ" in msg.text:
                if msg._from in user:
                    if msg.to in _pro['PU']:
                        client.sendText(msg.to, 'URL保護をオフにしたよ！')
                        del _pro['PU'][msg.to]
                        f=codecs.open('url.json','w','utf-8')
                        json.dump(_pro["PU"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    else:
                        client.sendText(msg.to, '既にURL保護はオフだよ！')


            elif "招待保護オン" in msg.text:
                if msg._from in user:
                    if msg.to in _pro['PA']:
                        client.sendText(msg.to, '既に招待保護はオンだよ！')
                    else:
                        _pro['PA'][msg.to] = True
                        f=codecs.open('inv.json','w','utf-8')
                        json.dump(_pro["PA"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        client.sendText(msg.to, '招待保護をオンにしたよ！')
    
    
            elif "招待保護オフ" in msg.text:
                if msg._from in user:
                    if msg.to in _pro['PA']:
                        client.sendText(msg.to, '招待保護をオフにしたよ！')
                        del _pro['PA'][msg.to]
                        f=codecs.open('inv.json','w','utf-8')
                        json.dump(_pro["PA"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    else:
                        client.sendText(msg.to, '既に招待保護はオフだよ！')

            elif "蹴り保護オン" in msg.text:
                if msg._from in user:
                    if msg.to in _pro['PK']:
                        client.sendText(msg.to, '既に蹴り保護はオンだよ！')
                    else:
                        _pro['PK'][msg.to] = True
                        f=codecs.open('kick.json','w','utf-8')
                        json.dump(_pro['PK'], f, sort_keys=True, indent=4,ensure_ascii=False)
                        client.sendText(msg.to, '蹴り保護をオンにしたよ！')
    
    
            elif "蹴り保護オフ" in msg.text:
                if msg._from in user:
                    if msg.to in _pro['PK']:
                        client.sendText(msg.to, '蹴り保護をオフにしたよ！')
                        del _pro['PK'][msg.to]
                        f=codecs.open('kick.json','w','utf-8')
                        json.dump(_pro['PK'], f, sort_keys=True, indent=4,ensure_ascii=False)
                    else:
                        client.sendText(msg.to, '既に蹴り保護はオフだよ！')

            elif "終了" in msg.text:
                if msg._from in master:
                    client.sendText(msg.to, 'ok')
                    sys.exit(0)

            elif "ブラックリスト確認" in msg.text:
                if msg._from in user:
                    if tran['BL'] == {}:
                        client.sendText(msg.to, "ブラックリストにしている人はいないよ")
                    else:
                        client.sendText(msg.to, "以下がブラックリストだよ")
                        mc = ""
                        for mi_d in tran['BL']:
                            try:
                                mc += "・" +client.getContact(mi_d).displayName + "\n"
                            except:
                                pass
                        client.sendText(msg.to, mc)


            elif "ブラックリスト排除" in msg.text:
                if msg._from in user:
                    group = client.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in tran["BL"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        client.sendText(msg.to, "ブラックリストユーザーはいないよ！")
                        return
                    for jj in matched_list:
                        bot=random.choice(BOT)
                        bot2=random.choice(BOT)
                        try:
                            bot.kickoutFromGroup(msg.to,[jj])
                            time.sleep(0.5)
                        except:
                            try:
                                bot2.kickoutFromGroup(msg.to,[jj])
                                time.sleep(0.5)
                            except:
                                pass
                    client.sendText(msg.to, "ブラックリストユーザーの追い出しが完了したよ！")

            elif "ブラックリスト追加" in msg.text:
                if msg._from in master:
                    if tran['ab'] == True:
                        if tran["db"] == True:
                            tran["db"] = False
                            client.sendText(msg.to, 'ブラックリストに追加する連絡先を送信してね！')
                    else:
                        if tran["db"] == True:
                            tran["db"] = False
                        tran['ab'] = True
                        client.sendText(msg.to, 'ブラックリストに追加する連絡先を送信してね！')
    
    
            elif "ブラックリスト削除" in msg.text:
                if msg._from in master:
                    if tran['db'] == True:
                        if tran["ab"] == True:
                            tran["ab"] = False
                        client.sendText(msg.to, 'ブラックリストから削除する連絡先を送信してね！')
                    else:
                        tran['db'] = True
                        if tran["ab"] == True:
                            tran["ab"] = False
                        client.sendText(msg.to, 'ブラックリストから削除する連絡先を送信してね！')



            elif msg.text == "作成者":
                if msg._from in user:
                    _mid = "NGU3YTU1N2E0ZDdhNGQ3ODRlNmE0NTMyNGU0NDRkMzU0ZDdhNTkzMjRlNDQ0ZDMyNGQ3YTQ5MzI0ZTQ0NGQ3NzRlNmE0NTMyNGQ3YTRkMzE0ZDdhNTE3YTRlNTQ0ZDdhNGQ3YTRkN2E0ZjQ0NGQzMzRkN2E2NzdhNGQ2YTU5MzA0ZDdhNTEzMjRlNmE0ZDMzNGU2YTU5N2EwYTRlNmE1OTdhNGU2YTU5N2E0ZTZhNTk3OTBh"
                    client.sendContact(msg.to, td(_mid))

            elif msg.text == "招待→":
                if msg._from in user:
                    if msg.toType == 2:
                        mid = mst.replace("招待→","")
                        bot=random.choice(BOT)
                        bot2=random.choice(BOT)
                        try:
                            bot.findAndAddContactsByMid(td(mid))
                            bot.inviteIntoGroup(msg.to,[td(mid)])
                        except:
                            try:
                                bot2.findAndAddContactsByMid(td(mid))
                                bot2.inviteIntoGroup(msg.to,[td(mid)])
                            except:
                                pass
                    else:
                        client.sendText(msg.to,"グループ以外では使用できないよ！")

            elif msg.text == "ginfo":
                if msg.toType == 2:
                    ginfo = client.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                        u = "拒否"
                    else:
                        u = "許可"
                    client.sendText(msg.to,"[名前]\n" + str(ginfo.name) + "\n[gid]\n" + te(msg.to) + "\n[グループの作成者]\n" + gCreator + "\n[グループアイコン]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nメンバー:" + str(len(ginfo.members)) + "人\n招待中:" + sinvitee + "人\n招待URL:" + u + "中だよ！")
                else:
                    client.sendText(msg.to,"グループ以外では使用できないよ！")

            elif "mk" in msg.text:
                if msg._from in user:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target == "":
                            pass
                        elif target == " ":
                            pass
                        elif target in "":
                            pass
                        elif target in " ":
                            pass
                        else:
                            try:
                                botr = random.choice(BOT)
                                botr.kickoutFromGroup(msg.to, [target])
                            except:
                                botr_ = random.choice(BOT)
                                botr_.kickoutFromGroup(msg.to, [target])

        except Exception as e:
            print e

    if msg.contentType == 13:
        try:
            if tran["ab"] == True:
                if msg.contentMetadata["mid"] in tran["BL"]:
                    client.sendText(msg.to, "すでにブラックリストに入っているよ！")
                else:
                    client.sendText(msg.to, "ブラックリストに追加したよ！")
                    tran["BL"][msg.contentMetadata["mid"]] = True
                    f=codecs.open('bl.json','w','utf-8')
                    json.dump(tran["BL"], f, sort_keys=True, indent=4,ensure_ascii=False)
                tran["ab"] = False

            elif tran["db"] == True:
                if msg.contentMetadata["mid"] in tran["BL"]:
                    client.sendText(msg.to, "ブラックリストから削除したよ！")
                    del tran["BL"][msg.contentMetadata["mid"]]
                    f=codecs.open('bl.json','w','utf-8')
                    json.dump(tran["BL"], f, sort_keys=True, indent=4,ensure_ascii=False)
                else:
                    client.sendText(msg.to, "ブラックリストに入っていないよ！")
                tran["db"] = False

            else:
                mid = msg.contentMetadata["mid"]
                data = client.getContact(mid)
                mes = ""
                mes += "[名前]\n%s" % data.displayName
                mes += "\n\n[一言]\n%s" % data.statusMessage
                mes += "\n\n[mid]\n%s" % te(mid)
                mes += "\n\n[トプ画]\nhttp://dl.profile.line-cdn.net/" + data.pictureStatus
                mes += "\n\n[ホーム画]\n" + channel.getProfileCoverURL(mid)
                if msg.contentMetadata["mid"] in tran["BL"]:
                    mes +=  "\n\n[ブラックリスト]\nTrue"
                else:
                    mes +=  "\n\n[ブラックリスト]\nFalse"
                client.sendText(msg.to, mes)

            """for n in channel.getHomeProfile(mid)["result"]["feeds"]:
                for mes_ in [channel, channel_1, channel_2, channel_3, channel_4, channel_5]:
                    mes_.like(n["post"]["postInfo"]["homeId"], n["post"]["postInfo"]["postId"], likeType=1001)
                    time.sleep(0.5)"""

        except Exception as e:
            print e


    if msg.contentType == 1:
        if msg._from in user:
            if  msg.to in tran["gim"]:
                try:
                    client.downloadObjectMsg(msg.id, returnAs='path', saveAs='image\\gp\\a.png')
                    time.sleep(1)
                    client.updateGroupPicture(msg.to, "image\\gp\\a.png")
                    client.sendText(msg.to, 'グル画を以下に設定しました。')
                    client.sendImage(msg.to, "image\\gp\\a.png")
                    del tran["gim"]
                except Exception as e:
                    print e

tracer.addOpInterrupt(26, SENDM)


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
                try:
                    channel_1.like(home_id, post_id, likeType=1001)
                except:
                    pass
                try:
                    channel_2.like(home_id, post_id, likeType=1001)
                except:
                    pass
                try:
                    channel_3.like(home_id, post_id, likeType=1001)
                except:
                    pass
                try:
                    channel_4.like(home_id, post_id, likeType=1001)
                except:
                    pass
                try:
                    channel_5.like(home_id, post_id, likeType=1001)
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