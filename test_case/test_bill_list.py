#coding=UTF-8
import unittest
import requests

class Test_bill_list(unittest.TestCase):
	def setUp(self):
		
		self.url = "http://120.79.31.179:8080/fastLoan.do?orderList"
		self.headers = {		    
		    'Content-Type': "application/x-www-form-urlencoded",
		    }
	def test001_bill_list(self):
		u"""提单列表"""
		print('正常情况')
		
		url = self.url
		headers = self.headers
		data = {'operator':'123456'}

		response = requests.request("POST", url=url, data=data, headers=headers).json()
		self.assertTrue(response['success'],'True')
		self.assertEqual(response['value']['datas'][0]['appno'],'20180716000010')
		#print(response)
	def test002_bill_list(self):
		print('不填operator')

		url = self.url
		headers = self.headers
		data = {'operator':''}

		response = requests.request("POST", url=url, data=data, headers=headers).json()
		self.assertFalse(response['success'],'false')
		self.assertEqual(response['message'],'[operator]无效!')
	def test003_bill_list(self):
		print('填入不存在operator')

		url = self.url
		headers = self.headers
		data = {'operator':'asd'}

		response = requests.request("POST", url=url, data=data, headers=headers).json()
		self.assertTrue(response['success'],'True')
		self.assertEqual(response['message'],'暂无数据')
if __name__ == "__main__":
	unittest.main()