from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/')
def index2():
    return render_template("signup.html")



if __name__ == '__main__':
    app.run(debug=True, port=5001)

