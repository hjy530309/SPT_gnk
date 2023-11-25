from flask import Flask, render_template, request, session, redirect, url_for
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'project'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.secret_key = "0000"
mysql.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
   error = None
   if request.method == 'POST':
      username = request.form.get('username')  
      password = request.form.get('password')
      
      conn = mysql.connect()
      cursor = conn.cursor()
      sql = "SELECT id FROM users WHERE id = %s AND pw = %s"
      value = (username, password)  
      cursor.execute("set names utf8")
      cursor.execute(sql, value)
 
      data = cursor.fetchall()
      cursor.close()
      conn.close()
 
      for row in data:
            data = row[0]
 
      if data:
            session['login_user'] = username
            return redirect(url_for('home'))  
      else:
            error = 'Invalid input data detected!'
   return render_template('index.html', error=error)
 
 
@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        username = request.form['sign_id']  
        password = request.form['sign_pw']  

        conn = mysql.connect()
        cursor = conn.cursor()

        
        sql = "INSERT INTO users (id, pw) VALUES (%s, %s)"
        value = (username, password)
        cursor.execute(sql, value)

        if not cursor.lastrowid:  #
            conn.commit()
            return redirect(url_for('home'))  
        else:
            conn.rollback()
            return "Register Failed"

        cursor.close()
        conn.close()
    return render_template('signup.html', error=error)
 
@app.route('/index.html', methods=['GET', 'POST'])
def home():
    error = None
    username = session.get('login_user') 
    return render_template('index.html', error=error, name=username)
 
if __name__ == '__main__':
    app.run()
