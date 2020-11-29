import requests
f = open("proxy.txt")
proxyies = f.readlines()
f.close()
proxyiesX = []
for i in proxyies:
    proxyiesX.append(i.strip())
session = requests.Session()
session.get("http://localhost:5555/", proxies={"http":proxyiesX[0]})