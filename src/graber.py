import requests
Apps = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=json").json()["applist"]["apps"][:100:]

"""INSERT INTO "Apps"("Name","Category","Views","Price","Rating","SourceCode","Functions","Tags","Size","Age","Desc","LinkToOffPage") VALUES (NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);"""
for i in Apps:
	#print(i)
	if requests.get(f"https://store.steampowered.com/api/appdetails?appids={str(i['appid'])}").json()[str(i["appid"])]["success"] == True:
		price = requests.get(f"https://store.steampowered.com/api/appdetails?appids={str(i['appid'])}").json()[str(i["appid"])]["data"]["is_free"]
		detailed_description = requests.get(f"https://store.steampowered.com/api/appdetails?appids={i['appid']}").json()[str(i["appid"])]["data"]["detailed_description"]
		sql = ""
		if price:
			sql = f'INSERT INTO "Apps"("Name","Category","Views","Price","Rating","SourceCode","Functions","Tags","Size","Age","Desc","LinkToOffPage") VALUES ("{i["name"]}","Игры",0,"бесплатно","?.?","?","Играть","Игры","Зависит от системы","?+","{detailed_description}", "https://store.steampowered.com/app/{i["appid"]}");'
		else:
			sql = f'INSERT INTO "Apps"("Name","Category","Views","Price","Rating","SourceCode","Functions","Tags","Size","Age","Desc","LinkToOffPage") VALUES ("{i["name"]}","Игры",0,"платно","?.?","?","Играть","Игры","Зависит от системы","?+","{detailed_description}", "https://store.steampowered.com/app/{i["appid"]}");'
		print(sql)