
#/usr/bin/python
#coding=utf-8

"""
此python程序是为了将leetcode测试用例json格式数据转成SQL insert语句。
使得测试用例可以导入本地mysql数据库，加速调试。
"""

import json

def get_mysql_sql_from_leetcodejson(json_str):
    '''
    json_str -- leetcode 题目的案例输入。通常是json串
    输出 -- SQL插入串 insert ... values
    '''
    jo = json.loads(json_str)
    res = []
    for db_name in jo['headers'].keys():
        col_list = jo['headers'][db_name]
        sql = 'insert into %s (%s) values' %(db_name,','.join(col_list))
        #print(sql)
        values = []
        for x in jo['rows'][db_name]:
            tos = ['NULL' if y is None else '\'%s\'' % (y) for y in x]
            values.append('(%s)' % (','.join(tos)))
        sql += ','.join(values)+';'
        res.append(sql)
    return res

json_str = input('input leetcode json string:')
for sql in get_mysql_sql_from_leetcodejson(json_str):
    print(sql)

Create table Person (PersonId int, FirstName varchar(255), LastName varchar(255))
Create table Address (AddressId int, PersonId int, City varchar(255), State varchar(255))
Truncate table Person
insert into Person (PersonId, LastName, FirstName) values ('1', 'Wang', 'Allen')
Truncate table Address
insert into Address (AddressId, PersonId, City, State) values ('1', '2', 'New York City', 'New York')

