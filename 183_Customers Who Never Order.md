### 183.  从不订购的客户

SQL框架

```mysql
Create table If Not Exists Customers (Id int, Name varchar(255))
Create table If Not Exists Orders (Id int, CustomerId int)
Truncate table Customers
insert into Customers (Id, Name) values ('1', 'Joe')
insert into Customers (Id, Name) values ('2', 'Henry')
insert into Customers (Id, Name) values ('3', 'Sam')
insert into Customers (Id, Name) values ('4', 'Max')
Truncate table Orders
insert into Orders (Id, CustomerId) values ('1', '3')
insert into Orders (Id, CustomerId) values ('2', '1')
```

某网站包含两个表，`Customers` 表和 `Orders` 表。

编写一个 SQL 查询，找出所有从不订购任何东西的客户。

`Customers` 表：

| Id   | Name  |
| ---- | ----- |
| 1    | Joe   |
| 2    | Henry |
| 3    | Sam   |
| 4    | Max   |

`Orders` 表：

| Id   | CustomerId |
| ---- | ---------- |
| 1    | 3          |
| 2    | 1          |

例如给定上述表格，你的查询应返回：

| Customers |
| --------- |
| Henry     |
| Max       |



#### MySQL解题方法01  :

```mysql
# Write your MySQL query statement below

select a.name as Customers
from  
    Customers as a left join Orders as b     #等价于Customers a left join Orders b
    on a.Id = b.CustomerId        #左连接后,若不符合on的条件,那左边对应右边的列自动为空.
where 
    b.Id is  null

```

#### MySQL解题方法02  :

```mysql
# 这种解法更简单易懂
select name as Customers 
from Customers 
where Id not in (select CustomerId from Orders)
```



