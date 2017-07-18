#! /usr/bin/env python3
# coding: utf-8

import itchat
from itchat.content import *


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def reply(msg):
    print(msg.User.NickName)
    if msg.User.NickName == "群主最帅":
        #msg.user.send_image("/home/louch/shuai.jpg")
        msg.user.send("不管不管，我就是最帅的！")
        print("sent!")
    if msg.User.NickName == "计科60同学群":
        msg.user.send("膜dalao")
    print("\n\n\n\n============\n\n\n")

itchat.auto_login(enableCmdQR=2)
itchat.run()

