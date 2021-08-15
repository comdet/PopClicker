# import requests
import cloudscraper
import time
import json
from random import randint
scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJDb3VudHJ5Q29kZSI6IlRIIiwiQ291bnRyeU5hbWUiOiJUaGFpbGFuZCIsIklQIjoiMTgwLjE4My4xNTMuMjMiLCJJRCI6MzAsImV4cCI6MTYyOTA0OTU0M30.ZHk25AqVJcibQQI2_FhNYgOENmFcRL-zcQ5Njd3zc-Y"
captcha_token = "03AGdBq27u2XpAaLzTGbKTTTWbGM0ofRGfC79QEc933r5Jzml445tNYvSExkiod-6muplfyUHliz_pIUUH5jTTqffRY84N4a7i2YV2qIUs_1K7g42OwZlMzfpjrqmZ2jW8st74wTrwXewMOu1XnGC6QJ1erb8EbuX-6L1LwjiV2S4yOfX6IfaVrZO6KIsGPRfFGOzBz__hzVCL1WXei4ftwMFUnYm8ycCcVR4wZBwxuTC3jFh4hq6egtok2YHAcAZIwLk_dHK0gr1mznyCMRIwerYUMzBaNp1ZltTnP8E_0e4DSf7I29AlaKgQY-6yCtWmYwAZeGCDfI4hlpIInmj_w1atOIrCRdiSdYGL4NzgFJzXn2pMqEcYlt437cEcL2zRmzXgwhcvtTUM-QCpypRbUAg3_xRj6Prv-9C_gdX-lat0dKBN3l-nDIc"
clicked = 0
while True:
	url = "https://stats.popcat.click/pop?pop_count=800&captcha_token={captcha_token}&token={token}"
	res = scraper.get(url)
	if (res.text.startswith("{") and res.text.endswith("}")) or res.status_code == 201:
		res_json = json.loads(res.text)
		clicked += 800
		print(f"POP :O clicked : {clicked}")
		token = res_json["Token"]
	else:
		print(f"PIP :( {res.status_code}")
	time.sleep(30) #delay a bit