####  1173.  即时食物配送 I

SQL框架

```mysql
Create table If Not Exists Delivery (delivery_id int, customer_id int, order_date date, customer_pref_delivery_date date)
Truncate table Delivery
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('1', '1', '2019-08-01', '2019-08-02')
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('2', '5', '2019-08-02', '2019-08-02')
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('3', '1', '2019-08-11', '2019-08-11')
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('4', '3', '2019-08-24', '2019-08-26')
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('5', '4', '2019-08-21', '2019-08-22')
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('6', '2', '2019-08-11', '2019-08-13')
```

配送表: Delivery

| Column Name                 | Type |
| --------------------------- | ---- |
| delivery_id                 | int  |
| customer_id                 | int  |
| order_date                  | date |
| customer_pref_delivery_date | date |

delivery_id 是表的主键。
该表保存着顾客的食物配送信息，顾客在某个日期下了订单，并指定了一个期望的配送日期（和下单日期相同或者在那之后）。


如果顾客期望的配送日期和下单日期相同，则该订单称为 「即时订单」，否则称为「计划订单」。

写一条 SQL 查询语句获取即时订单所占的比例， 保留两位小数。

查询结果如下所示：

Delivery 表:

| delivery_id | customer_id | order_date | customer_pref_delivery_date |
| ----------- | ----------- | ---------- | --------------------------- |
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 5           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-11                  |
| 4           | 3           | 2019-08-24 | 2019-08-26                  |
| 5           | 4           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |

Result 表:

| immediate_percentage |
| -------------------- |
| 33.33                |

2 和 3 号订单为即时订单，其他的为计划订单。



#### MySQL解题01  : 条件判断 sum/count + case when / if

```mysql
select 
round(
    sum(case when order_date = customer_pref_delivery_date then 1 else 0 end )/ count(delivery_id)*100 
	,2) as immediate_percentage
from Delivery

-- sum(case when order_date = customer_pref_delivery_date then 1 else 0 end ) 等价于
-- sum(order_date = customer_pref_delivery_date)  
-- sum(if(order_date = customer_pref_delivery_date,1,null))
-- sum(if(order_date = customer_pref_delivery_date,1,0))
-- count(if(order_date = customer_pref_delivery_date,1,null))
-- count(case when order_date = customer_pref_delivery_date then 1 else null end)

```

#### MySQL解题02  :  直接计算

```mysql
select round(
    (select count(*) from Delivery where order_date=customer_pref_delivery_date) 
    / (select count(*) from Delivery )*100 
,2) as immediate_percentage
from Delivery
```




