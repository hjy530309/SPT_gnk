from flask import Flask, render_template, request, url_for, redirect, session
import pymysql
'''
db= pymysql.connect(host='localhost', user='root', password='0000', db='project', charset='utf8')

cursor = db.cursor()
sql = "select * from users"
cursor.execute(sql)

cursor.fetchall()
cursor.fetchone()
cursor.fetchmany(n)

db.commit()
db.close()
'''
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/')
def index2():
    return render_template("signup.html")



if __name__ == '__main__':
    app.run(debug=True, port=5001)

