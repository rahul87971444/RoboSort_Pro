from flask import Flask, render_template, request, redirect, session, jsonify
from dashboard_data import read_data, write_data

app = Flask(__name__)
app.secret_key = "robosort_secret_key"

# =====================================
# LOGIN CREDENTIALS
# =====================================

ADMIN_USER = "admin"
ADMIN_PASS = "admin123"

VIEWER_USER = "viewer"
VIEWER_PASS = "viewer123"

# =====================================
# LOGIN PAGE
# =====================================

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == ADMIN_USER and password == ADMIN_PASS:
            session["role"] = "admin"
            return redirect("/admin")

        elif username == VIEWER_USER and password == VIEWER_PASS:
            session["role"] = "viewer"
            return redirect("/viewer")

        return render_template(
            "login.html",
            error="Invalid Username or Password"
        )

    return render_template("login.html")


# =====================================
# ADMIN DASHBOARD
# =====================================

@app.route("/admin")
def admin_dashboard():
    if session.get("role") != "admin":
        return redirect("/")

    return render_template("admin_dashboard.html")


# =====================================
# VIEWER DASHBOARD
# =====================================

@app.route("/viewer")
def viewer_dashboard():
    if session.get("role") != "viewer":
        return redirect("/")

    return render_template("viewer_dashboard.html")

@app.route("/logs")
def logs():

    if session.get("role") != "admin":
        return redirect("/")

    try:

        with open("sorting_logs.txt", "r") as file:

            log_data = file.readlines()

    except:

        log_data = []

    return render_template(
        "logs.html",
        logs=log_data[::-1]
    )


# =====================================
# LOGOUT
# =====================================

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# =====================================
# STATUS API
# =====================================

@app.route("/status")
def status():
    return jsonify(read_data())


# =====================================
# ADMIN CONTROL API
# =====================================

@app.route("/move/<action>")
def move(action):
    if session.get("role") != "admin":
        return "Unauthorized", 403

    data = read_data()

    if action == "start":
        data["robot_arm_status"] = "Running"

    elif action == "stop":
        data["robot_arm_status"] = "Stopped"

    elif action == "reset":
        data["robot_arm_status"] = "Stopped"
        data["current_object"] = "Waiting..."
        data["weight"] = 0

        categories = [
            "black_small_circle_light",
            "black_small_circle_heavy",
            "black_big_circle_light",
            "black_big_circle_heavy",
            "white_small_circle_light",
            "white_small_circle_heavy",
            "white_big_circle_light",
            "white_big_circle_heavy",
            "black_small_rectangle_light",
            "black_small_rectangle_heavy",
            "black_big_rectangle_light",
            "black_big_rectangle_heavy",
            "white_small_rectangle_light",
            "white_small_rectangle_heavy",
            "white_big_rectangle_light",
            "white_big_rectangle_heavy"
        ]

        for category in categories:
            if category in data:
                data[category] = 0

    write_data(data)
    return "OK"


# =====================================
# RUN FLASK
# =====================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )

