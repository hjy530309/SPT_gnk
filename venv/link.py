import mysql.connector

db_config = {
    'host': '127.0.0.1',      # MySQL 호스트 주소
    'user': 'root',           # MySQL 사용자명
    'password': '1234',       # MySQL 비밀번호
    'database': 'project'     # 사용할 데이터베이스 이름
}

# MySQL 연결
conn = mysql.connector.connect(**db_config)

def user_email():
    if not conn.is_connected():
        conn.reconnect()

    # 커서 생성
    cursor = conn.cursor()

    user_sql = 'SELECT user_name FROM users'
    cursor.execute(user_sql)
    result = cursor.fetchall()

    # 커서 닫기
    cursor.close()

    return result

def pass_email():
    if not conn.is_connected():
        conn.reconnect()

    # 커서 생성
    cursor = conn.cursor()

    pass_sql = 'SELECT pass FROM users'
    cursor.execute(pass_sql)
    result = cursor.fetchall()

    # 커서 닫기
    cursor.close()

    return result

# 사용자 이름과 비밀번호 가져오기
user_names = user_email()
passwords = pass_email()

# 결과 출력 또는 활용
print("User Names:", user_names)
print("Passwords:", passwords)

# 연결 닫기
conn.close()

