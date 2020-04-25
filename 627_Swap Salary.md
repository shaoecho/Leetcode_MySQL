####交换工资

 SQL框架

```mysql
create table if not exists salary(id int, name varchar(100), sex char(1), salary int)
Truncate table salary
insert into salary (id, name, sex, salary) values ('1', 'A', 'm', '2500')
insert into salary (id, name, sex, salary) values ('2', 'B', 'f', '1500')
insert into salary (id, name, sex, salary) values ('3', 'C', 'm', '5500')
insert into salary (id, name, sex, salary) values ('4', 'D', 'f', '500')
```

给定一个 salary 表，如下所示，有 m = 男性 和 f = 女性 的值。交换所有的 f 和 m 值（例如，将所有 f 值更改为 m，反之亦然）。要求只使用一个更新（Update）语句，并且没有中间的临时表。

注意，您必只能写一个 Update 语句，请不要编写任何 Select 语句。

例如：

| id   | name | sex  | salary |
| ---- | ---- | ---- | ------ |
| 1    | A    | m    | 2500   |
| 2    | B    | f    | 1500   |
| 3    | C    | m    | 5500   |
| 4    | D    | f    | 500    |
运行你所编写的更新语句之后，将会得到以下表:

| id   | name | sex  | salary |
| ---- | ---- | ---- | ------ |
| 1    | A    | f    | 2500   |
| 2    | B    | m    | 1500   |
| 3    | C    | f    | 5500   |
| 4    | D    | m    | 500    |



#### MySQL解题方法01  :

```mysql
UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;
```

#### 知识点 :

要想动态地将值设置成列，我们可以在使用 [`CASE...WHEN...`](https://dev.mysql.com/doc/refman/5.7/en/case.html) 流程控制语句的同时使用 [`UPDATE`](https://dev.mysql.com/doc/refman/5.7/en/update.html) 语句。

#### MySQL解题方法02  :update salary set sex=IF(sex='f','m','f')

```mysql
update salary 
set sex=IF(sex='f','m','f')
```

