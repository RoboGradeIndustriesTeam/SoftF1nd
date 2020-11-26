from flask import Flask, render_template, request
import sqlite3

app = Flask("LeaderOfDigital", template_folder="web", static_folder='')
db = sqlite3.connect("database.db", check_same_thread=False)
cursor = db.cursor()

@app.route("/", methods=["GET", "POST"])
def index():
    cursor.execute("SELECT * FROM Apps")
    x = cursor.fetchall()
    if request.method == "POST":
        subs = request.form.get("search")
        end_arr = []
        for i in x:
            h = i[1]
            if subs.lower() in h.lower():
                end_arr.append(i)
        print(end_arr)

        return render_template("searched.html", searchs=end_arr)
    else:
        return render_template("index.html", appsCount=int(len(x)))
@app.route("/searched")
def searched():
    return render_template("searched.html")
app.run(host='0.0.0.0', port=5555)