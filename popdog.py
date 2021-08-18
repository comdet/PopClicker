import requests, json, time
import warnings
warnings.filterwarnings("ignore")
url = 'https://www.popdog.click/clicked/v2'
data = { "clicks": 2000,"uuid": "8745407d-0219-406d-ac09-058d2794b4dc","username": None}
while True:
	res = requests.post(url, json = data,verify=False)
	if res.status_code == 200:
		res_data = json.loads(res.text)
		print(f"clicks : {res_data['clicks']}")
		time.sleep(3)