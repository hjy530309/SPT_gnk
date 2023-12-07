import smtplib, email, poplib
from flask import Flask, render_template, request, url_for, redirect, flash, session
from flask_mysqldb import MySQL
#from flaskext.mysql import MySQL
import pymysql.cursors
from email.message import EmailMessage
from email.mime.text import MIMEText
from datetime import datetime
from email.parser import BytesParser
from email import policy


app = Flask(__name__)
  
app.secret_key = "qwer"
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='1234',
                       db='team02_06',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
 
    if request.method == 'POST':
        user_id = request.form['name']
        user_pw = request.form['pwd']

        

        return render_template('send.html')
    return render_template('login.html', error = error)
''' 
        for row in data:
            data = row[0]
 
        if data:
            session['login_user'] = user_id
            return redirect(url_for('send'))
        else:
            error = '정보를 다시 입력해주세요'
'''
        
    

    
@app.route('/signGNK', methods=['GET','POST'])
def signGNK():
    error = None
    if request.method == 'POST':
        sign_user = request.form['user_id']
        sign_pwd = request.form['user_pw']
        sign_confirm = request.form['user_cp']

        return render_template('signG.html')


    return render_template('signGNK.html', error=error)

'''
    if request.method == 'GET':
        return render_template("signGNK.html")
    else:
        sign_user = request.form['user_id']
        sign_pwd = request.form['user_pw']
        sign_confirm = request.form['user_cp']
        
        if sign_user =='' or sign_pwd =='' or sign_confirm =='':
            flash("입력되지 않은 값이 있습니다.")
            return render_template("signGNK.html") 
        elif sign_pwd != sign_confirm:
            flash("비밀번호가 일치하지 않습니다.")
            return render_template("signGNK.html")
        else:
        
        # 기존 db에 들어있는 id와 비교하고 값 넣어야함
        cur = mysql.connection.cursor()     
        cur.execute("INSERT INTO users (user_id, user_pw) VALUES (%s, %s)", (sign_user, sign_pwd))
        mysql.connection.commit()
        cur.close()
        flash("회원가입이 완료되었습니다.", 'success')
            
        return render_template('signG.html', user_id=sign_user, user_pw=sign_pwd)
'''

@app.route('/signG', methods=['GET','POST'])
def signG():
    if request.method == 'POST':
        google_id = request.form['google_id']
        google_pw = request.form['google_pw']
        
        return render_template('signN.html')
    return render_template("signG.html")

@app.route('/signN', methods=['POST'])
def signN():
    if request.method == 'POST':
        naver_id = request.form.get('naver_id')
        naver_pw = request.form['naver_id']
        
        return render_template('signK.html')
    return render_template('signN.html')


@app.route('/signK', methods=['POST'])
def signK():
    if request.method == 'POST':
        kakao_id = request.form['kakao_id']
        kakao_pw = request.form['kakao_pw']

        return render_template('login.html')
    return render_template('signK.html')


@app.route('/write11', methods=['POST'])
def write11():
    if request.method == 'POST':
        
        subject = request.form['subject']
        message = request.form['message']
        recipient = request.form['recipient']

        # html에서 gmail, naver, kakao 값 받아 구분하고 db에서 데이터 가져오기
        # server, email, pw
        SMTP_SERVER = 'smtp.gmail.com'  # 값에 따라 주소 변경 필요
        SMTP_PORT = 465                 # SSL

        # SMTP 서버 연결
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        
        EMAIL_ADDR = 'asdf1472486@gmail.com'       # Email 아이디
        EMAIL_PASSWORD = ''      # 비번

        # SMTP 서버에 로그인
        smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)

        # MIME 형태의 이메일 메세지 작성
        msg = EmailMessage()
        msg["Subject"] = subject                 # 메일 제목
        msg["From"] = EMAIL_ADDR                # 보내는 사람
        msg["To"] = recipient     # 받는 사람
        msg.set_content(message)      # 전송 내용

        # 서버로 메일 보내기
        smtp.send_message(msg)

        # 메일을 보내면 서버와의 연결 끊기
        smtp.quit()

        
        return render_template('receive.html')

@app.route('/receive11', methods=['POST'])
def receive11():

    #smtp와 동일
    
    POP_SERVER = "pop.gmail.com"
    POP_PORT = 995

    # POP3 서버 연결
    pop = poplib.POP3_SSL(POP_SERVER, POP_PORT)

    EMAIL_ADDR = 'asdf1472486@gmail.com'        # Email 아이디
    EMAIL_PASSWORD = ''     # 비번

    pop.user(EMAIL_ADDR)
    pop.pass_(EMAIL_PASSWORD)
    pop.select()

    # 메일함에 있는 메일 수
    num_messages = len(pop.list()[1])

    # 모든 메일 읽어오기
    for i in range(num_messages):
        # 메일 번호와 메일 내용 가져오기
        response, msg_data, octets = pop.retr(i + 1)
        msg_content = b'\n'.join(msg_data).decode('utf-8')

        # 메일 파싱
        msg = BytesParser().parsebytes(msg_content.encode('utf-8'))

        # 메일 제목과 내용 출력
        raw_email = b"\n".join(pop.retr(i + 1)[1])
        msg = email.message_from_bytes(raw_email)

        while msg.is_multipart():
            msg = msg.get_payload(0)
    
        subject = msg.get('subject', 'No Subject')
        from_address = msg.get('from', 'No Sender')
        date = msg.get('date', 'No Date')
        content = msg.get_payload(decode=True)

    pop.close()
    return render_template('receive.html', subject=subject ,from_address=from_address, date=date, content=content)


@app.route('/signup')
def signup():
    return render_template("signGNK.html")

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/receive')
def receive():
    return render_template("receive.html")


@app.route('/writeme')
def writeme():
    return render_template('writeme.html')

@app.route('/writemegather')
def writemegather():
    return render_template('writemegather.html')

@app.route('/trash')
def trash():
    return render_template('trash.html')
    
@app.route('/send')
def send():
    return render_template('send.html')

if __name__ == "__main__": 
        
    app.run(debug=True, host='0.0.0.0', port=5000)
