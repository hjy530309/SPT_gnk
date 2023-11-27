'''
import pymysql

def link():
    link = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='project', charset='utf8')
    return link
def insert_user(user_id, user_name, password):
    a = link()
    cursor=a.cursor()

    sql = "INSERT INTO users (user_id, user_name, password) VALUES (%s, %s, %s)"
    values = (user_id, user_name, password)
    cursor.execute(sql, values)

def get_all_users():

    a = link()
    cursor = a.cursor()

    sql= "SELECT * FROM users"
    cursor.execute(sql)

    users = cursor.fetchall()

    
    a.close()

    return users
'''