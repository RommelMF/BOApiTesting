# -*- coding: utf-8 -*-
import unittest
import requests
import json

# test for main greed budjeetbc
class ByudjeetbcTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # load user data
        with open('test_userData.json', 'r') as f:
            json_data = json.load(f)

        with requests.Session() as session:
            url = "https://test-bo.bars.group/core/account/logon/"  # URL with login form
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
            session.get(url)  # get login page
            session.post(url, json_data, headers)  # get user session and write a local variable
            cls.user_session = session

    # test edit for budjeet bc
    def test_budjeetbc_is200(self):
        year = "2018"
        url = "https://test-bo.bars.group/bars_office/byudjeetbc/read_rows/"
        payload = "{\"start\":0,\"limit\":0,\"extraParams\":{},\"filters\":[],\"additionalParams\":{\"year\":" + year + "}}"

        response = self.user_session.post(url, data=payload)
        self.assertEquals(response.status_code, 200, 'код ответа не 200 ')

    # test status code
    def test_byudjeetbc_data_is_not_null(self):
        year = "2018"
        url = "https://test-bo.bars.group/bars_office/byudjeetbc/read_rows/"
        payload = "{\"start\":0,\"limit\":0,\"extraParams\":{},\"filters\":[],\"additionalParams\":{\"year\":" + year + "}}"

        response = self.user_session.post(url=url, data=payload)

        self.assertTrue("byudjeetbc" in response.json(), 'нет данных по бюджетам БЦ')

        # test metadata
    def test_budjeetbc_metadata_is200(self):
        url = "https://test-bo.bars.group/bars_office/byudjeetbc/getMetaData/"

        response = self.user_session.get(url=url)
        self.assertEquals(response.status_code, 200, 'код запроса не 200')

    #     разутверждение
    def test_budjeetbc_onDisapprove(self):
        year = "2018"
        url = "https://test-bo.bars.group/bars_office/byudjeetbc/read_rows/"
        payload_budj = "{\"start\":0,\"limit\":0,\"extraParams\":{},\"filters\":[],\"additionalParams\":{\"year\":" + year + "}}"

        response_budj = self.user_session.post(url=url, data=payload_budj)
        data_json = response_budj.json()
        url = "https://test-bo.bars.group/bars_office/byudjeetbc/disapprove/"
        payload = {'Id': data_json["byudjeetbc"][0]['Id'], 'loadedGridFields': [], 'local_filters': []}
        response = self.user_session.post(url=url,data=payload)

        self.assertTrue(response.json()['success'], "Не работает разутверждение бюджета")

    #     утверждение
    def test_budjeetbc_onApprove(self):
        year = "2018"
        url = "https://test-bo.bars.group/bars_office/byudjeetbc/read_rows/"
        payload_budj = "{\"start\":0,\"limit\":0,\"extraParams\":{},\"filters\":[],\"additionalParams\":{\"year\":" + year + "}}"

        response_budj = self.user_session.post(url=url, data=payload_budj)
        data_json = response_budj.json()
        url = "https://test-bo.bars.group/bars_office/byudjeetbc/approve/"
        payload = {'Id': data_json["byudjeetbc"][0]['Id'], 'loadedGridFields': [], 'local_filters': []}
        response = self.user_session.post(url=url, data=payload)

        self.assertTrue(response.json()['success'], "Не работает утверждение бюджета")

    #     метод для печати
    def test_budjeetbc_print_to_exel_is200(self):
         url = "https://test-bo.bars.group/static/BarsUp/grid/multigrouping/MultigroupToExcel.js"

         response = self.user_session.get(url=url)

         self.assertEquals(response.status_code, 200, "печать не работает")

    # test recalc budjetBC
    def test_budjbc_recalc(self):
        # get budjetbc data
        year = "2018"
        url = "https://test-bo.bars.group/bars_office/byudjeetbc/read_rows/"
        payload_budj = "{\"start\":0,\"limit\":0,\"extraParams\":{},\"filters\":[],\"additionalParams\":{\"year\":" + year + "}}"

        response_budj = self.user_session.post(url=url, data=payload_budj)
        # recalc budj
        data_budj = response_budj.json()
        url = "https://test-bo.bars.group/bars_office/byudjeetbc/recalc_data/"

        payload = {'Id': data_budj["byudjeetbc"][0]['Id'], 'loadedGridFields': '[]',
                   'local_filters': '[{"groupName":"and","list_fie":[{"fie":"bc__name__icontains","symbol":"=","value":"\u0411\u0424\u041e\u0414\u0417"}]}]'}

        response = self.user_session.post( url=url, data=payload)
        data_json = response.json()
        self.assertTrue(data_json['success'], 'Ошибка в пересчете бюджета')