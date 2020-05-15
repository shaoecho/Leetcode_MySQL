### 196.  删除重复的电子邮箱

编写一个 SQL 查询，来删除 `Person` 表中所有重复的电子邮箱，重复的邮箱里只保留 **Id** *最小* 的那个。

| Id   | Email            |
| ---- | ---------------- |
| 1    | john@example.com |
| 2    | bob@example.com  |
| 3    | john@example.com |

Id 是这个表的主键。

例如，在运行你的查询语句之后，上面的 `Person` 表应返回以下几行:

| Id   | Email            |
| ---- | ---------------- |
| 1    | john@example.com |
| 2    | bob@example.com  |

**提示：**

- 执行 SQL 之后，输出是整个 `Person` 表。
- 使用 `delete` 语句。



#### MySQL解题方法01  :

```mysql
# Write your MySQL query statement below

delete from Person    #用时900ms.
where id not in 
(select need.id from 
((select min(Id) as id from Person  group by Email) as need ))

```

#### 知识点 : 

1) 先把表中每个email组（group之后自动过滤了重复）的最小id搞出来, 这样得到需要保留的id

 	select min(Id) from Person group by Email

2) 将需要保留的id放在一个虚拟表中,取名为need,用 () as need.

3) Person需要删除的行对应的id不在need表中. delete from Person where id not in ()



#### MySQL解题方法02  :

```mysql
DELETE p1     #用时776ms
FROM 
    Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id
```

#### 知识点 :

直接找到需要删除的行. 

将此表与它自身在电子邮箱列中连接起来。

