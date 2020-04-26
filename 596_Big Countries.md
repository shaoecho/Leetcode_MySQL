#### 大的国家  

SQL框架

```mysql
Create table If Not Exists courses (student varchar(255), class varchar(255))
Truncate table courses
insert into courses (student, class) values ('A', 'Math')
insert into courses (student, class) values ('B', 'English')
insert into courses (student, class) values ('C', 'Math')
insert into courses (student, class) values ('D', 'Biology')
insert into courses (student, class) values ('E', 'Math')
insert into courses (student, class) values ('F', 'Computer')
insert into courses (student, class) values ('G', 'Math')
insert into courses (student, class) values ('H', 'Math')
insert into courses (student, class) values ('I', 'Math')
```

有一个`courses` 表 ，有: **student (学生)** 和 **class (课程)**。

请列出所有超过或等于5名学生的课。

例如,表:

| student | class    |
| ------- | -------- |
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |

应该输出:

| class |
| ----- |
| Math  |

**Note:**
学生在每个课中不应被重复计算。

#### MySQL解题01  :

```mysql
SELECT
    class
FROM
    (SELECT
        class, COUNT(DISTINCT student) AS num
    FROM
        courses
    GROUP BY class) AS temp_table
WHERE
    num >= 5
```

#### 知识点 :

思路是先统计每门课程的学生数量，再从中选择超过 5 名学生的课程。

注：`COUNT(student)` 不能直接在 `WHERE` 子句中使用，这里将其重命名为 `num`。

生成了一个临时表 temp_table

| class    | COUNT(student) |
| -------- | -------------- |
| Biology  | 1              |
| Computer | 1              |
| English  | 1              |
| Math     | 6              |



#### MySQL解题02  :

```mysql
SELECT
    class
FROM
    courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5
```

#### 知识点 :

- 执行顺序 where>group by>having>order by
- where 分组前，将不符合where条件的行去掉, 后面不接聚合函数
- group by 分组
- having 分组之后过滤数据条件中经常包含聚组函数
- 在 `GROUP BY` 子句后使用 [`HAVING`](https://dev.mysql.com/doc/refman/5.7/en/group-by-handling.html) 条件是实现子查询的一种更加简单直接的方法。

