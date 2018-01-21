# -*- coding: utf-8 -*-
import unittest
import requests

class MainbyudjeetzarplataTestCases(unittest.TestCase):

    def setUp(self):
        url = "https://bo.bars.group/bars_office/mainbyudjeetzarplata/read_rows/"

        querystring = {"_dc":"1516478680739"}

        payload = "{\"subfilterfie\":\"byudjeetbc\",\"subfiltervalue\":\"6921BDC6945EAE43AA3266F25B3F9E75\",\"extraParams\":{\"subfilterfie\":\"byudjeetbc\",\"subfiltervalue\":\"6921BDC6945EAE43AA3266F25B3F9E75\"},\"filters\":[],\"additionalParams\":{}}"
        headers = {
            'origin': "https://bo.bars.group",
            'x-requested-with': "XMLHttpRequest",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            'content-type': "application/json; charset=UTF-8",
            'accept': "*/*",
            'referer': "https://bo.bars.group/",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            'cookie': "",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        self.data_json = dict(response.json())
        self.data_response = response

    def test_mainbyudjeetzarplata_statuscode(self):
        self.assertEquals(self.data_response.status_code, 200, 'код ответа не 200 ')

    def test_mainbyudjeetzarplata_data(self):
        self.assertTrue("mainbyudjeetzarplata" in self.data_json, 'нет данных по зарплате сотрудников БЦ')