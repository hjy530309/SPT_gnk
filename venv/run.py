from flask import Flask, render_template, request, url_for, redirect, session
import pymysql

db= pymysql.connect(db = pymysql.connect(host='localhost', user='root', password='0000', db='project', charset='utf8'))

cursor = db.cursor() # 데이터에 접근
sql = "select * from users" # SQL query 작성
cursor.execute(sql) # SQL query 실행

# db 데이터 가져오기
cursor.fetchall()
cursor.fetchone()
cursor.fetchmany(n)

db.commit() # 수정 사항 db에 저장
db.close() # Database 닫기

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/')
def index2():
    return render_template("signup.html")



if __name__ == '__main__':
    app.run(debug=True, port=5001)

