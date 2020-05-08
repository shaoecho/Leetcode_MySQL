#### 连续空余座位

SQL框架

```mysql
Create table If Not Exists cinema (seat_id int primary key auto_increment, free bool)
Truncate table cinema
insert into cinema (seat_id, free) values ('1', '1')
insert into cinema (seat_id, free) values ('2', '0')
insert into cinema (seat_id, free) values ('3', '1')
insert into cinema (seat_id, free) values ('4', '1')
insert into cinema (seat_id, free) values ('5', '1')
```

几个朋友来到电影院的售票处，准备预约连续空余座位。

你能利用表 cinema ，帮他们写一个查询语句，获取所有空余座位，并将它们按照 seat_id 排序后返回吗？

| seat_id | free |
| ------- | ---- |
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |

对于如上样例，你的查询语句应该返回如下结果。

| seat_id |
| ------- |
| 3       |
| 4       |
| 5       |
注意：

seat_id 字段是一个自增的整数，free 字段是布尔类型（'1' 表示空余， '0' 表示已被占据）。
连续空余座位的定义是大于等于 2 个连续空余的座位。

#### MySQL解题  :  使用自连接 `join` 和 `abs()`

这个问题中只有一张表，所以我们需要使用自连接 self join 来解决这个相对复杂的问题。

算法

首先，我们看看将这个表自连接后得到什么结果。

注意：将两个表连接的结果是这两个表的 笛卡尔乘积 。

```mysql
select a.seat_id, a.free, b.seat_id, b.free
from cinema a join cinema b;
```

| a.seat_id | a.free | b.seat_id | b.free |
| :-------- | ------ | --------- | ------ |
| 1         | 1      | 1         | 1      |
| 2         | 0      | 1         | 1      |
| 3         | 1      | 1         | 1      |
| 4         | 1      | 1         | 1      |
| 5         | 1      | 1         | 1      |
| 1         | 1      | 2         | 0      |
| 2         | 0      | 2         | 0      |
| 3         | 1      | 2         | 0      |
| 4         | 1      | 2         | 0      |
| 5         | 1      | 2         | 0      |
| 1         | 1      | 3         | 1      |
| 2         | 0      | 3         | 1      |
| 3         | 1      | 3         | 1      |
| 4         | 1      | 3         | 1      |
| 5         | 1      | 3         | 1      |
| 1         | 1      | 4         | 1      |
| 2         | 0      | 4         | 1      |
| 3         | 1      | 4         | 1      |
| 4         | 1      | 4         | 1      |
| 5         | 1      | 4         | 1      |
| 1         | 1      | 5         | 1      |
| 2         | 0      | 5         | 1      |
| 3         | 1      | 5         | 1      |
| 4         | 1      | 5         | 1      |
| 5         | 1      | 5         | 1      |

为了找到连续空座位，`a.seat_id` 里面的值应该大于 `b.seat_id` 且两者都应该为空。

```mysql
select a.seat_id, a.free, b.seat_id, b.free
from cinema a join cinema b    #自连接
  on abs(a.seat_id - b.seat_id) = 1    #abs()取绝对值
  and a.free = true and b.free = true;
```

| a.seat_id | a.free | b.seat_id | b.free |
| --------- | ------ | --------- | ------ |
| 4         | 1      | 3         | 1      |
| 3         | 1      | 4         | 1      |
| 5         | 1      | 4         | 1      |
| 4         | 1      | 5         | 1      |

最后，选择上表中的字段 seat_id ，并排序后返回。

注意：你可能发现 `seat_id` `4` 在表中出现了两次。这是因为座位 `4` 与 `3` 和 `5` 都相邻。所以我们需要使用 `distinct` 将重复记录筛除。

```
select distinct a.seat_id
from cinema a join cinema b
  on abs(a.seat_id - b.seat_id) = 1
  and a.free = true and b.free = true
order by a.seat_id;

```

