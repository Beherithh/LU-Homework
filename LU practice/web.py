from datetime import datetime
from flask import Flask, render_template, request

application = Flask(__name__)


@application.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        time = datetime.now()

        return render_template("post.html",
                               title=title,
                               time=time,
                               content=content)

    return render_template("form.html")


application.run(debug=True)
