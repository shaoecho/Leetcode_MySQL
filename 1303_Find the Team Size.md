####  1303. 求团队人数 

SQL框架

```mysql
Create table If Not Exists Employee (employee_id int, team_id int)
Truncate table Employee
insert into Employee (employee_id, team_id) values ('1', '8')
insert into Employee (employee_id, team_id) values ('2', '8')
insert into Employee (employee_id, team_id) values ('3', '8')
insert into Employee (employee_id, team_id) values ('4', '7')
insert into Employee (employee_id, team_id) values ('5', '9')
insert into Employee (employee_id, team_id) values ('6', '9')
```

员工表：Employee

| Column Name | Type |
| ----------- | ---- |
| employee_id | int  |
| team_id     | int  |

employee_id 字段是这张表的主键，表中的每一行都包含每个员工的 ID 和他们所属的团队。
编写一个 SQL 查询，以求得每个员工所在团队的总人数。

查询结果中的顺序无特定要求。

查询结果格式示例如下：

Employee Table:

| employee_id | team_id |
| ----------- | ------- |
| 1           | 8       |
| 2           | 8       |
| 3           | 8       |
| 4           | 7       |
| 5           | 9       |
| 6           | 9       |

Result table:

| employee_id | team_size |
| ----------- | --------- |
| 1           | 3         |
| 2           | 3         |
| 3           | 3         |
| 4           | 1         |
| 5           | 2         |
| 6           | 2         |

D 为 1、2、3 的员工是 team_id 为 8 的团队的成员，
ID 为 4 的员工是 team_id 为 7 的团队的成员，
ID 为 5、6 的员工是 team_id 为 9 的团队的成员。



#### MySQL解题01  :  建立符合要求的临时表

先求team size 建立 team_id + team_siez的临时表 再与原表用team_id链接 .

```mysql
select employee_id, team_size
from employee e,
(select team_id, count(*) as team_size
from employee
group by team_id) t
where e.team_id = t.team_id
```

#### MySQL解题02  : 左连接_多对多+自连接

```mysql
select e1.employee_id, count(*) as team_size
from employee e1 left join employee e2
on e1.team_id = e2.team_id
group by e1.employee_id;
```

1. 思路:

要求"每个员工所在团队的总人数", 说明最后是按照employee_id进行分组, 即要求在每个employee_id分组后,能通过聚合函数统计出对应团队的总人数, 就想到了用on e1.team_id = e2.team_id进行自连接, 这样在每个分组内, 都会把team_id相同的数据连接起来.



2.  这是左连接中多对多的情况:  同使还是自连接, 左右表都是employee.

employee e1 left join employee e2 on e1.team_id = e2.team_id的运行逻辑是:

1)    从e1中拿出第1行数据(1,8), 再遍历e2,找出满足e1.team_id = e2.team_id的数据, 找到了3条(1,8),(2,8)(3,8).

2)   从e1中拿出第2行数据(2,8), 再遍历e2,找出满足e1.team_id = e2.team_id的数据, 找到了3条(1,8),(2,8)(3,8).

3)   从e1中拿出第3行数据(3,8), 再遍历e2,找出满足e1.team_id = e2.team_id的数据, 找到了3条(1,8),(2,8)(3,8).

4)   从e1中拿出第4行数据(4,7), 再遍历e2,找出满足e1.team_id = e2.team_id的数据, 找到了1条(4,7).

5)   从e1中拿出第5行数据(5,9), 再遍历e2,找出满足e1.team_id = e2.team_id的数据, 找到了2条(5,9),(6,9).

6)   从e1中拿出第6行数据(6,9), 再遍历e2,找出满足e1.team_id = e2.team_id的数据, 找到了2条(5,9),(6,9).

| e1.employee_id | e1.team_id | e2.employee_id | e2.team_id |
| -------------- | ---------- | -------------- | ---------- |
| 1              | 8          | 1              | 8          |
| 1              | 8          | 2              | 8          |
| 1              | 8          | 3              | 8          |
| 2              | 8          | 1              | 8          |
| 2              | 8          | 2              | 8          |
| 2              | 8          | 3              | 8          |
| 3              | 8          | 1              | 8          |
| 3              | 8          | 2              | 8          |
| 3              | 8          | 3              | 8          |
| 4              | 7          | 4              | 7          |
| 5              | 9          | 5              | 9          |
| 5              | 9          | 6              | 9          |
| 6              | 9          | 5              | 9          |
| 6              | 9          | 6              | 9          |



#### MySQL解题03  :  分组+组内子查询

```mysql
select 
e1.employee_id,
(select count(*) from Employee e2 where e2.team_id=e1.team_id) as team_size #看不懂
from Employee e1
group by e1.employee_id
```

 要求在每个employee_id分组后,能通过聚合函数统计出对应团队的总人数, 即要把team_id相同的数据连接起来.

运行逻辑是:

1) 先分组,每个组是同一个employee_id.

2) 在每个分组内, 用了子查询,查询e2中和此分组同一个team_id的数据.











