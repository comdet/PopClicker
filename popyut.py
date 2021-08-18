import requests, json, time, math, warnings
warnings.filterwarnings("ignore")
while True:
	# see guild id here (line number - 1 as ID) : https://github.com/narze/popyut/blob/main/src/lib/guilds.ts
	data = { "g": 39,"n":1000,"t":str(math.floor(time.time() * 1000)) }
	res = requests.post("https://api.prayut.click/clicks", json = data,verify=False)
	if res.status_code == 200:
		res_data = json.loads(res.text)
		print(f"clicks : {res_data['total']}")
		time.sleep(10)