#coding=UTF-8
import unittest
import requests
#情况较多，暂不做
class Test_save_order(unittest.TestCase):
	def setUp(self):
		
		self.url = "http://120.79.31.179:8080/fastLoan.do?createOrder"
		self.headers = {		    
		    'Content-Type': "application/x-www-form-urlencoded",
		    }
	def test001_save_order(self):
		u"""保存订单"""
		print('正常情况')
		
		url = self.url
		headers = self.headers
		data = {'name':'测试30',
				'idCard':'610625199704110529',
				'phone':'18180470030',
				'billType':'01',
				'bankAccount':'6227003694530105004',
				'loanDate':'6',
				'operator':'123456',
				'loanAmount':'5000'
				}

		response = requests.request("POST", url=url, data=data, headers=headers).json()
		self.assertTrue(response['success'],'True')
		self.assertEqual(response['message'],'保存订单成功!')
		#print(response)
	
if __name__ == "__main__":
	unittest.main()