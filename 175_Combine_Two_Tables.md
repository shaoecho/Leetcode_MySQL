### 175.  组合两个表

####  SQL框架

```mysql
Create table Person (PersonId int, FirstName varchar(255), LastName varchar(255))
Create table Address (AddressId int, PersonId int, City varchar(255), State varchar(255))
Truncate table Person
insert into Person (PersonId, LastName, FirstName) values ('1', 'Wang', 'Allen')
Truncate table Address
insert into Address (AddressId, PersonId, City, State) values ('1', '2', 'New York City', 'New York')
```

表1: `Person`

| 列名      | 类型    |
| --------- | ------- |
| PersonId  | int     |
| FirstName | varchar |
| LastName  | varchar |

表2: `Address`

| 列名      | 类型    |
| --------- | ------- |
| AddressId | int     |
| PersonId  | int     |
| City      | varchar |
| State     | varchar |

AddressId 是上表主键


编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，都需要基于上述两表提供 person 的以下信息：

FirstName, LastName, City, State



#### MySQL解题  :

```mysql
# Write your MySQL query statement below
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
```

#### 知识点 :

##### 1. 用left join的方式整合两个表.

Person表 >= Address表, 因为不一定每人都有地址信息, 而看题目,要求的是完全保留左表(Person表),所以用left join.

![175_1](https://raw.githubusercontent.com/shaoecho/Leetcode_MySQL/master/img/175_1.png)

##### 2. select .... from 整合后的表, 表示从整合后的表中挑选....

##### 3. on和where的区别

1) on条件是在生成临时表时使用的条件，它不管on中的条件是否为真，都会返回左边表中的记录。

2) where条件是在临时表生成好后，再对临时表进行过滤的条件。这时已经没有left join的含义（必须返回左边表的记录）了，条件不为真的就全部过滤掉。

##### 4. Truncate table Person 表示整个删除Person表

delete和truncate table的最大区别是delete可以通过WHERE语句选择要删除的记录。但执行得速度不快。而且还可以返回被删除的记录数。

而truncate table是删除整个表, 无法删除指定的记录，而且不能返回被删除的记录。但它执行得非常快。



