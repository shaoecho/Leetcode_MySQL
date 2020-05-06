####  寻找用户推荐人 

SQL框架

```mysql
CREATE TABLE IF NOT EXISTS customer (id INT,name VARCHAR(25),referee_id INT);
Truncate table customer
insert into customer (id, name, referee_id) values ('1', 'Will', 'None')
insert into customer (id, name, referee_id) values ('2', 'Jane', 'None')
insert into customer (id, name, referee_id) values ('3', 'Alex', '2')
insert into customer (id, name, referee_id) values ('4', 'Bill', 'None')
insert into customer (id, name, referee_id) values ('5', 'Zack', '1')
insert into customer (id, name, referee_id) values ('6', 'Mark', '2')
```

给定表 `customer` ，里面保存了所有客户信息和他们的推荐人。

| id   | name | referee_id |
| ---- | ---- | ---------- |
| 1    | Will | NULL       |
| 2    | Jane | NULL       |
| 3    | Alex | 2          |
| 4    | Bill | NULL       |
| 5    | Zack | 1          |
| 6    | Mark | 2          |

写一个查询语句，返回一个编号列表，列表中编号的推荐人的编号都 **不是** 2。

对于上面的示例数据，结果为：

| name |
| ---- |
| Will |
| Jane |
| Bill |
| Zack |

#### MySQL解题  :

```mysql
SELECT name 
FROM customer 
WHERE referee_id != 2 OR referee_id IS NULL;
```

#### 知识点 :

MySQL 使用三值逻辑 —— TRUE, FALSE 和 UNKNOWN。任何与 NULL 值进行的比较都会与第三种值 UNKNOWN 做比较。这个“任何值”包括 NULL 本身！这就是为什么 MySQL 提供 IS NULL 和 IS NOT NULL 两种操作来对 NULL 特殊判断。

因此，在 WHERE 语句中我们需要做一个额外的条件判断 `referee_id IS NULL'。

