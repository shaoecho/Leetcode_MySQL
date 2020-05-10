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

编写一个 SQL 查询，查询购买了 S8 手机却没有购买 iPhone 的买家。注意这里 S8 和 iPhone 是 Product 表中的产品。

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
| 2         | 1          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 3        | 2019-05-13 | 2        | 2800  |

Result 表：

| buyer_id |
| -------- |
| 1        |

id 为 1 的买家购买了一部 S8，但是却没有购买 iPhone，而 id 为 3 的买家却同时购买了这 2 部手机。

#### MySQL解题01  :

先用where筛除购买了iPhone的数据行 ,然后在剩下的数据行中挑选购买了S8的buyer_id.

```mysql
#此处用distinct()是因为有可能某一个buyer_id多次购买了S8
select distinct(buyer_id)  
from sales 
join product 
on sales.product_id = product.product_id
where
    product.product_name = "S8"    
    and                 # 并且buyer_id不在购买了iPhone的buyer_id中
    buyer_id not in (select buyer_id from sales join product on sales.product_id=product.product_id where product.product_name="iphone" )
```

#### MySQL解题02  :  count配合distinct使用

```mysql
select t.buyer_id 
from(
    select s.buyer_id, p.product_name
    from sales s
    inner join product p
    on s.product_id=p.product_id and (p.product_name='S8' or p.product_name='iPhone')
    group by s.buyer_id
    having count(distinct p.product_name) = 1
) t
where t.product_name='S8';
```

思路:

1) 这里比较精妙的处理是, 用count配合distinct使用. 

 count(distinct p.product_name) 统计的是购买的手机的种类, 而不是购买的次数. 

如果不加distinc,  count(p.product_name) 统计的是购买的次数. 

having count(distinct p.product_name) = 1表示只购买了一种手机

2)  思路:  

先在on s.product_id=p.product_id and (p.product_name='S8' or p.product_name='iPhone')将两个表进行内连接,  就是只保留了买S8或者买iPhone的数据(包含了只买过S8, 只买过iPhone, 两种都买过).

再having count(distinct p.product_name) = 1作为表示只购买了一种手机, 排除了两种手机都买过的数据.  此时得到中间表t, 包含的数据是只买过S8, 或者只买过iPhone这两类数据.

最后, 用where t.product_name='S8'从中间表中获取只买过S8的数据.



#### MySQL解题03  :  group_concat()函数+ instr()函数

```mysql
# Write your MySQL query statement below
select buyer_id
from sales s left join product p
using(product_id)    #等价于on s.product_id=p.product_id,在mysql中using等价于join操作中的on. 
group by buyer_id
having instr(group_concat(product_name), 'S8')>0 and instr(group_concat(product_name), 'iPhone')=0
```

先分组, 再使用group_concat(product_name), 可以把同一个buyer_id买的product_name拼接到一起. 

再用instr(源字符串, 要找的字符串) 来判断是否买了S8和iPhone.



#### MySQL解题04 :  sum(表达式)或者count(表达式 or null ) 都是用表达式 真假来筛选数据

```mysql
select buyer_id   
from Sales 
left join Product 
on Sales.product_id = Product.product_id 
group by buyer_id 
having sum(product_name='S8')>0 and sum(product_name='iPhone')=0
```

1)  先按照buyer_id 分组后, 用having+聚合函数进行过滤.

2)  此处的sum用的比较妙.

每一行数据中, 当product_name='S8'为真时, product_name='S8'相当于1, 当product_name='S8'为假时, product_name='S8'相当于0. 一个buyer_id 分组下有多行数据, 分别为0或1.

当sum(product_name='S8') >0时表示这个buyer_id买过S8. 

同理, sum(product_name='iPhone')=0表示这个buyer_id没买过iPhone. 

3)  若此处不用sum, 而是用count,应该怎么改? 

可以改为 having count(IF(product_name='S8',1,null))>0  and  count(IF(product_name='iPhone',1,null))=0

因为count()是计算总数，不管括号内是0还是1都会计入（只有NULL 不计, 所以如果想用count的话, 就要排除括号内为0的情况.

或者改为 having count(product_name='S8' or null)>0  and  count(product_name='iPhone' or null)=0



