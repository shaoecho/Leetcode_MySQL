#### 项目员工 III

SQL框架

```mysql
Create table If Not Exists Project (project_id int, employee_id int)
Create table If Not Exists Employee (employee_id int, name varchar(10), experience_years int)
Truncate table Project
insert into Project (project_id, employee_id) values ('1', '1')
insert into Project (project_id, employee_id) values ('1', '2')
insert into Project (project_id, employee_id) values ('1', '3')
insert into Project (project_id, employee_id) values ('2', '1')
insert into Project (project_id, employee_id) values ('2', '4')
Truncate table Employee
insert into Employee (employee_id, name, experience_years) values ('1', 'Khaled', '3')
insert into Employee (employee_id, name, experience_years) values ('2', 'Ali', '2')
insert into Employee (employee_id, name, experience_years) values ('3', 'John', '1')
insert into Employee (employee_id, name, experience_years) values ('4', 'Doe', '2')
```

项目表 `Project`： 

| Column Name | Type |
| ----------- | ---- |
| project_id  | int  |
| employee_id | int  |

主键为 (project_id, employee_id)。
employee_id 是员工表 Employee 表的外键。

员工表 `Employee`：

| Column Name      | Type    |
| ---------------- | ------- |
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |

主键是 employee_id。

写 一个 SQL 查询语句，报告在每一个项目中经验最丰富的雇员是谁。如果出现经验年数相同的 情况，请报告所有具有最大经验年数的员工。

查询结果的格式如下：

Project 表：

| project_id | employee_id |
| ---------- | ----------- |
| 1          | 1           |
| 1          | 2           |
| 1          | 3           |
| 2          | 1           |
| 2          | 4           |

Employee 表：

| employee_id | name   | experience_years |
| ----------- | ------ | ---------------- |
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |

Result 表：

| project_id | employee_id |
| ---------- | ----------- |
| 1          | 1           |
| 1          | 3           |
| 2          | 1           |

employee_id 为 1 和 3 的员工在 project_id 为 1 的项目中拥有最丰富的经验。

在 project_id 为 2 的项目中，employee_id 为 1 的员工拥有最丰富的经验。

#### MySQL解题01 :  窗口函数

```mysql
/* Write your T-SQL query statement below */
select project_id,employee_id 
from (
	select 
    	p.project_id,
    	e.employee_id,
    	e.experience_years,
    	RANK()over(partition by p.project_id order by e.experience_years desc)as ranking 
	from 
    	project p left join Employee  e 
    	on p.employee_id =e.employee_id 
	)t  
where ranking<=1

```

#### MySQL解题02 : select * from ... where....

题目问的是每一个项目中经验最丰富的雇员是谁（经验最丰富=工龄最长）

我们先筛选出每个项目最长工龄
两个表进行通过相同的employee_id进行inner join，筛选出每组的最大experience_years，输出项目和experience_years

```mysql
select project_id, max(experience_years) ey
from Project p inner join Employee e 
on p.employee_id=e.employee_id
group by project_id
```

利用子查询提取每个项目的经验最丰富的员工

用到结构 `select * from ... where (project_id,experience_years) in ...`

```mysql
select project_id,e.employee_id 
from Project p inner join Employee e 
on p.employee_id = e.employee_id
where 
	(project_id,experience_years) 
	in
	(select project_id, max(experience_years) as ey 
     from Project p inner join Employee e
     on p.employee_id=e.employee_id
     group by project_id
    )
```



