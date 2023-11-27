'''
from flask import Flask, session, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)
 
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'project'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = "ABCDEFG"
mysql.init_app(app)
 
@app.route('/', methods=['GET', 'POST'])
def main():
    error = None
 
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
 
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "SELECT id FROM users WHERE id = %s AND pw = %s"
        value = (id, pw)
        cursor.execute("set names utf8")
        cursor.execute(sql, value)
 
        data = cursor.fetchall()
        cursor.close()
        conn.close()
 
        for row in data:
            data = row[0]
 
        if data:
            session['login_user'] = id
            return redirect(url_for('main'))
        else:
            error = 'invalid input data detected !'
    return render_template('main.html', error = error)
 
 
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        id = request.form['login_id']
        pw = request.form['login_pw']
 
        conn = mysql.connect()
        cursor = conn.cursor()
 
        sql = "INSERT INTO users VALUES ('%s', '%s')" % (id, pw)
        cursor.execute(sql)
 
        data = cursor.fetchall()
 
        if not data:
            conn.commit()
            return redirect(url_for('main'))
        else:
            conn.rollback()
            return "Register Failed"
 
        cursor.close()
        conn.close()
    return render_template('login.html', error=error)
 
if __name__ == '__main__':
    app.run()
'''

from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'  # MySQL 호스트
app.config['MYSQL_USER'] = 'root'  # MySQL 사용자
app.config['MYSQL_PASSWORD'] = '1234'  # MySQL 비밀번호
app.config['MYSQL_DB'] = 'project'  # MySQL 데이터베이스명
mysql = MySQL(app)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/index', methods=['POST'])
def index():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['pwd']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (user_id, user_name, pass) VALUES (%s, %s, %s)", (5, username, password))
        mysql.connection.commit()
        cur.close()
      
        return render_template('write.html',username = username, password = password)

    return render_template('main.html', username=username)

@app.route('/receive', methods=['POST'])
def receive():
    


if __name__ == '__main__':
    app.run(debug=True)
