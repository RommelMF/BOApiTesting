# -*- coding: utf-8 -*-
import requests
import unittest
import json

class AuthTest(unittest.TestCase):
    def test_auth_test(self):
        # load user data from file
        with open('./test_userData.json', 'r') as f:
            user_data = dict(json.load(f))
            username = user_data['username']
            password =  user_data['password']

        url = "https://test-bo.bars.group/core/account/logon/"

        payload = {'username': username, 'password': password}
        headers = {
                'origin': "https://test-bo.bars.group",
                'x-devtools-emulate-network-conditions-client-id': "(9FDDFF3335C3E58460CE1BEFEF8B222)",
                'x-requested-with': "XMLHttpRequest",
                'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
                'content-type': "application/x-www-form-urlencoded",
                'accept': "*/*",
                'referer': "https://test-bo.bars.group/",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                'cookie': "JSESSIONID=dummy;",
                'cache-control': "no-cache",
                    }

        response = requests.request("POST", url, data=payload, headers=headers)

        result = self.assertTrue('success' in dict(response.json()))
        if (result):
            # получаем куки
            d = dict(response.cookies)
            value = "sessionid=" + d['sessionid']
            data_json = {'cookies': value}
            # сохраняем в фаил json
            with open('./test_config.json', 'w') as f:
                json.dump(data_json,f)
            print ("added cookies for testing")




