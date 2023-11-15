import email
import poplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from datetime import datetime

# POP3 서버 url, port
POP_SERVER = "pop.gmail.com"
POP_PORT = 995

# POP3 서버 연결
pop = poplib.POP3_SSL(POP_SERVER, POP_PORT)

EMAIL_ADDR = 'asdf1472486@gmail.com'        # Email 아이디
EMAIL_PASSWORD = "xxmi rifl vtut qyez"      # 비번
EMAIL_TO = 'asdf1472486@gmail.com'          # 받는 사람

pop.user(EMAIL_ADDR)
pop.pass_(EMAIL_PASSWORD)
numMsg = len(pop.list()[1])

for i in range(numMsg):
    raw_email = b"\n".join(pop.retr(i + 1)[1])
    msg = email.message_from_bytes(raw_email)

    while msg.is_multipart():
        msg = msg.get_payload(0)

    content = msg.get_payload(decode=True)
    # f = open("email_" + str(datetime.now()) + ".html", "wb")
    f = open("email_.html", "wb")
    f.write(content)
    f.close()

pop.close()