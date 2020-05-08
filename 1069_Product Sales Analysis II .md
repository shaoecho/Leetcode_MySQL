####  产品销售分析 II

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

编写一个 SQL 查询，按产品 id `product_id` 来统计每个产品的销售总量。

示例：

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

| product_id | total_quantity |
| ---------- | -------------- |
| 100        | 22             |
| 200        | 15             |

#### MySQL解题  :

```mysql
select 
    product_id, 
    sum(quantity) as total_quantity
from Sales
group by product_id 
```



