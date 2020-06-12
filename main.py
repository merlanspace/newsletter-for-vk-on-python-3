# -*- coding: utf-8 -*-
import vk_api

vk_session = vk_api.VkApi(token='token')
vk = vk_session.get_api()

mailing = vk.messages.getConversations(count=200, filter="all", group_id="group_id")['items'] #Можете добавить offset, если рассылка делается больше 200
text = "text"
for peer_id in mailing:
   peer = peer_id.get('conversation').get('peer').get('id')
   try:
       vk.messages.send(
           peer_id=peer,
           message=text,
           random_id=0
       )
   except BaseException as r:
      print(r)
      pass
print('Newsletter is over!')
