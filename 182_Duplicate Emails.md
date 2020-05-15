### 182.  查找重复的电子邮箱

SQL框架

```mysql
Create table If Not Exists Person (Id int, Email varchar(255))
Truncate table Person
insert into Person (Id, Email) values ('1', 'a@b.com')
insert into Person (Id, Email) values ('2', 'c@d.com')
insert into Person (Id, Email) values ('3', 'a@b.com')
```

编写一个 SQL 查询，查找 `Person` 表中所有重复的电子邮箱。

| Id   | Email   |
| ---- | ------- |
| 1    | a@b.com |
| 2    | c@d.com |
| 3    | a@b.com |

根据以上输入，你的查询应返回以下结果：

| Email   |
| ------- |
| a@b.com |

**说明：**所有电子邮箱都是小写字母。

#### MySQL解题方法01  :

```mysql
# Write your MySQL query statement below
select a.Email 
from
	Person as a,
    Person as b
where
    a.Email = b.Email
```

#### MySQL解题方法02  :

```mysql
select Email
from Person
group by Email
having count(Email) > 1;
```

#### 知识点 :

1)  执行顺序  where>group by>having>order by

2)  where 后不能跟聚合函数子句的作用是在对查询结果进行分组前，将不符合where条件的行去掉 .

3)  having 子句的作用是筛选满足条件的组，即在分组之后过滤数据，条件中经常包含聚组函数

