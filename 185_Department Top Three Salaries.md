#### 185.  部门工资前三高的所有员工

 SQL框架

```mysql
Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, DepartmentId int)
Create table If Not Exists Department (Id int, Name varchar(255))
Truncate table Employee
insert into Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '85000', '1')
insert into Employee (Id, Name, Salary, DepartmentId) values ('2', 'Henry', '80000', '2')
insert into Employee (Id, Name, Salary, DepartmentId) values ('3', 'Sam', '60000', '2')
insert into Employee (Id, Name, Salary, DepartmentId) values ('4', 'Max', '90000', '1')
insert into Employee (Id, Name, Salary, DepartmentId) values ('5', 'Janet', '69000', '1')
insert into Employee (Id, Name, Salary, DepartmentId) values ('6', 'Randy', '85000', '1')
insert into Employee (Id, Name, Salary, DepartmentId) values ('7', 'Will', '70000', '1')
Truncate table Department
insert into Department (Id, Name) values ('1', 'IT')
insert into Department (Id, Name) values ('2', 'Sales')
```

 `Employee` 表包含所有员工信息，每个员工有其对应的工号 `Id`，姓名 `Name`，工资 `Salary` 和部门编号 `DepartmentId` 。

| Id   | Name  | Salary | DepartmentId |
| ---- | ----- | ------ | ------------ |
| 1    | Joe   | 85000  | 1            |
| 2    | Henry | 80000  | 2            |
| 3    | Sam   | 60000  | 2            |
| 4    | Max   | 90000  | 1            |
| 5    | Janet | 69000  | 1            |
| 6    | Randy | 85000  | 1            |
| 7    | Will  | 70000  | 1            |

`Department` 表包含公司所有部门的信息。

| Id   | Name  |
| ---- | ----- |
| 1    | IT    |
| 2    | Sales |

编写一个 SQL 查询，找出每个部门获得前三高工资的所有员工。例如，根据上述给定的表，查询结果应返回：

| Department | Employee | Salary |
| ---------- | -------- | ------ |
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
| IT         | Joe      | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |

解释：

IT 部门中，Max 获得了最高的工资，Randy 和 Joe 都拿到了第二高的工资，Will 的工资排第三。销售部门（Sales）只有两名员工，Henry 的工资最高，Sam 的工资排第二。

补充一个提交注意点，部门薪水前三高包含了相同薪水下排名相同的意思



#### MySQL解题01  :

```mysql
SELECT
	d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
 	Employee e1 
	JOIN Department d 
	ON e1.DepartmentId = d.Id
WHERE
#工资级别数量小于等于3，即最多只有3个工资级别，也就是前三高
 	3 >= (
     	SELECT COUNT(DISTINCT e2.Salary)
 		FROM Employee e2
  		WHERE e2.Salary >= e1.Salary  AND e1.DepartmentId = e2.DepartmentId
    	)
ORDER BY e1.DepartmentId,e1.Salary DESC;
#e2的工资级别大于等于e1的工资级别
```

#### 知识点 :



#### MySQL解题02 :    用窗口函数DENSE_RANK() OVER ()

```mysql
SELECT 
    B.Name AS Department,
    A.Name AS Employee,
    A.Salary
FROM 
	(SELECT 
		DENSE_RANK() OVER (partition by DepartmentId order by Salary desc) AS ranking,
	 	DepartmentId,Name,Salary
     FROM Employee
      ) AS A
JOIN Department AS B ON A.DepartmentId=B.id
WHERE A.ranking<=3
```

 解题思路:

先对Employee表进行部门分组工资排名，再关联Department表查询部门名称，再使用WHERE筛选出排名小于等于3的数据（也就是每个部门排名前3的工资）。

1. MySQL 8+开始可以使用窗口函数. 

2. 窗口函数dense_rank() over (partition by DepartmentId order by Salary desc)   表示按照DepartmentId 分组, 并在每个组里按照薪水的降序排列, 并给与无间隔排序.

3. 下列代码

   ```MYSQL
   SELECT 
   	DENSE_RANK() OVER (partition by DepartmentId order by Salary desc) AS ranking,
   	DepartmentId,Name,Salary
   FROM Employee
   ```

   会生成临时表A

   注: 看下表有两个85000, ranking 都是2, 然后后面的7000, ranking 都是3, 这就是dense_rank()的无间隔排序.

   | Id   | Name  | Salary | DepartmentId | ranking |
   | ---- | ----- | ------ | ------------ | ------- |
   | 4    | Max   | 90000  | 1            | 1       |
   | 1    | Joe   | 85000  | 1            | 2       |
   | 6    | Randy | 85000  | 1            | 2       |
   | 7    | Will  | 70000  | 1            | 3       |
   | 5    | Janet | 69000  | 1            | 4       |
   | 2    | Henry | 80000  | 2            | 1       |
   | 3    | Sam   | 60000  | 2            | 2       |

   采用JOIN Department AS B ON A.DepartmentId=B.id语句 将上表和Department表结合. 得到下表:

   | A.Id | A.Name | A.Salary | A.DepartmentId | A.ranking | B.id | B.Name |
   | ---- | ------ | -------- | -------------- | --------- | ---- | ------ |
   | 4    | Max    | 90000    | 1              | 1         | 1    | IT     |
   | 1    | Joe    | 85000    | 1              | 2         | 1    | IT     |
   | 6    | Randy  | 85000    | 1              | 2         | 1    | IT     |
   | 7    | Will   | 70000    | 1              | 3         | 1    | IT     |
   | 5    | Janet  | 69000    | 1              | 4         | 1    | IT     |
   | 2    | Henry  | 80000    | 2              | 1         | 2    | Sales  |
   | 3    | Sam    | 60000    | 2              | 2         | 2    | Sales  |

   从上表中  SELECT  B.Name AS Department, A.Name AS Employee, A.Salary , 并且增加过滤条件A.ranking<=3 得到下表:

   | Department | Employee | Salary |
   | ---------- | -------- | ------ |
   | IT         | Max      | 90000  |
   | IT         | Joe      | 85000  |
   | IT         | Randy    | 85000  |
   | IT         | Will     | 70000  |
   | Sales      | Henry    | 80000  |
   | Sales      | Sam      | 60000  |

   

   #### MySQL解题03 :    用自定义变量

   分解步骤的思路,可以依据必要存在的步骤进行分解

   1.根据 **部门 (升)**，**薪水 (降)** 顺序查询出每个部门的员工 **(Department, Employee, Salary)**

   ```mysql
   SELECT dep.Name Department, emp.Name Employee, emp.Salary
   FROM Employee emp
   INNER JOIN Department dep ON emp.DepartmentId = dep.Id
   ORDER BY emp.DepartmentId, emp.Salary DESC
   ```

   2.每个部门的员工根据薪水排等级

   > 由于原本没有排序的字段,所以这里就需要自定义变量补充一个字段出来

   ```mysql
   ## 先(部门,薪水)去重,再 部门(升),薪水(降) 排序
   SELECT te.DepartmentId, te.Salary,
          CASE 
               WHEN @pre = DepartmentId THEN @rank:= @rank + 1
               WHEN @pre := DepartmentId THEN @rank:= 1
          END AS RANK
   FROM (SELECT @pre:=null, @rank:=0)tt,
        (## (部门,薪水)去重,根据 部门(升),薪水(降) 排序
            SELECT DepartmentId,Salary
            FROM Employee
            GROUP BY DepartmentId,Salary
            ORDER BY DepartmentId,Salary DESC
        )te
   ```

   3. 组合步骤

   组合步骤时,尽量将每个步骤变成一个 **结果集（不存在二次查询）**
   再将所有步骤的 **结果集进行关联**，从而提高性能.

   ```mysql
   SELECT dep.Name Department, emp.Name Employee, emp.Salary
   FROM (## 自定义变量RANK, 查找出 每个部门工资前三的排名
           SELECT te.DepartmentId, te.Salary,
                  CASE 
                       WHEN @pre = DepartmentId THEN @rank:= @rank + 1
                       WHEN @pre := DepartmentId THEN @rank:= 1
                  END AS RANK
           FROM (SELECT @pre:=null, @rank:=0)tt,
                (## (部门,薪水)去重,根据 部门(升),薪水(降) 排序
                    SELECT DepartmentId,Salary
                    FROM Employee
                    GROUP BY DepartmentId,Salary
                    ORDER BY DepartmentId,Salary DESC
                )te
          )t
   INNER JOIN Department dep ON t.DepartmentId = dep.Id
   INNER JOIN Employee emp ON t.DepartmentId = emp.DepartmentId and t.Salary = emp.Salary and t.RANK <= 3
   ORDER BY t.DepartmentId, t.Salary DESC ## t 结果集已有序,根据该集合排序
   ```

   