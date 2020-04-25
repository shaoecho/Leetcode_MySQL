####  2016年的投资

SQL框架

```mysql
reate table If Not Exists World (name varchar(255), continent varchar(255), area int, population int, gdp int)
Truncate table World
insert into World (name, continent, area, population, gdp) values ('Afghanistan', 'Asia', '652230', '25500100', '20343000000')
insert into World (name, continent, area, population, gdp) values ('Albania', 'Europe', '28748', '2831741', '12960000000')
insert into World (name, continent, area, population, gdp) values ('Algeria', 'Africa', '2381741', '37100000', '188681000000')
insert into World (name, continent, area, population, gdp) values ('Andorra', 'Europe', '468', '78115', '3712000000')
insert into World (name, continent, area, population, gdp) values ('Angola', 'Africa', '1246700', '20609294', '100990000000')
```

这里有张 World 表

| name    gdp             | continent | area    | population |
| ----------------------- | --------- | ------- | ---------- |
| Afghanistan    20343000 | Asia      | 652230  | 25500100   |
| Albania    12960000     | Europe    | 28748   | 2831741    |
| Algeria     188681000   | Africa    | 2381741 | 37100000   |
| Andorra   3712000       | Europe    | 468     | 78115      |
| Angola      100990000   | Africa    | 1246700 | 20609294   |

如果一个国家的面积超过300万平方公里，或者人口超过2500万，那么这个国家就是大国家。

编写一个SQL查询，输出表中所有大国家的名称、人口和面积。

例如，根据上表，我们应该输出:

| name        | population | area    |
| ----------- | ---------- | ------- |
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |

#### MySQL解题01  :

```mysql
# Write your MySQL query statement below
select 
    name, population, area 
from World
where area > 3000000 or population > 25000000
```

#### MySQL解题02  :

```mysql
SELECT
    name, population, area
FROM
    world
WHERE
    area > 3000000

UNION

SELECT
    name, population, area
FROM
    world
WHERE
    population > 25000000

```

#### 知识点: union

 **UNION 语句**：用于将不同表中相同列中查询的数据展示出来；（不包括重复数据）

**UNION ALL 语句**：用于将不同表中相同列中查询的数据展示出来；（包括重复数据）

