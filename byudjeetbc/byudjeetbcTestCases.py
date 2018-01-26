# -*- coding: utf-8 -*-
import unittest
import requests
import json
# test for main greed budjeetbc
class ByudjeetbcTestCases(unittest.TestCase):

    # test edit for budjeet bc
    def setUp(self):
        # load from json
        with open('test_config.json', 'r') as f:
            json_data = json.load(f)
            self.cookies = json_data['cookies']
            print(self.cookies)
        #     params
        year = "2018"
        url = "https://test-bo.bars.group/bars_office/byudjeetbc/read_rows/"
        self.value = "JSESSIONID=dummy; " + self.cookies
        print(self.value)
        querystring = {"_dc": "1516787375303"}

        payload = "{\"start\":0,\"limit\":0,\"extraParams\":{},\"filters\":[],\"additionalParams\":{\"year\":" + year + "}}"
        headers = {
            'origin': "https://test-bo.bars.group",
            'x-devtools-emulate-network-conditions-client-id': "(9FDDFF3335C3E58460CE1BEFEF8B222)",
            'x-requested-with': "XMLHttpRequest",
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            'content-type': "application/json; charset=UTF-8",
            'accept': "*/*",
            'referer': "https://test-bo.bars.group/",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            'cookie': self.value,
            'cache-control': "no-cache",
        }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        # conversion to dict type
        print(response.text)
        self.data_json = dict(response.json())
        self.data_response = response
        # сохранение данных по бюджету в json
        bc_data = self.data_json["byudjeetbc"][0]
        with open('test_data.json', 'w') as f:
            json.dump(bc_data, f)
        print self.data_json

    # test status code
    def test_byudjeetbc_statuscode(self):
        self.assertEquals(self.data_response.status_code, 200, 'код ответа не 200 ')

    # test data json
    def test_byudjeetbc_data(self):
        self.assertTrue("byudjeetbc" in self.data_json, 'нет данных по бюджетам БЦ')

    # test metadata
    def test_budjeetbc_metadata(self):

        url = "https://test-bo.bars.group/bars_office/byudjeetbc/getMetaData/"

        querystring = {"_dc": "1516971339549"}

        headers = {
            'x-devtools-emulate-network-conditions-client-id': "(9FDDFF3335C3E58460CE1BEFEF8B222)",
            'x-requested-with': "XMLHttpRequest",
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            'accept': "*/*",
            'referer': "https://test-bo.bars.group/",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            'cookie': self.value,
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.status_code)
        self.assertEquals(response.status_code, 200, 'код запроса не 200')

#     метод добавления бюджетов
#     метод для редактирования +
#     метод для удаления

#     метод для печати
    def test_print_to_exel(self):
        url = "https://test-bo.bars.group/static/BarsUp/grid/multigrouping/MultigroupToExcel.js"

        querystring = {"_dc": "1516973420202"}

        headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            'x-devtools-emulate-network-conditions-client-id': "(9FDDFF3335C3E58460CE1BEFEF8B222)",
            'accept': "*/*",
            'referer': "https://test-bo.bars.group/",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            'cookie': self.value,
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        self.assertEquals(response.status_code, 200, "печать не работает")
#     метод для кнопки "применить"
#     метод для кнопки в разрезе ЭРБЦ
#     метод для кнопки в разрезе месяцев
#     метод для пересчета
    #TODO refactor and update
    def skipTest(self):

        url = "https://test-bo.bars.group/bars_office/byudjeetbc/recalc_data_test/"

        payload = {'id': '974D5C1AD902DB47B8462590453030C2', 'bc_select':'БФОДЗ;', 'bc_select_id': 'A543C74FA97DE94B82FFE3AEBE3894E8', 'loadedGridFields': '[]', 'local_filters': '[{"groupName":"and","list_fie":[{"fie":"bc__name__icontains","symbol":"=","value":"\u0411\u0424\u041e\u0414\u0417"}]}]', 'month': '2', 'year': '2017'}
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
            'cookie': self.value,
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        print (response.json())

    # TODO refactor and update
    def skipTest(self, reason):
         import requests

         url = "https://test-bo.bars.group/bars_office/byudjeetbc/recalc_data/"

         payload = {'Id': '0D916B08ECCBB84BA17EB3F961FC95FB;', 'loadedGridFields': '[]', 'local_filters': '[{"groupName":"and","list_fie":[{"fie":"bc__name__icontains","symbol":"=","value":"\u0411\u0424\u041e\u0414\u0417"}]}]'}
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
             'cookie': self.value,
             'cache-control': "no-cache"
         }
         response = requests.request("POST", url, data=payload, headers=headers)

         print(response.text)




