# -*-coding: utf-8 -*-
import random
import requests

class LxFunction():
    @staticmethod
    def get_tion(tions):
        if tions:
            return random.choice(tions)
        return None

    @staticmethod
    def request_get(url, data, headers):
        try:
            res = requests.post(url=url, data=data, headers=headers)
        except Exception as e:
            return {"errer": e}
        else:
            return res.text

