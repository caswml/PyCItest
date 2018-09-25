#coding=UTF-8
import unittest
import requests

class Test_order_state(unittest.TestCase):
	def setUp(self):
		
		self.url = "http://120.79.31.179:8080/fastLoan.do?orderState"
		self.headers = {		    
		    'Content-Type': "application/x-www-form-urlencoded",
		    }
	def test_order_state(self):
		u"""订单状态"""
		print('正常情况')
		
		url = self.url
		headers = self.headers
		data = {'appno':'20180627000001'
				
				}

		response = requests.request("POST", url=url, data=data, headers=headers).json()
		self.assertTrue(response['success'],'True')
		self.assertEqual(response['value']['currentRate'],1.8)
		#print(response)
	
if __name__ == "__main__":
	unittest.main()