### 178.  分数排名

#### SQL框架

```mysql
Create table If Not Exists Scores (Id int, Score DECIMAL(3,2))
Truncate table Scores
insert into Scores (Id, Score) values ('1', '3.5')
insert into Scores (Id, Score) values ('2', '3.65')
insert into Scores (Id, Score) values ('3', '4.0')
insert into Scores (Id, Score) values ('4', '3.85')
insert into Scores (Id, Score) values ('5', '4.0')
insert into Scores (Id, Score) values ('6', '3.65')
```

编写一个 SQL 查询来实现分数排名。

如果两个分数相同，则两个分数排名（Rank）相同。

请注意，平分后的下一个名次应该是下一个连续的整数值。换句话说，名次之间不应该有“间隔”。

| Id   | Score |
| ---- | ----- |
| 1    | 3.50  |
| 2    | 3.65  |
| 3    | 4.00  |
| 4    | 3.85  |
| 5    | 4.00  |
| 6    | 3.65  |

例如，根据上述给定的 `Scores` 表，你的查询应该返回（按分数从高到低排列）：

| Score | Rank |
| ----- | ---- |
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |



#### MySQL解题  :

```mysql
SELECT a.Score, p.Rank
FROM Scores a    #Scores a 等于Scores as a表示将Scores表重命名为a??
    LEFT JOIN
        (
            SELECT s.Score AS Score, @num:=@num+1 AS Rank
            FROM (SELECT DISTINCT Score FROM Scores ORDER BY Score DESC) s, (SELECT @num:=0) r
        ) AS p
    ON a.Score = p.Score
ORDER BY a.Score DESC

```

#### 知识点 :

1)创建一张新表,显示去重后的 Score 和 Rank。

​	(SELECT DISTINCT Score FROM Scores ORDER BY Score DESC) s 表示对Scores表中Score列去重并降序排列,重新命名为s列.

​	(SELECT @num:=0) r 表示新定义变量num,初始值为0,重新命名为r列.

​	(SELECT s.Score AS Score, @num:=@num+1 AS Rank from...) as p 表示创建新表p, 包含两列Score列和Rank列.



2)将a表左连接p表,形成一张新的临时表.

​	a LEFT JOIN p



3) SELECT a.Score, p.Rank FROM 临时表 ORDER BY a.Score DESC 

​	从临时表中选出a.Score, p.Rank,并按照a.Score的降序排列.

