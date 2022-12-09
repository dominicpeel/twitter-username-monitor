import requests
import time

f = open('usernames.txt').read().strip()
usernames = [x for x in f.split('\n')]
authorization = 'Bearer ' + open('bearer.txt').read()

# Get guest token
r = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers={'authorization': authorization})
guest_token = r.json()["guest_token"]

url = f"https://twitter.com/i/api/i/users/username_available.json"
querystring = {"suggest":"false"}

while True:
	for username in usernames:
		querystring["username"] = username
		response = requests.get(url, params=querystring, headers={'Authorization': authorization, "x-guest-token": guest_token})
		result = response.json()
		print(time.strftime("%H:%M:%S", time.localtime()) + '.' + str(time.time()).split('.')[1][:3], end=" ")
		if result["valid"] == False:
			print(username + ' is taken')
		elif result["valid"] == True:
			print(username + ' is available')
		else:
			print('error: ' + str(response.status_code))
	time.sleep(60)


