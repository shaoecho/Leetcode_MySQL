####  订单最多的客户 

SQL框架

```mysql
Create table If Not Exists orders (order_number int, customer_number int, order_date date, required_date date, shipped_date date, status char(15), comment char(200), key(order_number))
Truncate table orders
insert into orders (order_number, customer_number) values ('1', '1')
insert into orders (order_number, customer_number) values ('2', '2')
insert into orders (order_number, customer_number) values ('3', '3')
insert into orders (order_number, customer_number) values ('4', '3')
```

在表 **orders** 中找到订单数最多客户对应的 **customer_number** 。

数据保证订单数最多的顾客恰好只有一位。

表 **orders** 定义如下：

| Column            | Type     |
| ----------------- | -------- |
| order_number (PK) | int      |
| customer_number   | int      |
| order_date        | date     |
| required_date     | date     |
| shipped_date      | date     |
| status            | char(15) |
| comment           | char(200 |

**样例输入**

| order_number | customer_number | order_date | required_date | shipped_date | status | comment |
| ------------ | --------------- | ---------- | ------------- | ------------ | ------ | ------- |
| 1            | 1               | 2017-04-09 | 2017-04-13    | 2017-04-12   | Closed |         |
| 2            | 2               | 2017-04-15 | 2017-04-20    | 2017-04-18   | Closed |         |
| 3            | 3               | 2017-04-16 | 2017-04-25    | 2017-04-20   | Closed |         |
| 4            | 3               | 2017-04-18 | 2017-04-28    | 2017-04-25   | Closed |         |

**样例输出**

| customer_number |
| --------------- |
| 3               |

解释

customer_number 为 '3' 的顾客有两个订单，比顾客 '1' 或者 '2' 都要多，因为他们只有一个订单
所以结果是该顾客的 customer_number ，也就是 3 。
进阶： 如果有多位顾客订单数并列最多，你能找到他们所有的 customer_number 吗？

#### MySQL解题  :

首先，我们使用 `GROUP BY` 选择 **customer_number** 和相应的订单数目。

```mysql
SELECT
    customer_number, COUNT(*)
FROM
    orders
GROUP BY customer_number
```

| customer_number | COUNT(*) |
| --------------- | -------- |
| 1               | 1        |
| 2               | 1        |
| 3               | 2        |

将它们按照订单数目降序排序之后，第一条记录的 **customer_number** 就是答案。

| customer_number | COUNT(*) |
| --------------- | -------- |
| 3               | 2        |

在 MySQL 中， LIMIT 语句可以被用来限制 SELECT 语句的返回行数。它需要传入 1 个或 2 个非负整数参数，第一个参数 offset 表示跳过前面多少行后开始取数据，第二个参数表示最多返回多少行的数据。默认 offset 为 0（不是 1）。

LIMIT 语句也可以只使用一个参数，这个参数的含义是从结果的第一行开始返回的行数。所以 LIMIT 1 会返回第一行的记录。

```mysql
SELECT
    customer_number
FROM
    orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
```

