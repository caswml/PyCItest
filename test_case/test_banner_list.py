
import requests
import unittest


class Test_banner_list(unittest.TestCase):
	
	def test_banner_list(self):
		u'''banner列表'''
		url = 'http://120.79.31.179:8080/fastLoan.do?bannerList'
		
		headers = {
		    'Content-Type':"application/x-www-form-urlencoded"
		    }
		response = requests.request("GET", url, headers=headers).json()
		#print(dict(response))
		self.assertTrue(response['success'],'True')
		self.assertEqual(response['value'][0]['title'],'123')
		
		
if __name__ == "__main__":
	unittest.main()