### 部门工资最高的员工 

SQL框架

```mysql
Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, DepartmentId int)
Create table If Not Exists Department (Id int, Name varchar(255))
Truncate table Employee
insert into Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '70000', '1')
insert into Employee (Id, Name, Salary, DepartmentId) values ('2', 'Jim', '90000', '1')
insert into Employee (Id, Name, Salary, DepartmentId) values ('3', 'Henry', '80000', '2')
insert into Employee (Id, Name, Salary, DepartmentId) values ('4', 'Sam', '60000', '2')
insert into Employee (Id, Name, Salary, DepartmentId) values ('5', 'Max', '90000', '1')
Truncate table Department
insert into Department (Id, Name) values ('1', 'IT')
insert into Department (Id, Name) values ('2', 'Sales')
```

`Employee` 表包含所有员工信息，每个员工有其对应的 Id, salary 和 department Id。

| Id   | Name  | Salary | DepartmentId |
| ---- | ----- | ------ | ------------ |
| 1    | Joe   | 70000  | 1            |
| 2    | Henry | 80000  | 2            |
| 3    | Sam   | 60000  | 2            |
| 4    | Max   | 90000  | 1            |

`Department` 表包含公司所有部门的信息。

| Id   | Name  |
| ---- | ----- |
| 1    | IT    |
| 2    | Sales |

编写一个 SQL 查询，找出每个部门工资最高的员工。

例如，根据上述给定的表格，Max 在 IT 部门有最高工资，Henry 在 Sales 部门有最高工资。

| Department | Employee | Salary |
| ---------- | -------- | ------ |
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |

#### MySQL解题  :

```mysql
# Write your MySQL query statement below

select 
    D.Name as Department ,
    E.Name as Employee,
    E.Salary 
from 
    Employee E  join Department D
    on E.DepartmentId = D.Id
where
    (E.DepartmentId, E.Salary) in
    (   select
            DepartmentID,max(Salary)
        from 
            Employee                 #此处不能用代称E, 会报错
        group by DepartmentId
    )

```

#### 知识点 :

先用where 表示先筛选出Employee表中包含每个部门最高薪水的行

​	select DepartmentID,max(Salary) from E group by DepartmentId

再用 join 将Department 和上一步筛选出的行组成临时表

最后,从临时表中选取题目要求显示的内容

如果使用left join, 要注意,部门名字不能是null???不太懂

