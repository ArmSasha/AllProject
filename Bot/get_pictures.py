#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, vk_api, data
import time

vk_session = vk_api.VkApi(token='Тут ваш токен')
session_api = vk_session.get_api()


def get():
    try:
        id_group = '-playbote'
        attachment = '-130670107'
        pictures = session_api.photos.get(owner_id=id_group, album_id='wall', count=5)['items']
        buf = []
        for element in pictures:
            buf.append('photo' + str(id_group) + '_' + str(element['id']))
        attachment = ','.join(buf)
        return attachment
    except:
        return get()
