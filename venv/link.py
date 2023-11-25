import pymysql


# MySQL 데이터베이스 연결
db = pymysql.connect(host='192.168.35.124', port=3306, user='sean', password='qkqh1936@@@', db='project', charset='utf8')

# 데이터에 접근
cursor = db.cursor()

# SQL query 작성
sql = "SELECT * FROM users;"

# SQL query 실행
cursor.execute(sql) 

# db 데이터 가져오기

r = cursor.fetchall() #모든 행 가져오기
cursor.fetchone() # 하나의 행만 가져오기

print(r)

# 수정 사항 db에 저장
db.commit()
 
# Database 닫기
db.close()