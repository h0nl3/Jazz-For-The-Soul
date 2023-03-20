from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "b4ll3r"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login():
  if request.method == "POST":
    user = request.form['nm']
    session ["user"] = user
    return redirect(url_for("user"))
  else:
    return render_template('login.html')

@app.route('/user')
def user():
    if "user" in session:
     user = session["user"]
     return f"<h1>{user}</h1>"
    else:
     return redirect(url_for("login"))

  
@app.route('/secret')
def secret():
    return render_template("easter_egg.html")
    print("hey, why are you here? it's an easter egg.")

app.run(host='0.0.0.0', port=81)
app.run(debug = True)