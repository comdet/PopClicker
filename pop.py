# import requests
import cloudscraper
import time
import json
from random import randint
scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJDb3VudHJ5Q29kZSI6IlRIIiwiQ291bnRyeU5hbWUiOiJUaGFpbGFuZCIsIklQIjoiMTgwLjE4My4xNTMuMjMiLCJJRCI6MzAsImV4cCI6MTYyOTA0OTU0M30.ZHk25AqVJcibQQI2_FhNYgOENmFcRL-zcQ5Njd3zc-Y"
captcha_token = "03AGdBq26xxECcbynVH87SSmzzgsfciYr-URNZukFsfxpRv5P-eXqkNA4XjlZqMzmrnmD9X26qnQt40dC7Yk4y30dLTAMyIHd8KDcw_9wlEcmErG1wmdHRnsH4NN39aBV9zEgl46BzBn0bZYTlg2eMbXeczlXE31O2sQUwV6Fqf4gdRUj5G18xv0JZPrVhRkubHhzo23lWOSsvC5LSUpc_soleSWjBm9cv512aKx_3A1c1T0MifABbRcDR6y7GDeSF_F1iPedvAStYjdbkE7KOnBv67SZcKWAQORcJtoJKudBoYwMr6IzJAoNtu1KgifiUr9tOMPQ7SkF7NYQS8VVEKXGgbiJsoWimwBxrFvW5yTLtP-_WGN10R_RiV-SOWaop2JnuJqdiAZth3VowCJLA8rmLlXfu8LKNXZaZzzPOXMCVCf6YKebzkC8"
for i in range(1000):
	url = f"https://stats.popcat.click/pop?pop_count=800&captcha_token={captcha_token}&token={token}"
	res = scraper.get(url)
	if (res.text.startswith("{") and res.text.endswith("}")) or res.status_code == 201:
		res_json = json.loads(res.text)
		print(res_json)
		print("POP :O : " + res_json["Token"])
		token = res_json["Token"]
	else:
		pass
		#print("PIP :( "+ str(res.status_code))
	time.sleep(randint(100,2000)/1000) #delay a bit