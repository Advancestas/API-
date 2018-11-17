import requests
import unittest 
BASE_URL ="https://bittrex.com/api/v1.1/public/getmarketsummary?market=BTC-GBG"
class testlyric(unittest.TestCase):
	def test_correct_check(self):
		r = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=BTC-GBG')
		assert(r.status_code == 200)
		print(r.status_code)
	def test_incorrect_check(self):
		r1 = requests.get('https://bittrex.com/api/v1.1/public/21313')
		assert(r1.status_code == 404)
		print(r1.status_code)
	def test_empty_check(self):
		r2 = requests.get('https://bittrex.com/api/v1.1/public/')
		assert(r2.status_code == 404)
		print(r2.status_code)
if __name__ == '__main__':
    unittest.main ()