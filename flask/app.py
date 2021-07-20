from markupsafe import escape

from flask import Flask

app = Flask(__name__)
l = []

@app.route("/add/<string:text>")
def hello_world(text):
    l.append(text)
    return f"<p>Added, {escape(text)} to the list!</p>"

@app.route("/list")
def get_list():
    concat_string = "".join(l)
    return f"<p>Concatenated String is : {concat_string}</p>"

if __name__ == "__main__":
    app.run()
