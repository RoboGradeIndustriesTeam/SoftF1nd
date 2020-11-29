from flask import Flask, render_template, request, jsonify
import sqlite3
import json

app = Flask("LeaderOfDigital", template_folder="web", static_folder='')
db = sqlite3.connect("database.db", check_same_thread=False)
cursor = db.cursor()
@app.route("/getAuto")
def getAuto():
    cursor.execute("SELECT * FROM Apps")
    x = cursor.fetchall()
    a = ""
    for i in range(len(x)):
        a += x[i][0]
        if i != len(x):
            a += ", "
    
    return jsonify(a)
@app.route("/app")
def appPage():
    appID = request.args.get("appID")
    print(appID)
    cursor.execute(f"SELECT * FROM Apps WHERE Name = '{appID}'")
    return render_template("app.html", app=cursor.fetchone())
@app.route("/", methods=["GET", "POST"])
def index():
    cursor.execute("SELECT * FROM Apps")
    x = cursor.fetchall()
    if request.method == "POST":
        subs = request.form.get("search")
        price = request.form.get("prc")
        source = request.form.get("src")
        end_arr = []
        cat = request.form.get("cat")
        at = list(map(str, subs.lower().split()))
        for i in x:
            h = i[0]
            l = i[1]
            z = i[6].split()
            y = i[7].split()
            o = i[10]
            """
                cat-none
                cat-office - Офис
                cat-audio - Аудио
                cat-webbrowser - Веб-браузеры
                cat-game - Игры
                cat-socialnetwork - Социальные сети
                cat-utils - Утилиты
            """
            if cat == "cat-none":
                if subs.lower() in h.lower():
                    end_arr.append(i)
                elif subs.lower() in l.lower():
                    end_arr.append(i)
                elif subs.lower() in z:
                    end_arr.append(i)
                elif subs.lower() in y:
                    end_arr.append(i)
                elif subs.lower() in o.lower():
                    end_arr.append(i)
            elif cat == "cat-office":
                if l == "Офис":
                    end_arr.append(i)
            elif cat == "cat-audio":
                if l == "Аудио":
                    end_arr.append(i)
            elif cat == "cat-webbrowser":
                if l == "Веб-браузеры":
                    end_arr.append(i)
            elif cat == "cat-game":
                if l == "Игры":
                    end_arr.append(i)
            elif cat == "cat-socialnetwork":
                if l == "Социальные сети":
                    end_arr.append(i)
            elif cat == "cat-utils":
                if l == "Утилиты":
                    end_arr.append(i)
            else:
                for j in at:
                    if ut.count(j) > 0:
                        end_arr.append(i)
            end_arra = list(reversed(sorted(end_arr, key=lambda point: (point[2]))))
        end_arrb = []
        for i in end_arra:
            if source == None or source == "src-none":
                end_arrb.append(i)
            elif source == "src-open":
                if i[5] == "открытый":
                    end_arrb.append(i)
            elif source == "src-close":
                if i[5] == "закрытый":
                    end_arrb.append(i)
        end_arrc = []
        #print(price)
        for i in end_arrb:
            if price == "prc-none" or price == None:
                end_arrc.append(i)
            elif price == "prc-free":
                if i[3] == "бесплатно":
                    end_arrc.append(i)
            elif price == "prc-middle":
                if i[3] == "бесплатно (с ограничениями)":
                    end_arrc.append(i)
            elif price == "prc-nofree":
                if i[3] == "платно":
                    end_arrc.append(i)
        return render_template("searched.html", searchs=end_arrc)
    else:
        return render_template("index.html", appsCount=int(len(x)))
@app.route("/searched")
def searched():
    return render_template("searched.html")
def lAdd(name):
    ip = request.remote_addr
    text = ""
    try:
        with open("usersLikes.json") as f:
            text += f.read()
    except FileNotFoundError:
        a = 0
    loaded : dict = json.loads(text)
    if loaded.get(name) != None:
        a = loaded[name]
        if ip not in a:
            a.append(ip)
            cursor.execute(f"SELECT Views FROM Apps WHERE Name = '{name}'")
            Views = int(cursor.fetchone()[0])
            cursor.execute(f"UPDATE Apps SET Views = {Views + 1} WHERE Name = '{name}'")
            db.commit()
        loaded[name] = a       
    else:
        loaded.update({name: [ip]})
    with open("usersLikes.json", "w") as f:
        f.write(json.dumps(loaded))
    print(loaded)
app.jinja_env.globals.update(addLike=lAdd)
app.run(host='0.0.0.0', port=5555)