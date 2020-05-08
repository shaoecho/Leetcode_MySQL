####  直线上的最近距离

SQL框架

```mysql
CREATE TABLE If Not Exists point (x INT NOT NULL, UNIQUE INDEX x_UNIQUE (x ASC))
Truncate table point
insert into point (x) values ('-1')
insert into point (x) values ('0')
insert into point (x) values ('2')
```

表 point` 保存了一些点在 x 轴上的坐标，这些坐标都是整数。

写一个查询语句，找到这些点中最近两个点之间的距离。

| x    |
| ---- |
| -1   |
| 0    |
| 2    |

最近距离显然是 '1' ，是点 '-1' 和 '0' 之间的距离。所以输出应该如下：

| shortest |
| -------- |
| 1        |


注意：每个点都与其他点坐标不同，表 table 不会有重复坐标出现。

进阶：如果这些点在 x 轴上从左到右都有一个编号，输出结果时需要输出最近点对的编号呢？

#### MySQL解题  :

为了得到每两对点之间的距离，我们需要将这个表与它自己做连接，然后使用 ABS() 函数。有一个小技巧是我们在计算距离的时候增加一个判断条件，来避免一个点与它自己计算距离。

```mysql
SELECT
    p1.x, p2.x, ABS(p1.x - p2.x) AS distance
FROM
    point p1
        JOIN
    point p2 ON p1.x != p2.x
;
```

注意：列 p1.x 和 p2.x 只是为了展示目的，它们在最后的输出中并不是必须的。

拿样例数据举例，输出应该如下。

| x    | x    | distance |
| ---- | ---- | -------- |
| 0    | -1   | 1        |
| 2    | -1   | 3        |
| -1   | 0    | 1        |
| 2    | 0    | 2        |
| -1   | 2    | 3        |
| 0    | 2    | 2        |

最后，我们使用 `MIN()` 选出 *distance* 列中的最小值。

```mysql
SELECT
    MIN(ABS(p1.x - p2.x)) AS shortest
FROM
    point p1
    JOIN point p2 
    ON p1.x != p2.x   
;
```

或

```mysql
select min(a.distance) AS shortest   #没有上一个简洁
from 
    (select 
        abs(p1.x -p2.x) as distance
    from 
        point p1 
        join point p2 
        on p1.x != p2.x
    order by distance
    ) a

```



