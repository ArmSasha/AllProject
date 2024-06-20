#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, vk_api, data
import time

vk_session = vk_api.VkApi(token='43e04b63445d4a431dbfdb6d38e2e00a4068efdaddfa25b4e3e5e769c219b290be914d470fbf4d1fe3e49')
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