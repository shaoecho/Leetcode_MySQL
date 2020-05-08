####  只出现一次的最大数字

SQL框架

```mysql
Create table If Not Exists my_numbers (num int)
Truncate table my_numbers
insert into my_numbers (num) values ('8')
insert into my_numbers (num) values ('8')
insert into my_numbers (num) values ('3')
insert into my_numbers (num) values ('3')
insert into my_numbers (num) values ('1')
insert into my_numbers (num) values ('4')
insert into my_numbers (num) values ('5')
insert into my_numbers (num) values ('6')
```

表 `my_numbers` 的 **num** 字段包含很多数字，其中包括很多重复的数字。

你能写一个 SQL 查询语句，找到只出现过一次的数字中，最大的一个数字吗？

| num  |
| ---- |
| 8    |
| 8    |
| 3    |
| 3    |
| 1    |
| 4    |
| 5    |
| 6    |

对于上面给出的样例数据，你的查询语句应该返回如下结果：

| num  |
| ---- |
| 6    |

**注意：**

如果没有只出现一次的数字，输出 **null** 。

#### MySQL解题  :  使用**子查询** 和 `MAX()` 函数

使用子查询找出仅出现一次的数字。然后使用 `MAX()` 函数找出其中最大的一个。

1) 

```mysql
SELECT num
FROM  number
GROUP BY num
```

得到下表:  默认升序排列.

| num  |
| ---- |
| 1    |
| 3    |
| 3    |
| 4    |
| 5    |
| 6    |
| 8    |
| 8    |

#用group by分组后,可以用having+ 聚合函数来过滤数据. 

此处用的是HAVING COUNT(num) = 1. 会过滤掉出现了不止一次的数字. 得到表t

| num  |
| ---- |
| 1    |
| 4    |
| 5    |
| 6    |

从t表中找到最大的一个数, 用 select max(num) from t

完整MySQL代码为

```mysql
select max(t.num) as num
from
    (select num
    from my_numbers
    group by num
    HAVING COUNT(num) = 1
    ) t
```





