
# coding: utf-8

# In[1]:

import itchat


# In[34]:

itchat.auto_login(enableCmdQR=2)


# In[35]:

friends = itchat.get_friends()


# In[36]:

friends


# In[37]:

NAME_TO_ID = {
    "娄晨耀": "",
    "王梦迪": "",
    "墨染经年": "",
    ".....": "",
    "任崇旭": "",
    "张若天": "",
}

ID_TO_NAME = {}

for f in friends:
    if f["NickName"] in NAME_TO_ID:
        id_ = f["UserName"]
        NAME_TO_ID[f["NickName"]] = id_
        ID_TO_NAME[id_] = f["NickName"]


# In[38]:

ID_TO_NAME


# In[39]:

reply = {
    "王梦迪": "梦迪梦迪梦",
    "墨染经年": "小熊熊",
    ".....": "啊，你先睡吧，我现在有事，晚安~",
    "张若天": "膜zrt dalao",
    "任崇旭": "膜rcx dalao"
}


# In[40]:

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg)
    name = ID_TO_NAME[msg["FromUserName"]]
    if name in reply:
        return reply[name]
    


# In[ ]:

itchat.run()


# In[ ]:



