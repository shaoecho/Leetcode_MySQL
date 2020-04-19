### 上升的温度

SQL框架

```mysql
Create table If Not Exists Weather (Id int, RecordDate date, Temperature int)
Truncate table Weather
insert into Weather (Id, RecordDate, Temperature) values ('1', '2015-01-01', '10')
insert into Weather (Id, RecordDate, Temperature) values ('2', '2015-01-02', '25')
insert into Weather (Id, RecordDate, Temperature) values ('3', '2015-01-03', '20')
insert into Weather (Id, RecordDate, Temperature) values ('4', '2015-01-04', '30')
```

给定一个 `Weather` 表，编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 Id。

| Id(INT) | RecordDate(DATE) | Temperature(INT) |
| ------- | ---------------- | ---------------- |
| 1       | 2015-01-01       | 10               |
| 2       | 2015-01-02       | 25               |
| 3       | 2015-01-03       | 20               |
| 4       | 2015-01-04       | 30               |

例如，根据上述给定的 `Weather` 表格，返回如下 Id:

| Id   |
| ---- |
| 2    |
| 4    |



#### MySQL解题方法01  :

```mysql
select w1.Id as  Id 
from
	Weather w1 join Weather w2 
	on datediff(w1.RecordDate,w2.RecordDate)=1 #表示相隔1天
	and w1.Temperature > w2.Temperature
```

#### 知识点 :

将join..on..根据on后面的条件连接两表,此处连接后,一行上前一半是今天的数据,后一半是昨天的数据.
datediff()函数表示两日期的差值

