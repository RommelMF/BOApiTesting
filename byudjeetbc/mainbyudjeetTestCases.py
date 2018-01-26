# -*- coding: utf-8 -*-
import requests
import unittest
import json


class MainbyudjeetTestCases(unittest.TestCase):

    def setUp(self):
        # получение id бюджета из файла
        with open('test_data.json', 'r') as f:
            data = dict(json.load(f))
            byudjeet_id = data["Id"]
        url = "https://test-bo.bars.group/bars_office/mainbyudjeet/read_rows/"

        querystring = {"_dc": "1516699633543"}
        payload = "{\"subfilterfie\":\"byudjeetbc\",\"subfiltervalue\":\""+ byudjeet_id +"\",\"extraParams\":{\"subfilterfie\":\"byudjeetbc\",\"subfiltervalue\":\""+ byudjeet_id +"\"},\"filters\":[],\"additionalParams\":{}}"
        headers = {
            'origin': "https://bo.bars.group",
            'x-requested-with': "XMLHttpRequest",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            'content-type': "application/json; charset=UTF-8",
            'accept': "*/*",
            'referer': "https://bo.bars.group/",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            'cookie': "" ,
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        self.data_json = dict(response.json())
        self.data_response = response
        print self.data_json

    def test_mainbyudjeet_statuscode(self):
        self.assertEquals(self.data_response.status_code, 200, 'код ответа не 200 ')

    def test_mainbyudjeet_data(self):
        self.assertTrue("mainbyudjeet" in self.data_json, 'нет данных по статьям расходов бюджета БЦ')


