### 180.  连续出现的数字

SQL框架

```mysql
Create table If Not Exists Logs (Id int, Num int)
Truncate table Logs
insert into Logs (Id, Num) values ('1', '1')
insert into Logs (Id, Num) values ('2', '1')
insert into Logs (Id, Num) values ('3', '1')
insert into Logs (Id, Num) values ('4', '2')
insert into Logs (Id, Num) values ('5', '1')
insert into Logs (Id, Num) values ('6', '2')
insert into Logs (Id, Num) values ('7', '2')
```

编写一个 SQL 查询，查找所有至少连续出现三次的数字。

| Id   | Num  |
| ---- | ---- |
| 1    | 1    |
| 2    | 1    |
| 3    | 1    |
| 4    | 2    |
| 5    | 1    |
| 6    | 2    |
| 7    | 2    |

例如，给定上面的 `Logs` 表， `1` 是唯一连续出现至少三次的数字。

| ConsecutiveNums |
| --------------- |
| 1               |



#### MySQL解题  :

```mysql
# Write your MySQL query statement below
SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1    
    AND l2.Id = l3.Id - 1  
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num

```

#### 知识点 :

方法01: 这种方法不太好,因为如果是找出连续出现20次的数字呢?

l1.Id = l2.Id - 1 AND l2.Id = l3.Id - 1  表示将三个表按照后一个id比前一个id多1的方式错位连结.

l1.Num = l2.Num AND l2.Num = l3.Num  表示连结后的表同一个数字在一行出现三次.

