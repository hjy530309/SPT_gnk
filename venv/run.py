from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
import email
import poplib
from datetime import datetime
from email.parser import BytesParser
from email import policy

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'  # MySQL 호스트
app.config['MYSQL_USER'] = 'root'  # MySQL 사용자
app.config['MYSQL_PASSWORD'] = '1234'  # MySQL 비밀번호
app.config['MYSQL_DB'] = 'project'  # MySQL 데이터베이스명
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/main', methods=['POST'])
def main():
    if request.method == 'POST':
         
        global username, password
        username = request.form['name']
        password = request.form['pwd']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (user_id, user_name, pass) VALUES (%s, %s, %s)", (9887, username, password))
        mysql.connection.commit()
        cur.close()
        
        return render_template('write.html',username = username, password = password)

    return render_template('main.html', username=username)

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        sign_user = request.form['name']
        sign_pwd = request.form['pwd']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (user_id, user_name, pass) VALUES (%s, %s, %s)", (9887, username, password))
        mysql.connection.commit()
        cur.close()

        return render_template('sign2.html')
    
app.add_url_rule('/signup', 'signup', signup) 
     
     

@app.route('/write', methods=['POST'])
def write():
    if request.method == 'POST':
        global recipient
        recipient = request.form['recipient']
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
        for i in range(num_messages):
            raw_email = b"\n".join(pop.retr(i + 1)[1])
            msg = email.message_from_bytes(raw_email)

            while msg.is_multipart():
                msg = msg.get_payload(0)
            
            subject = msg.get('subject', 'No Subject')
            from_address = msg.get('from', 'No Sender')
            date = msg.get('date', 'No Date')
            content = msg.get_payload(decode=True)
    # f = open("email_" + str(datetime.now()) + ".html", "wb")
            f = open("email_.html", "wb")
            f.write(subject)
            f.write(from_address)
            f.write(date)
            f.write(content)
            f.close()

        

        

        f.close()

    pop.close()
    
if __name__ == "__main__":
    with app.test_request_context():
          signup_url = url_for('signup')
		
    app.run(debug=True)