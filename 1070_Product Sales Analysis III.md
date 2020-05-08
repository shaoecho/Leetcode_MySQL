####  产品销售分析III 

SQL框架

```mysql
Create table Sales (sale_id int, product_id int, year int, quantity int, price int)
Create table Product (product_id int, product_name varchar(10))
Truncate table Sales
insert into Sales (sale_id, product_id, year, quantity, price) values ('1', '100', '2008', '10', '5000')
insert into Sales (sale_id, product_id, year, quantity, price) values ('2', '100', '2009', '12', '5000')
insert into Sales (sale_id, product_id, year, quantity, price) values ('7', '200', '2011', '15', '9000')
Truncate table Product
insert into Product (product_id, product_name) values ('100', 'Nokia')
insert into Product (product_id, product_name) values ('200', 'Apple')
insert into Product (product_id, product_name) values ('300', 'Samsung')
```

销售表 `Sales`：

| Column Name | Type |
| ----------- | ---- |
| sale_id     | int  |
| product_id  | int  |
| year        | int  |
| quantity    | int  |
| price       | int  |

sale_id 是销售表 Sales 的主键.   product_id 是产品表 Product 的外键.  注意: price 表示每单位价格

产品表 `Product`：

| Column Name  | Type    |      |
| ------------ | ------- | ---- |
| product_id   | int     |      |
| product_name | varchar |      |

product_id 是表的主键.

编写一个 SQL 查询，选出每个销售产品的 **第一年** 的 **产品 id**、**年份**、**数量** 和 **价格**。

查询结果格式如下：

Sales 表：

| sale_id | product_id | year | quantity | price |
| ------- | ---------- | ---- | -------- | ----- |
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |

Product 表：

| product_id | product_name |
| ---------- | ------------ |
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |

Result 表 :  

| product_id | first_year | quantity | price |
| ---------- | ---------- | -------- | ----- |
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |

#### MySQL解题 01  :窗口函数

```mysql
select  
    product_id, year as first_year, quantity, price
from 
    (select 
        product_id, 
        year as first_year, 
        quantity,
        price,
        dense_rank() over (partition by player_id order by year) rnk
    from Sales
    ) t
where rnk =1
```

用窗口函数增加一列rnk ,rnk=1时表示每个销售产品的 第一年. 

MySQL8.0+才有窗口函数.

#### 错误解法  :

虽然先进行了分组, 但是limit 1取的并不是每个分组内的1个数据, 还是整个Sales表的数据.

```mysql
select  
    product_id, year as first_year, quantity,price
from 
    (select *
     from Sales
     group by product_id
     order by year
     limit 1   
    ) t
```

#### MySQL解题 02  :

```mysql
select 
	product_id,year as first_year,quantity,price 
from Sales 
where 
    (product_id,year) 
    in 
    (select product_id,min(year) from Sales group by product_id)
```

select product_id,min(year) from Sales group by product_id 得到下表

| sale_id | product_id | year | quantity | price |
| ------- | ---------- | ---- | -------- | ----- |
| 1       | 100        | 2008 | 10       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |

用where 来进行过滤数据