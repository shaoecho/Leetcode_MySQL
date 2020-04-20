### 换座位

SQL框架

```mysql
Create table If Not Exists seat(id int, student varchar(255))
Truncate table seat
insert into seat (id, student) values ('1', 'Abbot')
insert into seat (id, student) values ('2', 'Doris')
insert into seat (id, student) values ('3', 'Emerson')
insert into seat (id, student) values ('4', 'Green')
insert into seat (id, student) values ('5', 'Jeames')
```

小美是一所中学的信息科技老师，她有一张 seat 座位表，平时用来储存学生名字和与他们相对应的座位 id。

其中纵列的 id 是连续递增的

小美想改变相邻俩学生的座位。你能不能帮她写一个 SQL query 来输出小美想要的结果呢？

| Id   | student |
| ---- | ------- |
| 1    | Abbot   |
| 2    | Doris   |
| 3    | Emerson |
| 4    | Green   |
| 5    | Jeames  |

假如数据输入的是上表，则输出结果如下：

| id   | student |
| ---- | ------- |
| 1    | Doris   |
| 2    | Abbot   |
| 3    | Green   |
| 4    | Emerson |
| 5    | Jeames  |

**注意：**

如果学生人数是奇数，则不需要改变最后一个同学的座位。

#### MySQL解题方法01 :  使用 `CASE`

算法

对于所有座位 id 是奇数的学生，修改其 id 为 id+1，如果最后一个座位 id 也是奇数，则最后一个座位 id 不修改。对于所有座位 id 是偶数的学生，修改其 id 为 id-1。

首先查询座位的数量。

```mysql
SELECT
    COUNT(*) AS counts
FROM
    seat
```

然后使用 `CASE` 条件和 `MOD` 函数修改每个学生的座位 id。

```mysql
SELECT	
    (CASE
        WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1 
     	#当此id为奇数, 且不是最后一个座位id时,修改其 id 为 id+1.
        WHEN MOD(id, 2) != 0 AND counts = id THEN id
        #当最后一个座位id为奇数时, 最后一个座位 id 不修改.
        ELSE id - 1
        #对于所有座位 id 是偶数的学生，修改其 id 为 id-1。
    END) AS id,
    student 
FROM
    seat,
    (SELECT
        COUNT(*) AS counts
    FROM
        seat) AS seat_counts
ORDER BY id ASC;  #根据id递增排序
```



#### 知识点 :

1)  case...when....else....end 的用法

```mysql
select 字段1, 字段2,       
    case 字段3     
    when 值1 then 新值       
    when 值2 then 新值      
    end as 重新命名字段3的名字       
from table      
where ……      
order by ……  
```

2) 解题框架

```mysql
select
	id,   #将id重新修改
	student
from 
	seat,
	seat_counts     
ORDER BY id ASC;  #最后形成的表要根据id递增排序
```

#### MySQL解题方法02 :   使用位操作和 `COALESCE()`

**算法**

使用 `(id+1)^1-1` 计算交换后每个学生的座位 id。

```mysql
SELECT id, (id+1)^1-1, student FROM seat;
```









```mysql


```