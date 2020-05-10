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

| Column Name  | Type    |
| ------------ | ------- |
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |

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

编写一个 SQL 查询，查询总销售额最高的销售者，如果有并列的，就都展示出来。

查询结果格式如下所示：

Product 表：

| product_id | product_name | unit_price |
| ---------- | ------------ | ---------- |
| 1          | S8           | 1000       |
| 2          | G4           | 800        |
| 3          | iPhone       | 1400       |

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

#### MySQL解题01  :

```mysql
-- 首先，要统计每个销售员的总业绩
-- 这里只是为了看一下结果而已，属于中间过程
select  seller_id, sum(price) as yeji from  Sales  group by  seller_id;

-- 然后找到这里面最高的业绩
select sum(price) as ye_ji from  Sales  group by  seller_id order by ye_ji desc limit 1;

-- 然后找到原始表中业绩与这个最高业绩相等的seller_id
select seller_id 
from Sales 
group by seller_id 
having 
	sum(price) = 
	(select sum(price) as ye_ji 
     from  Sales  
     group by  seller_id 
     order by ye_ji desc 
     limit 1);

```

#### MySQL解题02  :

```mysql
select seller_id
from Sales
group by seller_id
having 
      sum(price) >=      #这里用大于等于所有业绩中的最大值,简洁有用.
      all ( select sum(price) 
            from Sales 
            group by seller_id)
```


