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
    sender_email VARCHAR(255), #보내는 사람
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

INSERT INTO users (user_id, user_name, pass) VALUES
(1, 'John Doe','hashed_password_1'),
(2, 'Jane Smith', 'hashed_password_2'),
(3, 'Alice Johnson','hashed_password_3');

INSERT INTO user_email (link_id, user_id, service_naver, service_google, service_kakao, linked_email_address, access_token) VALUES
(1, 1, 'naver_token_1', 'google_token_1', 'kakao_token_1', 'john.doe@example.com', 'access_token_1'),
(2, 2, 'naver_token_2', 'google_token_2', 'kakao_token_2', 'jane.smith@example.com', 'access_token_2'),
(3, 3, 'naver_token_3', 'google_token_3', 'kakao_token_3', 'alice.johnson@example.com', 'access_token_3');

INSERT INTO sent (sent_id, user_id, recipient_email, subject_2, body_2, sent_timestamp)
VALUES
(1, 1, 'jane.doe@example.com', 'Meeting Tomorrow', 'Hi Jane, Let''s meet tomorrow!', '2023-11-17 10:00:00'),
(2, 2, 'john.smith@example.com', 'Re: Project Update', 'Sure, here is the update.', '2023-11-18 14:45:00'),
(3, 3, 'bob.jones@example.com', 'Discussion on Budget', 'Bob, we need to discuss the budget.', '2023-11-19 18:00:00');

INSERT INTO inbox (inbox_id, user_id, sender_email, subject_1, body_1, received_timestamp)
VALUES
(1, 1, 'john.doe@example.com', 'Meeting Tomorrow', 'Hi John, Let''s meet tomorrow!', '2023-11-17 10:30:00'),
(2, 2, 'jane.smith@example.com', 'Project Update', 'Jane, here is the project update.', '2023-11-18 14:45:00'),
(3, 3, 'bob.miller@example.com', 'Quick Question', 'Bob, I have a quick question for you.', '2023-11-19 18:00:00');

INSERT INTO my_sent_mailbox (me_email_id, user_id, subject_3, body_3, me_timestamp)
VALUES
(1, 1, 'Meeting Tomorrow', 'Hi Jane, Let''s meet tomorrow!', '2023-11-17 10:30:00'),
(2, 2, 'Project Update', 'Bob, here is the project update.', '2023-11-18 14:45:00'),
(3, 3, 'Quick Question', 'David, I have a quick question for you.', '2023-11-19 18:00:00');

