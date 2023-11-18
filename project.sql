create database project;
use project;
# 사용자 정보 테이블
CREATE TABLE users (
    user_id INT not null, 
    user_name VARCHAR(255),
    pass VARCHAR(255) not null,
    primary key(user_id)
);

#사용자 이메일 서비스를 저장하는 테이블
CREATE TABLE user_email (
    link_id INT PRIMARY KEY,
    user_id INT not null,
    service_naver VARCHAR(50) ,
    service_google VARCHAR(50) ,
    service_kakao VARCHAR(50) ,
    linked_email_address VARCHAR(255), #연동된 이메일 주소
    access_token VARCHAR(255), #엑세스 토큰
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


 #받은 메일함 테이블
 CREATE TABLE inbox (
    inbox_id INT PRIMARY KEY,
    user_id INT not null,
    sender_email_messagesemail_messagesemail VARCHAR(255), #보내는 사람
    subject_1 VARCHAR(255), #메일 제목
    body_1 TEXT, #메일 내용
    received_timestamp DATETIME, #받은 시간
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

#보낸 메일함
CREATE TABLE sent (
    sent_id INT PRIMARY KEY,
    user_id INT not null,
    recipient_email VARCHAR(255), #보내는 사람
    subject_2 VARCHAR(255),
    body_2 TEXT,
    sent_timestamp DATETIME, #보낸 시간
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

#내게쓴 메일함
CREATE TABLE my_sent_mailbox (
     me_email_id INT PRIMARY KEY,
    user_id INT,
    subject_3 VARCHAR(255),
    body_3 TEXT,
    me_timestamp DATETIME, #내게 쓴 시간
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);



