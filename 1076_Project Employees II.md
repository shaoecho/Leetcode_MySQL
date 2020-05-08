#### 项目员工 I

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

请写一个 SQL 语句，报告所有雇员最多的项目。

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

| project_id |
| ---------- |
| 1          |

第一个项目有3名员工，第二个项目有2名员工。

#### MySQL解题01  :

```mysql
select 
    project_id 
from 
    Project 
group by project_id 
having 
    count(*) = 
    (select count(*) as num
    from Project 
    group by project_id 
    order by count(*) desc 
    limit 1);
```

思路:

having后面的这个语句作用是确定所有项目组中, 雇员最多的项目组的雇员数. 

此时的limit 1的范围是所有项目组, 而不是分组后的项目组.

```mysql
select count(*) as num
from Project 
group by project_id      #先按照项目分组
order by count(*) desc   #计算每个项目组的雇员数并倒序排序
limit 1;                 #找到排第1位的
```

得到项目组1有3个雇员排第一位.

| num  |      |
| ---- | ---- |
| 3    |      |

代码简化为

```
select 
    project_id 
from 
    Project 
group by project_id 
having  count(*) = 3
```



