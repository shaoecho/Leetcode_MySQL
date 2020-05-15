####  学生们参加各科测试的次数

SQL框架

```mysql
Create table If Not Exists Subjects (subject_name varchar(20))
Create table If Not Exists Examinations (student_id int, subject_name varchar(20))
Truncate table Students
insert into Students (student_id, student_name) values ('1', 'Alice')
insert into Students (student_id, student_name) values ('2', 'Bob')
insert into Students (student_id, student_name) values ('13', 'John')
insert into Students (student_id, student_name) values ('6', 'Alex')
Truncate table Subjects
insert into Subjects (subject_name) values ('Math')
insert into Subjects (subject_name) values ('Physics')
insert into Subjects (subject_name) values ('Programming')
Truncate table Examinations
insert into Examinations (student_id, subject_name) values ('1', 'Math')
insert into Examinations (student_id, subject_name) values ('1', 'Physics')
insert into Examinations (student_id, subject_name) values ('1', 'Programming')
insert into Examinations (student_id, subject_name) values ('2', 'Programming')
insert into Examinations (student_id, subject_name) values ('1', 'Physics')
insert into Examinations (student_id, subject_name) values ('1', 'Math')
insert into Examinations (student_id, subject_name) values ('13', 'Math')
insert into Examinations (student_id, subject_name) values ('13', 'Programming')
insert into Examinations (student_id, subject_name) values ('13', 'Physics')
insert into Examinations (student_id, subject_name) values ('2', 'Math')
insert into Examinations (student_id, subject_name) values ('1', 'Math')
```

学生表: `Students`

| Column Name  | Type    |
| ------------ | ------- |
| student_id   | int     |
| student_name | varchar |

主键为 student_id（学生ID），该表内的每一行都记录有学校一名学生的信息。

科目表: Subjects

| Column Name  | Type    |
| ------------ | ------- |
| subject_name | varchar |

主键为 subject_name（科目名称），每一行记录学校的一门科目名称。

考试表: Examinations

| Column Name  | Type    |
| ------------ | ------- |
| student_id   | int     |
| subject_name | varchar |

这张表压根没有主键，可能会有重复行。
学生表里的一个学生修读科目表里的每一门科目，而这张考试表的每一行记录就表示学生表里的某个学生参加了一次科目表里某门科目的测试。

要求写一段 SQL 语句，查询出每个学生参加每一门科目测试的次数，结果按 student_id 和 subject_name 排序。

查询结构格式如下所示：

Students table:

| student_id | student_name |
| ---------- | ------------ |
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |

Subjects table:  

| subject_name |
| ------------ |
| Math         |
| Physics      |
| Programming  |

Examinations  table:

| student_id | subject_name |
| ---------- | ------------ |
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
| 13         | Math         |
| 13         | Programming  |
| 13         | Physics      |
| 2          | Math         |
| 1          | Math         |

Result table:

| student_id | student_name | subject_name | attended_exams |
| ---------- | ------------ | ------------ | -------------- |
| 1          | Alice        | Math         | 3              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 1              |
| 2          | Bob          | Physics      | 0              |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | 0              |
| 6          | Alex         | Physics      | 0              |
| 6          | Alex         | Programming  | 0              |
| 13         | John         | Math         | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Programming  | 1              |

结果表需包含所有学生和所有科目（即便测试次数为0）：
Alice 参加了 3 次数学测试, 2 次物理测试，以及 1 次编程测试；
Bob 参加了 1 次数学测试, 1 次编程测试，没有参加物理测试；
Alex 啥测试都没参加；
John  参加了数学、物理、编程测试各 1 次。



#### MySQL解题  :

```mysql
select 
e.student_id as student_id,
st.student_name as student_name,
e.subject_name as subject_name,
count(e.subject_name) as attended_exams
from 
	Students st 
	cross join Subjects su 
	left join Examinations e on st.student_id = e.student_id
group by st.student_id ,e.subject_name
order by st.student_id,su.subject_name 

```

题目要求结果表需包含所有学生以及,所有科目表,  所以不能简单的使用Examinations表左连接Students表.

1) 为了找出学生和课表的所有组合, 即所有学生参加了所有考试的情况.

用Students表 交叉连接subjects表.

```mysql
select *
from Students  cross join Subjects 
```

得到一个行数为 4 * 3行的表.

2) 再左连接第3个表, 因为Students表 交叉连接subjects表已经满足题目的要求(结果表需包含所有学生以及,所有科目表)了, 所以提出用左连接. 

```mysql
select *
from
	Students st cross join Subjects su
	left join Examinations e
	on st.student_id = e.student_id and su.subject_name = e.subject_name
	-- 注意: 此处on后面有两个条件! 仅仅用on st.student_id = e.student_id是不够的.
```

3) 分组排序后, 从中间表t2上选择要的数据.

```mysql
select 
	st.student_id,
	st.student_name,
	su.subject_name,
	count(e.subject_name) as attended_exams
from 
	Students st cross join Subjects su
	left join Examinations e
	on st.student_id = e.student_id and su.subject_name = e.subject_name
group by st.student_id ,su.subject_name
order by st.student_id ,su.subject_name
```







