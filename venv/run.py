from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
import email
import poplib
from datetime import datetime
from email.parser import BytesParser
from email import policy

global recipient, username, password

app = Flask(__name__)
app.secret_key = 'water7513@@' 
app.config['MYSQL_HOST'] = 'localhost'  # MySQL 호스트
app.config['MYSQL_USER'] = 'root'  # MySQL 사용자
app.config['MYSQL_PASSWORD'] = '1234'  # MySQL 비밀번호
app.config['MYSQL_DB'] = 'project'  # MySQL 데이터베이스명
mysql = MySQL(app)



@app.route('/')
def home():
    return render_template('main.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['pwd']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (user_id, user_name, pass) VALUES (%s, %s, %s)", (9887, username, password))
        mysql.connection.commit()
        cur.close()

        return render_template('write.html', username=username, password=password)

    return render_template('main.html')

@app.route('/sign1', methods=['GET','POST'])
def sign1():
    if request.method == 'POST': 
        sign_user = request.form['name']
        sign_pwd = request.form['pwd']
        sign_confirm = request.form['confirm_pwd']
        if sign_user =='' or sign_pwd =='' or sign_confirm =='':
            flash("입력되지 않은 값이 있습니다.")
            return render_template("sign1.html") 
        if sign_pwd != sign_confirm:
            flash("비밀번호가 일치하지 않습니다.")
            return render_template("sign1.html")
           
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (user_id, user_name, pass) VALUES (%s, %s, %s)", (sign_user, sign_pwd, sign_confirm))
        mysql.connection.commit()
        cur.close()

        flash("회원가입이 완료되었습니다.", 'success')
        return redirect(url_for('sign2'))

    return redirect(url_for('home'))


@app.route('/signup', methods=['GET','POST'])
def signup():
    return render_template("sign1.html")


@app.route('/sign2', methods=['POST'])
def sign2():
    if request.method == 'POST':
        service_naver = request.form['naver_id']
        naver_pwd = request.form['naver_pwd']
        naver_confirm_pwd = request.form['naver_confirm_pwd']
        return render_template('sign3.html')

    return redirect(url_for('sign1'))

@app.route('/sign3', methods=['POST'])
def sign3():
    if request.method == 'POST':
        service_naver = request.form['naver_id']
        naver_pwd = request.form['naver_pwd']
        naver_confirm_pwd = request.form['naver_confirm_pwd']
        return render_template('sign4.html')
    
    return redirect(url_for('sign2'))

@app.route('/sign4', methods=['POST'])
def sign4():
    return render_template('main.html')

@app.route('/write', methods=['POST'])
def write():
    if request.method == 'POST':
        subject = request.form['subject']
        message = request.form['message']
        SMTP_SERVER = 'smtp.gmail.com'  # smtp.naver.com / smtp.kakao.com
        SMTP_PORT = 465                 # SSL

        # SMTP 서버 연결
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        
        EMAIL_ADDR = username       # Email 아이디
        EMAIL_PASSWORD = password      # 비번

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

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sent (sent_id, user_id, recipient_email, subject_2, body_2,  sent_timestamp) VALUES (%s, %s, %s,%s, %s, %s)", (1111,2222,recipient,subject, message, '22/01/03'))
        mysql.connection.commit()
        cur.close()

        return render_template('receive.html')

@app.route('/receive', methods=['POST'])
def receive():
    
    POP_SERVER = "pop.gmail.com"
    POP_PORT = 995

    # POP3 서버 연결
    pop = poplib.POP3_SSL(POP_SERVER, POP_PORT)

    EMAIL_ADDR = username        # Email 아이디
    EMAIL_PASSWORD = password      # 비번
    EMAIL_TO = recipient          # 받는 사람

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

        # 파일 여러 번 열고 닫는 부분을 수정
        with open(f"email_{datetime.now()}.html", "w", encoding="utf-8") as f:
            f.write(f"Subject: {subject}\n")
            f.write(f"From: {from_address}\n")
            f.write(f"Date: {date}\n")
            f.write(content)

    pop.close()

if __name__ == "__main__":
    with app.test_request_context():
          signup_url = url_for('sign1')
        
    app.run(debug=True)
