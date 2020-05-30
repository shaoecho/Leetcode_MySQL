####  1327. 列出指定时间段内所有的下单产品

SQL框架

```mysql
Create table If Not Exists Products (product_id int, product_name varchar(40), product_category varchar(40))
Create table If Not Exists Orders (product_id int, order_date date, unit int)
Truncate table Products
insert into Products (product_id, product_name, product_category) values ('1', 'Leetcode Solutions', 'Book')
insert into Products (product_id, product_name, product_category) values ('2', 'Jewels of Stringology', 'Book')
insert into Products (product_id, product_name, product_category) values ('3', 'HP', 'Laptop')
insert into Products (product_id, product_name, product_category) values ('4', 'Lenovo', 'Laptop')
insert into Products (product_id, product_name, product_category) values ('5', 'Leetcode Kit', 'T-shirt')
Truncate table Orders
insert into Orders (product_id, order_date, unit) values ('1', '2020-02-05', '60')
insert into Orders (product_id, order_date, unit) values ('1', '2020-02-10', '70')
insert into Orders (product_id, order_date, unit) values ('2', '2020-01-18', '30')
insert into Orders (product_id, order_date, unit) values ('2', '2020-02-11', '80')
insert into Orders (product_id, order_date, unit) values ('3', '2020-02-17', '2')
insert into Orders (product_id, order_date, unit) values ('3', '2020-02-24', '3')
insert into Orders (product_id, order_date, unit) values ('4', '2020-03-01', '20')
insert into Orders (product_id, order_date, unit) values ('4', '2020-03-04', '30')
insert into Orders (product_id, order_date, unit) values ('4', '2020-03-04', '60')
insert into Orders (product_id, order_date, unit) values ('5', '2020-02-25', '50')
insert into Orders (product_id, order_date, unit) values ('5', '2020-02-27', '50')
insert into Orders (product_id, order_date, unit) values ('5', '2020-03-01', '50')
```

表: Products

| Column Name      | Type    |
| ---------------- | ------- |
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |

product_id 是该表主键。
该表包含该公司产品的数据。

表: Orders

| Column Name | Type |
| ----------- | ---- |
| product_id  | int  |
| order_date  | date |
| unit        | int  |

该表无主键，可能包含重复行。
product_id 是表单 Products 的外键。
unit 是在日期 order_date 内下单产品的数目。


写一个 SQL 语句，要求获取在 2020 年 2 月份下单的数量不少于 100 的产品的名字和数目。

返回结果表单的顺序无要求。

 

查询结果的格式如下：

Products 表:

| product_id | product_name          | product_category |
| ---------- | --------------------- | ---------------- |
| 1          | Leetcode Solutions    | Book             |
| 2          | Jewels of Stringology | Book             |
| 3          | HP                    | Laptop           |
| 4          | Lenovo                | Laptop           |
| 5          | Leetcode Kit          | T-shirt          |

Orders 表:

| product_id | order_date | unit |
| ---------- | ---------- | ---- |
| 1          | 2020-02-05 | 60   |
| 1          | 2020-02-10 | 70   |
| 2          | 2020-01-18 | 30   |
| 2          | 2020-02-11 | 80   |
| 3          | 2020-02-17 | 2    |
| 3          | 2020-02-24 | 3    |
| 4          | 2020-03-01 | 20   |
| 4          | 2020-03-04 | 30   |
| 4          | 2020-03-04 | 60   |
| 5          | 2020-02-25 | 50   |
| 5          | 2020-02-27 | 50   |
| 5          | 2020-03-01 | 50   |

Result 表:

| product_name       | unit |
| ------------------ | ---- |
| Leetcode Solutions | 130  |
| Leetcode Kit       | 100  |

2020 年 2 月份下单 product_id = 1 的产品的数目总和为 (60 + 70) = 130 。
2020 年 2 月份下单 product_id = 2 的产品的数目总和为 80 。
2020 年 2 月份下单 product_id = 3 的产品的数目总和为 (2 + 3) = 5 。
2020 年 2 月份 product_id = 4 的产品并没有下单。
2020 年 2 月份下单 product_id = 5 的产品的数目总和为 (50 + 50) = 100 。




#### MySQL解题  :

```mysql
-- 方法01
-- 首先子表求出2月各个product_id的unit总和 , 外层再求出unit总和>=100的product
select T.product_name, T.unit
from (
    select p.product_name, sum(unit) as unit
    from Orders o join Products p on o.product_id = p.product_id
    where order_date like "2020-02%"
    group by p.product_id
    ) as T
where sum(T.unit) >= 100

-- 方法02
select p.product_name,sum(o.unit) unit
from products p left join orders o on p.product_id = o.product_id  
where date_format(order_date,'%Y-%m') = '2020-02'
group by p.product_id
having sum(o.unit)>=100
-- 此方法用products左连接orders, 一对多.


-- 方法03
SELECT p.product_name PRODUCT_NAME, sum(t.unit) UNIT
FROM Products p,
(
    SELECT product_id, unit
    FROM Orders
    WHERE year(order_date) = 2020
    AND month(order_date) = 2
) t
WHERE p.product_id = t.product_id
GROUP BY t.product_id
HAVING UNIT >= 100;
```

#### 知识点 :

```myql
-- 找order_date是2月份的数据
where order_date like "2020-02%"
where order_date between '2020-02-01' and '2020-02-29'
where year(order_date) = 2020 and month(order_date) = 2
where date_format(order_date,'%Y-%m') = '2020-02'
```



