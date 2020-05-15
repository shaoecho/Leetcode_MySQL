####  577.  员工奖金

SQL框架

```mysql
Create table If Not Exists Employee (EmpId int, Name varchar(255), Supervisor int, Salary int)
Create table If Not Exists Bonus (EmpId int, Bonus int)
Truncate table Employee
insert into Employee (EmpId, Name, Supervisor, Salary) values ('3', 'Brad', 'None', '4000')
insert into Employee (EmpId, Name, Supervisor, Salary) values ('1', 'John', '3', '1000')
insert into Employee (EmpId, Name, Supervisor, Salary) values ('2', 'Dan', '3', '2000')
insert into Employee (EmpId, Name, Supervisor, Salary) values ('4', 'Thomas', '3', '4000')
Truncate table Bonus
insert into Bonus (EmpId, Bonus) values ('2', '500')
insert into Bonus (EmpId, Bonus) values ('4', '2000')
```

选出所有 bonus < 1000 的员工的 name 及其 bonus。

`Employee` 表单

| empId | name   | supervisor | salary |
| ----- | ------ | ---------- | ------ |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 3     | Brad   | null       | 4000   |
| 4     | Thomas | 3          | 4000   |

empId 是这张表单的主关键字

`Bonus` 表单

| empId | bonus |
| :---- | ----- |
| 2     | 500   |
| 4     | 2000  |

empId 是这张表单的主关键字

输出示例：

| name | bonus |
| ---- | ----- |
| John | null  |
| Dan  | 500   |
| Brad | null  |

#### MySQL解题  :

使用左外连接（`left join` 或 `left outer join`）

```mysql
select name, bonus
from Employee left join Bonus
on Employee.EmpId = Bonus.EmpId
```

对于题目中的样例，上面的代码运行可以得到如下输出：

| name   | bonus |
| ------ | ----- |
| Dan    | 500   |
| Thomas | 2000  |
| Brad   |       |
| John   |       |

其中 Brad 和 John 的 bonus 值为空，空值在数据库中的表示为 null。我们使用 bonus is null（而不是 bonus = null）判断奖金是否为 null。随后即可用 where 子句筛选奖金小于 1000 或者为空的员工。

```mysql
select name, bonus
from Employee left join Bonus
on Employee.EmpId = Bonus.EmpId
where bonus is null or bonus < 1000
```

