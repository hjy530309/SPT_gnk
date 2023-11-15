import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText

# STMP 서버 url, port
SMTP_SERVER = 'smtp.gmail.com'  # smtp.naver.com / smtp.kakao.com
SMTP_PORT = 465                 # SSL

# SMTP 서버 연결
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

EMAIL_ADDR = 'asdf1472486@gmail.com'        # Email 아이디
EMAIL_PASSWORD = 'xxmi rifl vtut qyez'      # 비번

# SMTP 서버에 로그인
smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)

# MIME 형태의 이메일 메세지 작성
message = EmailMessage()
message["Subject"] = "Test"                 # 메일 제목
message["From"] = EMAIL_ADDR                # 보내는 사람
message["To"] = 'asdf1472486@gmail.com'     # 받는 사람
message.set_content('Test Send Email')      # 전송 내용


# 서버로 메일 보내기
smtp.send_message(message)

# 메일을 보내면 서버와의 연결 끊기
smtp.quit()
