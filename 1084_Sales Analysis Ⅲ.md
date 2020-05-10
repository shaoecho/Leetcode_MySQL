####  销售分析I

SQL框架

```mysql
Create table If Not Exists Product (product_id int, product_name varchar(10), unit_price int)
Create table If Not Exists Sales (seller_id int, product_id int, buyer_id int, sale_date date, quantity int, price int)
Truncate table Product
insert into Product (product_id, product_name, unit_price) values ('1', 'S8', '1000')
insert into Product (product_id, product_name, unit_price) values ('2', 'G4', '800')
insert into Product (product_id, product_name, unit_price) values ('3', 'iPhone', '1400')
Truncate table Sales
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('1', '1', '1', '2019-01-21', '2', '2000')
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('1', '2', '2', '2019-02-17', '1', '800')
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('2', '2', '3', '2019-06-02', '1', '800')
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('3', '3', '4', '2019-05-13', '2', '2800')
```

产品表：`Product`

| Column Name  | Type    |      |      |
| ------------ | ------- | ---- | ---- |
| product_id   | int     |      |      |
| product_name | varchar |      |      |
| unit_price   | int     |      |      |

product_id 是这个表的主键.

销售表：`Sales`

| Column Name | Type |
| ----------- | ---- |
| seller_id   | int  |
| product_id  | int  |
| buyer_id    | int  |
| sale_date   | date |
| quantity    | int  |
| price       | int  |

这个表没有主键，它可以有重复的行. product_id 是 Product 表的外键.

编写一个SQL查询，报告2019年春季才售出的产品。即**仅**在**2019-01-01**至**2019-03-31**（含）之间出售的商品。

查询结果格式如下所示：

Product 表：

| roduct_id | product_name | unit_price |
| --------- | ------------ | ---------- |
| 1         | S8           | 1000       |
| 2         | G4           | 800        |
| 3         | iPhone       | 1400       |

Sales 表：

| seller_id | product_id | buyer_id | sale_date  | quantity | price |
| --------- | ---------- | -------- | ---------- | -------- | ----- |
| 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
| 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
| 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |

Result 表：

| seller_id |
| --------- |
| 1         |
| 3         |

Id 为 1 和 3 的销售者，销售总金额都为最高的 2800。



#### MySQL解题01  :  用sum(表达式)=0 进行排他性筛选

```mysql
	
SELECT p.product_id,product_name 
FROM sales s,product p WHERE s.product_id=p.product_id
-- 此处用为什么FROM Sales s JOIN  Product p ON s.product_id = p.product_id会报错???
GROUP BY p.product_id
HAVING 
	SUM(sale_date < '2019-01-01')=0 
	AND 
	SUM(sale_date>'2019-03-31')=0;
```

sum(表达式) , 表达式为真时,等于1. 表达式为假时, 等于0. sum()相当于求一些系列0和1的和.

sum(sale_date < '2019-01-01')=0 时, 表示此product_id所有的sale_date都是>='2019-01-01'.





#### MySQL解题02  :  where x not in

```mysql
select product_id,product_name 
from product
where    
    product_id  not in (
        select product_id 
        from Sales 
        where sale_date >= '2019-03-31' or sale_date < '2019-01-01')
     -- where 语句还可以写成
     -- where sale_date not between '2019-01-01' and '2019-03-31'
```

仅在2019-01-01至2019-03-31（含）之间出售的商品, 即 在非2019-01-01至2019-03-31（含）之外的时间不销售.



#### MySQL解题03  :  分组后, 用having过滤数据

```mysql
SELECT p.product_id, p.product_name
FROM Sales s
JOIN Product p ON s.product_id = p.product_id
GROUP BY s.product_id
HAVING 
	MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31'
```

注意!  MIN(sale_date) > '2019-01-01'  没有等号会报错!

为啥????

题目的要求仅在 2019-01-01至2019-03-31（含）,不就是等级于> '2019-01-01' and  <= '2019-03-31'吗???

