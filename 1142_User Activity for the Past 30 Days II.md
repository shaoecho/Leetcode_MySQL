####  查询近30天活跃用户数

SQL框架

```mysql
Create table If Not Exists Activity (user_id int, session_id int, activity_date date, activity_type ENUM('open_session', 'end_session', 'scroll_down', 'send_message'))
Truncate table Activity
insert into Activity (user_id, session_id, activity_date, activity_type) values ('1', '1', '2019-07-20', 'open_session')
insert into Activity (user_id, session_id, activity_date, activity_type) values ('1', '1', '2019-07-20', 'scroll_down')
insert into Activity (user_id, session_id, activity_date, activity_type) values ('1', '1', '2019-07-20', 'end_session')
insert into Activity (user_id, session_id, activity_date, activity_type) values ('2', '4', '2019-07-20', 'open_session')
insert into Activity (user_id, session_id, activity_date, activity_type) values ('2', '4', '2019-07-21', 'send_message')
insert into Activity (user_id, session_id, activity_date, activity_type) values ('2', '4', '2019-07-21', 'end_session')
insert into Activity (user_id, session_id, activity_date, activity_type) values ('3', '2', '2019-07-21', 'open_session')
insert into Activity (user_id, session_id, activity_date, activity_type) values ('3', '2', '2019-07-21', 'send_message')
insert into Activity (user_id, session_id, activity_date, activity_type) values ('3', '2', '2019-07-21', 'end_session')
insert into Activity (user_id, session_id, activity_date, activity_type) values ('4', '3', '2019-06-25', 'open_session')
insert into Activity (user_id, session_id, activity_date, activity_type) values ('4', '3', '2019-06-25', 'end_session')
```

活动记录表：Activity

| Column Name   | Type |
| ------------- | ---- |
| user_id       | int  |
| session_id    | int  |
| activity_date | date |
| activity_type | enum |

该表是用户在社交网站的活动记录。
该表没有主键，可能包含重复数据。
activity_type 字段为以下四种值 ('open_session', 'end_session', 'scroll_down', 'send_message')。
每个 session_id 只属于一个用户。

编写SQL查询以查找截至2019年7月27日（含）的30天内每个用户的平均会话数，四舍五入到小数点后两位。我们只统计那些会话期间用户至少进行一项活动的有效会话。

查询结果示例如下：

Activity table:

| user_id | session_id | activity_date | activity_type |
| ------- | ---------- | ------------- | ------------- |
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 2       | 4          | 2019-07-21    | end_session   |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | end_session   |
| 3       | 5          | 2019-07-21    | open_session  |
| 3       | 5          | 2019-07-21    | croll_down    |
| 3       | 5          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |

Result table:

| average_sessions_per_user |
| ------------------------- |
| 1.33                      |

User 1 和 2 在过去30天内各自进行了1次会话，而用户3进行了2次会话，因此平均值为（1 +1 + 2）/ 3 = 1.33。

#### MySQL解题  :

本题的重点就是要理解每个用户的平均会话数。即：COUNT(session_id) / COUNT(user_id)
这个数字还需要加工处理：

由于表里面可能有重复的数据，所以需要使用 DISTINCT 去重。
使用 ROUND(x,2) 保留x小数点后两位数字。
使用 IFNULL(x,0)  x为null时,替换为0.
只需要查找截至 2019-07-27 日（含）的 30 天内的数据，有两种办法（注意是截至不是截止）：
计算出第一天，使用 BETWEEN ：WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'。
使用 datediff() 函数，计算当天与最后一天的差值：WHERE datediff('2019-07-27',activity_date) < 30。

```mysql
select  
	IFNULL(round(COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id) ,2) ,0)
	as average_sessions_per_user 
from Activity
where datediff('2019-07-27', activity_date) < 30
-- WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'  #between...and..包含左右边界. 
-- WHERE activity_dateBETWEEN DATE_SUB("2019-07-27", INTERVAL 29 DAY) AND "2019-07-27"因为包含2019-07-2, 所以减去时间间隔的时候, 少减去了1天, 减29天, 而不是30天.
```

