#### 行程和用户 

SQL框架

```mysql
Create table If Not Exists Trips (Id int, Client_Id int, Driver_Id int, City_Id int, Status ENUM('completed', 'cancelled_by_driver', 'cancelled_by_client'), Request_at varchar(50))
Create table If Not Exists Users (Users_Id int, Banned varchar(50), Role ENUM('client', 'driver', 'partner'))
Truncate table Trips
insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('1', '1', '10', '1', 'completed', '2013-10-01')
insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01')
insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('3', '3', '12', '6', 'completed', '2013-10-01')
insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('4', '4', '13', '6', 'cancelled_by_client', '2013-10-01')
insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('5', '1', '10', '1', 'completed', '2013-10-02')
insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('6', '2', '11', '6', 'completed', '2013-10-02')
insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('7', '3', '12', '6', 'completed', '2013-10-02')
insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('8', '2', '12', '12', 'completed', '2013-10-03')
insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('9', '3', '10', '12', 'completed', '2013-10-03')
insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03')
Truncate table Users
insert into Users (Users_Id, Banned, Role) values ('1', 'No', 'client')
insert into Users (Users_Id, Banned, Role) values ('2', 'Yes', 'client')
insert into Users (Users_Id, Banned, Role) values ('3', 'No', 'client')
insert into Users (Users_Id, Banned, Role) values ('4', 'No', 'client')
insert into Users (Users_Id, Banned, Role) values ('10', 'No', 'driver')
insert into Users (Users_Id, Banned, Role) values ('11', 'No', 'driver')
insert into Users (Users_Id, Banned, Role) values ('12', 'No', 'driver')
insert into Users (Users_Id, Banned, Role) values ('13', 'No', 'driver')
```

Trips 表中存所有出租车的行程信息。

每段行程有唯一键 Id，Client_Id 和 Driver_Id 是 Users 表中 Users_Id 的外键。

Status 是枚举类型，枚举成员为 (‘completed’, ‘cancelled_by_driver’, ‘cancelled_by_client’)。

| Id   | Client_Id | Driver_Id | City_Id | Status              | Request_at |
| ---- | --------- | --------- | ------- | ------------------- | ---------- |
| 1    | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2    | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3    | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4    | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5    | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6    | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7    | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8    | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9    | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10   | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |

Users 表存所有用户。每个用户有唯一键 Users_Id。Banned 表示这个用户是否被禁止，Role 则是一个表示（‘client’, ‘driver’, ‘partner’）的枚举类型。

| Users_Id | Banned | Role   |
| -------- | ------ | ------ |
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |

写一段 SQL 语句查出 2013年10月1日 至 2013年10月3日 期间非禁止用户的取消率。基于上表，你的 SQL 语句应返回如下结果，取消率（Cancellation Rate）保留两位小数。

取消率的计算方式如下：(被司机或乘客取消的非禁止用户生成的订单数量) / (非禁止用户生成的订单总数)

| Day        | Cancellation Rate |
| ---------- | ----------------- |
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |

#### MySQL解题01  :

```mysql
# Write your MySQL query statement below
SELECT
    request_at 'Day', round(avg(Status!='completed'), 2) 'Cancellation Rate'
FROM 
    trips t 
    JOIN users u1 ON (t.client_id = u1.users_id AND u1.banned = 'No')
    JOIN users u2 ON (t.driver_id = u2.users_id AND u2.banned = 'No')
WHERE	
    request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
    request_at
```

解题思路

- 对trips表和users表连接，连接条件是行程对应的乘客非禁止且司机非禁止.

- 筛选订单日期在目标日期之间

- 用日期进行分组

- 对订单取消率保留两位小数，round(x, 2) 

- 分别统计所有订单数和被取消的订单数，其中取消订单数用一个bool条件来得到0或1，再用avg求均值

- Status!='completed'为真时为1,即取消订单时为1, 不取消订单时为0.  avg(Status!='completed')表示求多个0和1的平均，最后得到的就是1的比例.

  

#### MySQL解题02 :

对client_id和driver_id各自关联的users_id，**同时检测**是否被禁止。

```mysql
SELECT *
FROM Trips AS T
JOIN Users AS U1 ON (T.client_id = U1.users_id AND U1.banned ='No')
JOIN Users AS U2 ON (T.driver_id = U2.users_id AND U2.banned ='No')
```

在此基础上，按日期分组，统计每组的 总行程数，取消的行程数 。

每组的总行程数：COUNT(T.STATUS)。

每组的取消的行程数：

```
SUM(IF(T.STATUS = 'completed',0,1))
```

**取消率** = 每组的取消的行程数 / 每组的总行程数

完整逻辑为:

```mysql
SELECT T.request_at AS `Day`, 
	ROUND(SUM(IF(T.STATUS = 'completed',0,1)) / COUNT(T.STATUS),2) AS `Cancellation Rate`
FROM Trips AS T
JOIN Users AS U1 ON (T.client_id = U1.users_id AND U1.banned ='No')
JOIN Users AS U2 ON (T.driver_id = U2.users_id AND U2.banned ='No')
WHERE T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T.request_at
```

其中[SUM求和函数，COUNT计数函数](http://www.mysqltutorial.org/mysql-aggregate-functions.aspx)，[ROUND四舍五入函数](http://www.mysqltutorial.org/mysql-math-functions/mysql-round/)。







