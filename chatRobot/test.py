#coding=utf8
import itchat
from itchat.content import *

itchat.auto_login(hotReload=True)

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
  # 返回同样的文本消息
  return msg['Text']

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # 微信里，每个用户和群聊，都使用很长的ID来区分
    # msg['FromUserName']就是发送者的ID
    # 将消息的类型和文本内容返回给发送者
    if "呵呵" in msg['Text']:
        itchat.send('嘿嘿', msg['FromUserName'])


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    # msg['Text']是一个文件下载函数
    # 传入文件名，将文件下载下来
    msg['Text'](msg['FileName'])
    # 把下载好的文件再发回给发送者
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
itchat.run()
# @itchat.msg_register(itchat.content.TEXT)
# def print_content(msg):
#     print(msg['Text'])
# while (1 < 100):
#     text = input("请输入：")
#     if text == "x":
#         print("ese")
#         break
#     else:
#         itchat.send(text, toUserName='wm199303060606')


