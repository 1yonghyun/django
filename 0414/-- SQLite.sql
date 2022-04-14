-- SQLite
SELECT * FROM users_user;

INSERT INTO users_user
VALUES (102,"길동","김",100,"경상북도",010-1234-1234,100);

SELECT * FROM users_user;
id,first_name, last_name, age, country,phone,balance
-- 102,"길동","김",100,"경상북도",010-1234-1234,100;

-- DELETE FROM users_user
-- WHERE id=102;

SELECT * FROM users_user WHERE id=101;

UPDATE users_user
SET first_name='철수'
WHERE id=101;

SELECT first_name FROM users_user WHERE id=101;

DELETE FROM users_user
WHERE id=102;

SELECT * FROM users_user WHERE id=102;

SELECT COUNT(*) FROM users_user;

SELECT first_name FROM users_user WHERE age=30;

SELECT count(*) FROM users_user WHERE age >= 30;

SELECT COUNT(*) FROM users_user WHERE age <= 20;

SELECT COUNT(*) FROM users_user
WHERE age = 30 AND last_name = '김';