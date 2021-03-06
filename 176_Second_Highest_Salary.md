### 176.  第二高的薪水

#### SQL框架

```mysql
Create table If Not Exists Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (Id, Salary) values ('1', '100')
insert into Employee (Id, Salary) values ('2', '200')
insert into Employee (Id, Salary) values ('3', '300')
```

编写一个 SQL 查询，获取 `Employee` 表中第二高的薪水（Salary） 。

| Id   | Salary |
| ---- | ------ |
| 1    | 100    |
| 2    | 200    |
| 3    | 300    |

例如上述 `Employee` 表，SQL查询应该返回 `200` 作为第二高的薪水。

如果不存在第二高的薪水，那么查询应返回 `null`。

| SecondHighestSalary |
| ------------------- |
| 200                 |

#### MySQL解题  :

```mysql
SELECT
    IFNULL(
      (SELECT DISTINCT    # DISTINCT是去重,用于返回唯一不同的值。
            Salary        # SELECT  列名称 FROM 表名称 
       FROM Employee
       ORDER BY Salary DESC       #DESC表降序 
       LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary

```

#### 知识点 :

\# SELECT DISTINCT Salary FROM Employee 表示从Employee中抽出Salary这一列,并去重,生成新的一列.

\# ORDER BY Salary EDSC 表示将新生成的一列降序排列.

\# LIMIT 1 OFFSET 1 其中LIMIT 1表示只读1个数据, OFFSET 1 表示第1条不读, 从第2条开始读. 即读取排名第2的数据.

\# SELECT...as...其中as有重命名的意思,本题表示把()内得到的列重新命名为SecondHighestSalary.

\#IFNULL(表达式, 参数2)如果参数1的表达式的值为 NULL，返回参数2. 如果不为 NULL 则返回表达式的值。

\#此处IFNULL(括号内的内容, NULL) 如果括号内的内容值为null, 则返回null.

