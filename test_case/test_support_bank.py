#coding=UTF-8
import unittest
import requests

class Test_support_bank(unittest.TestCase):
	def test_support_bank(self):
		u"""支持银行"""
		url = "http://120.79.31.179:8080/fastLoan.do?supportBank"
		headers = {
		    'Content-Type': "application/json",
		    'Cache-Control': "no-cache",
		    'Postman-Token': "3e7aa835-5aeb-48bd-92cc-4c1be7d408e8"
		    }

		response = requests.request("GET", url, headers=headers).json()
		#print(response)
		self.assertTrue(response['success'],'True')
		self.assertEqual(response['value'][0]['bankName'],'中国银行')
if __name__ == "__main__":
	unittest.main()