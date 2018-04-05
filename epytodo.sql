DROP DATABASE epytodo;
CREATE DATABASE epytodo;
USE epytodo;
CREATE TABLE user (
       user_id INT(5) NOT NULL AUTO_INCREMENT,
       username VARCHAR(20) NOT NULL,
       password VARCHAR(20) NOT NULL,
       PRIMARY KEY (user_id)
);
CREATE TABLE task (
       task_id INT(5) NOT NULL AUTO_INCREMENT,
       title VARCHAR(20) NOT NULL,
       begin TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       end INT(5),
       status ENUM('not started', 'in progress', 'done') DEFAULT 'not started',
       PRIMARY KEY (task_id)
);
CREATE TABLE user_has_task(
       fk_user_id INT(5),
       fk_task_id INT(5)
       PRIMARY KEY (fk_user_id, fk_task_id)
);;
