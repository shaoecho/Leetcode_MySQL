####  订单最多的客户

SQL框架

```mysql
Create table If Not Exists Views (article_id int, author_id int, viewer_id int, view_date date)
Truncate table Views
insert into Views (article_id, author_id, viewer_id, view_date) values ('1', '3', '5', '2019-08-01')
insert into Views (article_id, author_id, viewer_id, view_date) values ('1', '3', '6', '2019-08-02')
insert into Views (article_id, author_id, viewer_id, view_date) values ('2', '7', '7', '2019-08-01')
insert into Views (article_id, author_id, viewer_id, view_date) values ('2', '7', '6', '2019-08-02')
insert into Views (article_id, author_id, viewer_id, view_date) values ('4', '7', '1', '2019-07-22')
insert into Views (article_id, author_id, viewer_id, view_date) values ('3', '4', '4', '2019-07-21')
insert into Views (article_id, author_id, viewer_id, view_date) values ('3', '4', '4', '2019-07-21')
```

Views 表：

| Column Name | Type |
| ----------- | ---- |
| article_id  | int  |
| author_id   | int  |
| viewer_id   | int  |
| view_date   | date |

此表无主键，因此可能会存在重复行。
此表的每一行都表示某人在某天浏览了某位作者的某篇文章。
请注意，同一人的 author_id 和 viewer_id 是相同的。

编写一条 SQL 查询来找出在同一天阅读至少两篇文章的人，结果按照 id 升序排序。

查询结果的格式如下所示：

Views 表：

| article_id | author_id | viewer_id | view_date  |
| ---------- | --------- | --------- | ---------- |
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |

结果表：

| id   |
| ---- |
| 5    |
| 6    |

#### MySQL解题  :

```mysql
select distinct viewer_id as id
from Views
group by view_date,viewer_id
having count(distinct article_id) >= 2
order by viewer_id
```

根据题目一步一步的拆分成子任务：

1)  首先题目要求是同一天，所以需要根据时间聚合记录，使用 GROUP BY 聚合。

```mysql
GROUP BY view_date
```

2)  其次是至少阅读两篇文章的人。通过这句话我们可以知道还需要根据人来聚合，计算每个人阅读的文章数。在 GROUP BY 的基础上使用 HAVING 过滤条件。因为表中可能有重复的数据，所以还要对 article_id 做去重处理。

```mysql
GROUP BY viewer_id
HAVING COUNT(DISTINCT article_id) >= 2
```

3)  然后将结果按照 id 升序排序，这个只需要使用 ORDER BY 对结果进行排序。
4)  最后将上面三步联合起来就是我们需要的数据。但是结果依然有可能重复，所以需要再对结果去重。





