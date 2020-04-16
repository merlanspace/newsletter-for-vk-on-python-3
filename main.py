# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token='token')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id)


mailing = vk.messages.getConversations(count=200, filter="all", group_id="group_id")['items']
text = "text"
for peer_id in mailing:
   peer = peer_id.get('conversation').get('peer').get('id')
   print("id" + str(peer))
   try:
       vk.messages.send(
           peer_id=peer,
           message=text
           random_id=0
       )
   except Exception:
       pass
print('Newsletter is over!')
