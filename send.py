#coding=gbk
#coding=gb2312

#-*- coding: UTF-8 -*-
import requests

url = "http://live.bilibili.com/msg/send"

roomid = str(raw_input('roomid\n'));
text = str(raw_input('your message\n'));
payload = 'color=16777215&fontsize=25&mode=2&msg={0}&rnd=1475738964&roomid={1}'.format(text, roomid)
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cookie': "fts=1459666392; pgv_pvi=6563209216; LIVE_BUVID=0a9d09d9b3c6dbeefdbe4b6317c421ef; LIVE_BUVID__ckMd5=1f93cc10f7dc42b6; rpdid=owkkpwilmqdopmppipmxw; DedeUserID=7707374; DedeUserID__ckMd5=aa1f0beaba75e2c8; SESSDATA=a72b7279%2C1477910874%2C00ed8316; LIVE_LOGIN_DATA=df91051483fc8dddeb1dfcc5ea86827341c3b97b; LIVE_LOGIN_DATA__ckMd5=09ebffb81e9b1647; sid=k2erxake; pgv_si=s384468992; _cnt_dyn=null; _cnt_pm=1; _cnt_notify=30; uTZ=-480; rlc_time=1475733638969; activityGiftNum=%7B%2245%22%3A%7B%22num%22%3A36%2C%22bagId%22%3A9747188%2C%22dayNum%22%3A10%7D%7D; user_face=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Fface%2F2a2812ce04604fdef64f6251a2cff2b5c9696e0b.jpg; _dfcaptcha=3825536674c524a5a70d50000814ab43; attentionData=%7B%22code%22%3A0%2C%22msg%22%3A%22%22%2C%22data%22%3A%7B%22count%22%3A0%2C%22open%22%3A0%2C%22has_new%22%3A0%7D%7D; CNZZDATA2724999=cnzz_eid%3D1886699635-1468131581-http%253A%252F%252Fwww.bilibili.com%252F%26ntime%3D1475738966",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)