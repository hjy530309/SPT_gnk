<<<<<<< Updated upstream
from flask import Flask, render_template
=======
import pymysql
from flask import Flask, render_template, request
>>>>>>> Stashed changes


users_db = pymysql.connect(
    user='root', 
    passwd='1234', 
    host='127.0.0.1', 
    db='project', 
    charset='utf8'
)

#cursor = sensor_db.cursor(pymysql.cursors.DictCursor)
cursor = users_db.cursor()

#sql = "DELETE FROM sensor WHERE _id = 2;"
sql = "SELECT * FROM users"


cursor.execute(sql)


data_list = cursor.fetchall()


#Flask 객체 인스턴스 생성
app = Flask(__name__)

<<<<<<< Updated upstream
@app.route('/')
def home():
    return render_template('sign1.html')

if __name__ == '__main__':
    app.run(debug=True)

'''
mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'project'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.secret_key = "ABCDEFG"
mysql.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
 
    if request.method == 'POST':
        Username = request.form['Username']
        password = request.form['password']
 
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
            return redirect(url_for('home'))
        else:
            error = 'invalid input data detected !'
    return render_template('main.html', error = error)
 
 
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        id = request.form['regi_id']
        pw = request.form['regi_pw']
 
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
    return render_template('register.html', error=error)
 
@app.route('/home.html', methods=['GET', 'POST'])
def home():
    error = None
    id = session['login_user']
    return render_template('home.html', error=error, name=id)
 
if __name__ == '__main__':
    app.run()

'''    
=======
@app.route('/') # 접속하는 url
def signup():
    
    sql = "SELECT * from users"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    
    
    return render_template('signup.html',data_list=data_list)
    
if __name__=="__main__":
    #app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    app.run(host="0.0.0.0", port="80", debug=True)
>>>>>>> Stashed changes
