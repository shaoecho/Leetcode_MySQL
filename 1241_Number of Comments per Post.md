####  每个帖子的评论数

SQL框架

```mysql
Create table If Not Exists Submissions (sub_id int, parent_id int)
Truncate table Submissions
insert into Submissions (sub_id, parent_id) values ('1', 'None')
insert into Submissions (sub_id, parent_id) values ('2', 'None')
insert into Submissions (sub_id, parent_id) values ('1', 'None')
insert into Submissions (sub_id, parent_id) values ('12', 'None')
insert into Submissions (sub_id, parent_id) values ('3', '1')
insert into Submissions (sub_id, parent_id) values ('5', '2')
insert into Submissions (sub_id, parent_id) values ('3', '1')
insert into Submissions (sub_id, parent_id) values ('4', '1')
insert into Submissions (sub_id, parent_id) values ('9', '1')
insert into Submissions (sub_id, parent_id) values ('10', '2')
insert into Submissions (sub_id, parent_id) values ('6', '7')
```

表 Submissions 结构如下：

| 列名      | 类型 |
| --------- | ---- |
| sub_id    | int  |
| parent_id | int  |

上表没有主键, 所以可能会出现重复的行。每行可以是一个帖子或对该帖子的评论。
如果是帖子的话，parent_id 就是 null。对于评论来说，parent_id 就是表中对应帖子的 sub_id。

编写 SQL 语句以查找每个帖子的评论数。

结果表应包含帖子的 post_id 和对应的评论数 number_of_comments 并且按 post_id 升序排列。

Submissions 可能包含重复的评论。您应该计算每个帖子的唯一评论数。

Submissions 可能包含重复的帖子。您应该将它们视为一个帖子。

查询结果格式如下例所示：

Submissions table:

| sub_id | parent_id |
| ------ | --------- |
| 1      | Null      |
| 2      | Null      |
| 1      | Null      |
| 12     | Null      |
| 3      | 1         |
| 5      | 2         |
| 3      | 1         |
| 4      | 1         |
| 9      | 1         |
| 10     | 2         |
| 6      | 7         |

结果表：

| post_id | number_of_comments |
| ------- | ------------------ |
| 1       | 3                  |
| 2       | 2                  |
| 12      | 0                  |

表中 ID 为 1 的帖子有 ID 为 3、4 和 9 的三个评论。表中 ID 为 3 的评论重复出现了，所以我们只对它进行了一次计数。
表中 ID 为 2 的帖子有 ID 为 5 和 10 的两个评论。
ID 为 12 的帖子在表中没有评论。
表中 ID 为 6 的评论是对 ID 为 7 的已删除帖子的评论，因此我们将其忽略。



#### MySQL解题  :

1). 先查出贴子的`post_id`并去重

```mysql
SELECT DISTINCT sub_id AS post_id FROM Submissions WHERE parent_id IS NULL
```

查询结果:

| post_id |
| ------- |
| 1       |
| 2       |
| 12      |

2). 根据帖子的`post_id`找出该帖子下的所有评论

```mysql
SELECT post_id,S2.sub_id 
FROM
	( SELECT DISTINCT sub_id AS post_id FROM Submissions WHERE parent_id IS NULL ) S1
	LEFT JOIN Submissions S2 ON S1.post_id = S2.parent_id 
```

查询结果:

| post_id | sub_id |
| ------- | ------ |
| 1       | 3      |
| 2       | 5      |
| 1       | 3      |
| 1       | 4      |
| 1       | 9      |
| 2       | 10     |
| 12      | null   |

3). 先查出贴子的`post_id`并去重

因为默认排序已经满足条件,此处无需再用order by

```mysql
SELECT
	post_id,
	COUNT( DISTINCT S2.sub_id ) AS number_of_comments 
FROM
	( SELECT DISTINCT sub_id AS post_id FROM Submissions WHERE parent_id IS NULL ) S1
	LEFT JOIN Submissions S2 ON S1.post_id = S2.parent_id 
GROUP BY S1.post_id
```

查询结果:

| post_id | number_of_comments |
| ------- | ------------------ |
| 1       | 3                  |
| 2       | 2                  |
| 12      | 0                  |





