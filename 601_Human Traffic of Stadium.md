#### 体育馆的人流量

SQL框架

```mysql
Create table If Not Exists stadium (id int, visit_date DATE NULL, people int)
Truncate table stadium
insert into stadium (id, visit_date, people) values ('1', '2017-01-01', '10')
insert into stadium (id, visit_date, people) values ('2', '2017-01-02', '109')
insert into stadium (id, visit_date, people) values ('3', '2017-01-03', '150')
insert into stadium (id, visit_date, people) values ('4', '2017-01-04', '99')
insert into stadium (id, visit_date, people) values ('5', '2017-01-05', '145')
insert into stadium (id, visit_date, people) values ('6', '2017-01-06', '1455')
insert into stadium (id, visit_date, people) values ('7', '2017-01-07', '199')
insert into stadium (id, visit_date, people) values ('8', '2017-01-08', '188')
```

X 市建了一个新的体育馆，每日人流量信息被记录在这三列信息中：序号 (id)、日期 (visit_date)、 人流量 (people)。

请编写一个查询语句，找出人流量的高峰期。高峰期时，至少连续三行记录中的人流量不少于100。

例如，表 stadium：

| Id   | visit_date | people |
| ---- | ---------- | ------ |
| 1    | 2017-01-01 | 10     |
| 2    | 2017-01-02 | 109    |
| 3    | 2017-01-03 | 150    |
| 4    | 2017-01-04 | 99     |
| 5    | 2017-01-05 | 145    |
| 6    | 2017-01-06 | 1455   |
| 7    | 2017-01-07 | 199    |
| 8    | 2017-01-08 | 188    |

对于上面的示例数据，输出为：

| id   | visit_date | people |
| ---- | ---------- | ------ |
| 5    | 2017-01-05 | 145    |
| 6    | 2017-01-06 | 1455   |
| 7    | 2017-01-07 | 199    |
| 8    | 2017-01-08 | 188    |

**提示：**
每天只有一行记录，日期随着 id 的增加而增加。

#### MySQL解题01  :

先将哪些连续三天客流量都>=100的行找出来。

表三次连接。结果命名为表A。

```mysql
(
	SELECT S1.id AS `id1`,S2.id AS `id2`,S3.id AS `id3`
	FROM stadium AS S1
	JOIN stadium AS S2 ON(S1.id +1 = S2.id AND S1.people >=100 AND S2.people >=100)
	JOIN stadium AS S3 ON(S2.id +1 = S3.id AND S2.people >=100 AND S3.people >=100)
) AS A

```

那么，id1，id2，id3都是满足条件的行号。

与表Stadium连接。取出id1或id2或id3对应的行，但可能有些行重复取，要去重。

```mysql
SELECT DISTINCT S.*
FROM 
(
	SELECT S1.id AS `id1`,S2.id AS `id2`,S3.id AS `id3`
	FROM stadium AS S1
	JOIN stadium AS S2 ON(S1.id +1 = S2.id AND S1.people >=100 AND S2.people >=100)
	JOIN stadium AS S3 ON(S2.id +1 = S3.id AND S2.people >=100 AND S3.people >=100)
) AS A
JOIN stadium AS S ON(A.id1 = S.id OR A.id2=S.id OR A.id3=S.id)
```

#### MySQL解题02  :

对每一行A，如果A的前两行的客流量都>=100，或者A的前一行或后一行的客流量都>=100，或者 A的后两行的客流量都>=100 。那么，行A就是结果中的一条。

A的前两行的客流量都>=100，逻辑如下：

```
2=(
	SELECT COUNT(*)
	FROM stadium AS S
	WHERE S.people >= 100 AND (S.id = S1.id-1 OR S.id = S1.id-2)
)
```

A的前一行或后一行的客流量都>=100，逻辑如下：

```
2=(
	SELECT COUNT(*)
	FROM stadium AS S
	WHERE S.people >= 100 AND (S.id = S1.id-1 OR S.id = S1.id+1)
)
```

A的后两行的客流量都>=100，逻辑如下：

```
2=(
	SELECT COUNT(*)
	FROM stadium AS S
	WHERE S.people >= 100 AND (S.id = S1.id+1 OR S.id = S1.id+2)
)
```

最终,

```mysql
SELECT *
FROM stadium AS S1
WHERE S1.people >= 100 AND 
(
	2=(
		SELECT COUNT(*)
		FROM stadium AS S
		WHERE S.people >= 100 AND (S.id = S1.id-1 OR S.id = S1.id-2)
	) OR 
	2=(
		SELECT COUNT(*)
		FROM stadium AS S
		WHERE S.people >= 100 AND (S.id = S1.id-1 OR S.id = S1.id+1)
	) OR 
	2=(
		SELECT COUNT(*)
		FROM stadium AS S
		WHERE S.people >= 100 AND (S.id = S1.id+1 OR S.id = S1.id+2)
	)
)
```





