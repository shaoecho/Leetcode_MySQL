####  树节点

SQL框架

给定一个表 tree，id 是树节点的编号， p_id 是它父节点的 id 。

```mysql
Create table If Not Exists tree (id int, p_id int)
Truncate table tree
insert into tree (id, p_id) values ('1', 'None')
insert into tree (id, p_id) values ('2', '1')
insert into tree (id, p_id) values ('3', '1')
insert into tree (id, p_id) values ('4', '2')
insert into tree (id, p_id) values ('5', '2')
```

树中每个节点属于以下三种类型之一：

叶子：如果这个节点没有任何孩子节点。
根：如果这个节点是整棵树的根，即没有父节点。
内部节点：如果这个节点既不是叶子节点也不是根节点。


写一个查询语句，输出所有节点的编号和节点的类型，并将结果按照节点编号排序。上面样例的结果为：

| id   | Type  |
| ---- | ----- |
| 1    | Root  |
| 2    | Inner |
| 3    | Leaf  |
| 4    | Leaf  |

解释

节点 '1' 是根节点，因为它的父节点是 NULL ，同时它有孩子节点 '2' 和 '3' 。
节点 '2' 是内部节点，因为它有父节点 '1' ，也有孩子节点 '4' 和 '5' 。
节点 '3', '4' 和 '5' 都是叶子节点，因为它们都有父节点同时没有孩子节点。
样例中树的形态如下：


			  1
			/   \
	                  2       3
	                /   \
	              4       5

**注意**

如果树中只有一个节点，你只需要输出它的根属性。



#### MySQL解题01  :  用 两个`IF` 函数嵌套.

```mysql
SELECT
    atree.id,
    IF(ISNULL(atree.p_id),
        'Root',   -- 若atree.p_id为null, 则返回Root
        IF(atree.id IN (SELECT p_id FROM tree), 'Inner','Leaf')) as Type
FROM tree atree  #此处用FROM tree,atree会报错,加了逗号相当于与inner join???
ORDER BY atree.id
```

if（expr,v1,v2）若expr是TRUE（即：expr结果非 0 也非null），则该函数返回值为v1，否则返回值为v2。

第一个if判断, 判断p_id是否为空, 为空说明此id没有父节点, 类型是root. 若不为空,说明有父节点,继续下一个if判断.

第二个if判断, 表达式是atree.id IN (SELECT p_id FROM tree)

​			表达式为真时, 表示此id有子节点, 又结合第一个if判断说明有父节点, 则此id类型是内部节点(Inner).

​			表达式为假时, 表示此id没有子节点, 又结合第一个if判断说明有父节点, 则此id类型是叶子(Leaf).



#### MySQL解题02  : in

```mysql
select id, (case
            	when id in (select id from tree where p_id is null) then "Root"
            	when id in (select p_id from tree) then "Inner"
            	else "Leaf"
            end) as  Type
from tree
order by id
```

when id in (select id from tree where p_id is null) then "Root" 表示当p_id为null时, 对应的id是根节点.

主要逻辑是,

 先判断p_id是否为null, 是null就是根节点, 否则就不是根节点, 

然后继续判断, id in (select p_id from tree) 为真说明有子节点, 加上上一步判断了不是根节点, 说明是中间节点.

其余剩下来的就是叶.



#### MySQL解题03  : not in

```mysql
select id,
(case
    when p_id is null then "Root"
    when id not in (select ifnull(p_id,0) from tree) then "Leaf"   # 注意! 
    else "Inner" 
end) as Type
from tree
order by id
```

1)  用not in 的时候 一定要排除null的情况 , 否则会执行失败，因为NULL和任何值都不相等. 此处用的是ifnull(,)

2)  ifnull(p_id,0) 表示当p_id为null时, p_id取0. 相当于排除了p_id=null的情况.

3)  也可用not exists 代替 not in ().

```mysql
select id,
(case
    when p_id is null then "Root" 
 	when id not exists (select p_id from tree) then "Leaf"   ####为啥报错??
    else "Inner" 
end) as Type
from tree
order by id
```

#### MySQL解题04  :使用 `UNION

我们可以按照下面的定义，求出每一条记录的节点类型。

Root: 没有父节点
Inner: 它是某些节点的父节点，且有非空的父节点
Leaf: 除了上述两种情况以外的节点

1)   根节点是没有父节点的节点。

```mysql
SELECT id, 'Root' AS Type
FROM tree
WHERE p_id IS NULL
```

2)   叶子节点是没有孩子节点的节点，且它有父亲节点。

```mysql
SELECT id, 'Leaf' AS Type
FROM tree
WHERE 
	id NOT IN  (select distinct  p_id from tree where p_id is not null )  #表示没有子节点
	and 
	p_id IS NOT NULL #表示有父节点
```

3)  内部节点是有孩子节点和父节点的节点。

```mysql
SELECT id, 'Inner' AS Type
FROM tree
WHERE 
	id IN  (select distinct  p_id from tree where p_id is not null )  #表示有子节点
	and 
	p_id IS NOT NULL #表示有父节点
```

4) 用UNION 操作符连接两个以上的 SELECT 语句的结果组合到一个结果集合中。

```mysql
SELECT id, 'Root' AS Type
FROM tree
WHERE p_id IS NULL

UNION

SELECT id, 'Leaf' AS Type
FROM tree
WHERE 
	id NOT IN  (select distinct  p_id from tree where p_id is not null )  #表示没有子节点
	and 
	p_id IS NOT NULL #表示有父节点

UNION

SELECT id, 'Inner' AS Type
FROM tree
WHERE 
	id IN  (select distinct  p_id from tree where p_id is not null )  #表示有子节点
	and 
	p_id IS NOT NULL #表示有父节点
```



