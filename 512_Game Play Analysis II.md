####  512.  游戏玩家分析 II

SQL框架

```mysql
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int)
Truncate table Activity
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5')
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-05-02', '6')
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1')
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0')
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5')
```

Table: `Activity`

| Column Name  | Type |
| ------------ | ---- |
| player_id    | int  |
| device_id    | int  |
| event_date   | date |
| games_played | int  |

(player_id, event_date) 是这个表的两个主键
这个表显示的是某些游戏玩家的游戏活动情况
每一行是在某天使用某个设备登出之前登录并玩多个游戏（可能为0）的玩家的记录

请编写一个 SQL 查询，描述每一个玩家首次登陆的设备名称

查询结果格式在以下示例中：

Activity table:

| player_id | device_id | event_date | games_played |
| --------- | --------- | ---------- | ------------ |
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |

Result table:

| player_id | device_id |
| --------- | --------- |
| 1         | 2         |
| 2         | 3         |
| 3         | 1         |

#### MySQL解题01  :  where

先用where对Activity表进行过滤, 找出每一个玩家首次登陆的数据, 然后从中找出每一个玩家首次登陆的设备名称.

```mysql
select player_id, device_id
from  Activity
where 
    (player_id, event_date) 
    in 
    (select player_id, min(event_date) event_date from Activity group by player_id )
```



#### MySQL解题02  :  MySQL 变量 +  Case ...When... Else ...End用法

```mysql
select
    player_id, device_id
from (
    select 
        player_id, device_id,
        case
            when @player = player_id then @num := @num + 1
            when (@player := player_id) is not null then @num := 1
        end as num
    from 
        Activity a,
        (
            select
                @player := null,
                @num := null
        ) b 
    order by a.player_id, a.event_date
) t
where num = 1

```



#### MySQL解题03 :  窗口函数

```
select 
    player_id,
    device_id
from 
	(
    select 
        player_id,
        device_id,
        dense_rank() over(partition by player_id order by event_date) rnk
    from Activity
    ) t 
where rnk = 1
```

思路:

1)  dense_rank() over(partition by player_id order by event_date) 意思是在Activity表上新建一列,名为rnk, 这一列先根据player_id划分为几个区域, 然后在这几个区域分别按照event_date的无间隔排序(默认升序).

2)

(select player_id, device_id, dense_rank() over(partition by player_id order by event_date) rnk from Activity )t

生成了如下中间表t

| player_id | device_id | event_date | games_played | rnk  |
| --------- | --------- | ---------- | ------------ | ---- |
| 1         | 2         | 2016-03-01 | 5            | 1    |
| 1         | 2         | 2016-05-02 | 6            | 2    |
| 2         | 3         | 2017-06-25 | 1            | 1    |
| 3         | 1         | 2016-03-02 | 0            | 1    |
| 3         | 4         | 2018-07-03 | 5            | 2    |

然后用 select  player_id,  device_id from t where rnk = 1 得出下表

| player_id | device_id |
| --------- | --------- |
| 1         | 2         |
| 2         | 3         |
| 3         | 1         |