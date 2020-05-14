####  订单最多的客户 

SQL框架

```mysql
Create table If Not Exists Queries (query_name varchar(30), result varchar(50), position int, rating int)
Truncate table Queries
insert into Queries (query_name, result, position, rating) values ('Dog', 'Golden Retriever', '1', '5')
insert into Queries (query_name, result, position, rating) values ('Dog', 'German Shepherd', '2', '5')
insert into Queries (query_name, result, position, rating) values ('Dog', 'Mule', '200', '1')
insert into Queries (query_name, result, position, rating) values ('Cat', 'Shirazi', '5', '2')
insert into Queries (query_name, result, position, rating) values ('Cat', 'Siamese', '3', '3')
insert into Queries (query_name, result, position, rating) values ('Cat', 'Sphynx', '7', '4')
```

查询表 Queries： 

| Column Name | Type    |      |      |
| ----------- | ------- | ---- | ---- |
| query_name  | varchar |      |      |
| result      | varchar |      |      |
| position    | int     |      |      |
| rating      | int     |      |      |

此表没有主键，并可能有重复的行。此表包含了一些从数据库中收集的查询信息。“位置”（position）列的值为 1 到 500 。“评分”（rating）列的值为 1 到 5 。评分小于 3 的查询被定义为质量很差的查询。




将查询结果的质量 quality 定义为： 各查询结果的评分与其位置之间比率的平均值。

将劣质查询百分比 poor_query_percentage 为： 评分小于 3 的查询结果占全部查询结果的百分比。



编写一组 SQL 来查找每次查询的名称(query_name)、质量(quality) 和 劣质查询百分(poor_query_percentage)。

质量(quality) 和劣质查询百分比(poor_query_percentage) 都应四舍五入到小数点后两位。

查询结果格式如下所示：

Queries table:

| query_name | result           | position | rating |
| ---------- | ---------------- | -------- | ------ |
| Dog        | Golden Retriever | 1        | 5      |
| Dog        | German Shepherd  | 2        | 5      |
| Dog        | Mule             | 200      | 1      |
| Cat        | Shirazi          | 5        | 2      |
| Cat        | Siamese          | 3        | 3      |
| Cat        | Sphynx           | 7        | 4      |

Result table:

| query_name | quality | poor_query_percentage |
| ---------- | ------- | --------------------- |
| Dog        | 2.50    | 33.33                 |
| Cat        | 0.66    | 33.33                 |

Dog 查询结果的质量为 ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
Dog 查询结果的劣质查询百分比为 (1 / 3) * 100 = 33.33

Cat 查询结果的质量为 ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
Cat 查询结果的劣质查询百分比为 (1 / 3) * 100 = 33.33



#### MySQL解题  :

```mysql
select 
query_name,
round(avg(rating /position),2) as quality,
round(SUM(IF(rating < 3, 1, 0)) * 100 / COUNT(*), 2) poor_query_percentage
-- 此处   SUM(IF(rating < 3, 1, 0)) 
-- 等价于 SUM(rating < 3)
-- 等价于 sum(case when rating<3 then 1 else 0 end)
-- 等价于 count(rating < 3 or null) 
-- 等价于 count(case when rating < 3 then 1 else null end) 
-- 等价于 count(if(rating < 3,1,null))  
-- count(rating < 3)是错误的, 统计的是整个Queries的行数.

from Queries
group by query_name
order by quality desc
```

知识点: 

1)  round(x,2) 表示x的值保留小数点后2位.

2)  sum(if(表达式, v1,0 ))  每一次表达式为真,  就加V1,累计求和.

2)  难点!  用count()进行条件计数.

```mysql
-- 例子: 要求统计表A中id小于5的行数.

-- 方法01: 
select count(id < 5) from A    #错!
select sum(id < 5) from A    #对!
-- 逐行判断id<5是否为真,若为真,相当于数值1, 若为假, 相当于数值0.
-- count(id < 5)相当于count(1,1,0,0,...) .
-- count(id < 5)的结果=count(*),算出的结果就是A表的总行数.

-- 方法01: or null
select count(id < 5 or null) from A
select sum(id < 5 or 0) from A  
-- 其实sum(id < 5 or 0)就是sum(id < 5)
-- 若id<5为真,相当于数值1,若为假,则取null.而cont(字段)不统计null.
-- 所以当不满足id<5的行数没有计入统计.

-- 方法02: case when...then...else...end
select count(case when id < 5 then 1 else null end) from A #等价于
select sum(case when id < 5 then 1 else 0 end) from A 
-- 等价于方法01, 也是讲不满足id<5的行数不计入统计.

-- 方法03: if
select count(if(id < 5,1,null)) from A   #等价于
select sum(if(id < 5,1,0)) from A
-- 原理一样,当id<5为真,值取1, 当id<5为假时,值取null. 
-- 而count()不统计null,所以当不满足id<5的行数没有计入统计.
-- count(if(id < 5,1,0))是错的, 因为count()会将0计数. 
-- sum(if(id < 5,1,0))是对的,图为0在sum()中不起作用.

-- 方法04: 先将不满足条件的行过滤掉, 然后在统计行数
select count(id) 
from A
where id < 5




```