### 177.  第N高的薪水

编写一个 SQL 查询，获取 `Employee` 表中第 *n* 高的薪水（Salary）。

| Id   | Salary |
| ---- | ------ |
| 1    | 100    |
| 2    | 200    |
| 3    | 300    |

例如上述 `Employee` 表，*n = 2* 时，应返回第二高的薪水 `200`。

如果不存在第 *n* 高的薪水，那么查询应返回 `null`。

| getNthHighestSalary(2) |
| ---------------------- |
| 200                    |

#### MySQL解题  :

```mysql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE c INT default if(N>0,N-1,1);   # 声明变量c为整数,若N>0, c=N-1, 否则 c=1.
    RETURN (
        select 
            IFNULL(
            (select distinct Salary  from Employee order by Salary Desc limit c,1)
            ,null) 
    );
END

```

#### 知识点 :

1) MYSQL中申明变量的方法是 DECLARE 变量名 变量数据类型

2) default设置默认值, 结合if使用效果翻倍.

3) 当第n高的薪水重复时,则不存在第n高的薪水, 题目要求此时返回null值.

方法01: 用IFNULL(表达式null),则表达式不成立, 返回null, 表达式成立,返回表达式值.

方法02: 用groupby进行分组,分组的时候,group by Salary表示根据薪水分组,然后再找第n高的薪水,此时不会重复.

 select Salary from Employee group by Salary order by Salary desc limit c,1)

4) limit c,1 表示跳过c个数,取1个数据,即表示查找第c+1个数, =limit 1 offset c.