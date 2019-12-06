import requests
import unittest
# noinspection PyUnresolvedReferences
import json
class login(unittest.TestCase):
    def setUp(self):
        self.base_url='http://worldcreator.ksmobile.com/v1/getToken'
    def test_get_sucess(self):
        datalist={'dID':'b727bea5b9f26b859892cd1898e4cb33'
                  }
        headers={'Content-Type': 'application/json'
                 }
        r=requests.post(self.base_url,json=datalist,headers=headers)

        result=r.json()
        print(result['result']['token'])
        #self.assertEqual(result['result']['uuid'],'76a95389e00d48719dfcba020775eb64')


if __name__== '__main__':
    unittest.main()