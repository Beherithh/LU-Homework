import user
from flask import Flask, request, render_template
app = Flask(__name__)
users_list = []


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        users_list.append(user.User(username, email))
        return render_template("post.html", p_username=username, p_email=email)
    else:
        return render_template("form.html")


@app.route("/")
def show_users_list():
    if len(users_list) == 0:
        return "Users list is empty"
    else:
        listforprint = []
        for i in range(len(users_list)):
            listforprint.append(users_list[i].username)
            listforprint.append(users_list[i].email)
        resp = "<br/>".join(listforprint)
        print(resp)
        return f'{resp}'


if __name__ == "__main__":
    app.run(debug=True)

