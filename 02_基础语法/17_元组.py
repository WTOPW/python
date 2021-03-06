#-*— coding:utf-8 -*-
#Auther: wangjiana

'''
    Python的元组与列表类似，不同之处在于元组的元素不能修改。
    元组使用小括号，列表使用方括号。
    元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

# 创建空元组
tup1 = ()
#元组中只包含一个元素时，需要在元素后面添加逗号
tup1 = (50,)

# 访问元组

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# 修改元组

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 删除元组

tup = ('Google', 'Runoob', 1997, 2000)
print(tup)
del tup
print("删除后的元组 tup : ")
print(tup)
'''
元素运算符

Python 表达式	                      结果	                           描述
len((1, 2, 3))	                    3	                                计算元素个数
(1, 2, 3) + (4, 5, 6)	            (1, 2, 3, 4, 5, 6)	                连接
('Hi!',) * 4	                    ('Hi!', 'Hi!', 'Hi!', 'Hi!')	    复制
3 in (1, 2, 3)	                    True	                            元素是否存在
for x in (1, 2, 3): print (x,)	    1 2 3                               迭代

元组索引，截取
Python 表达式	        结果	                    描述
L[2]	               'Runoob'     	        读取第三个元素
L[-2]	               'Taobao'	                反向读取，读取倒数第二个元素
L[1:]	               ('Taobao', 'Runoob')	    截取元素，从第二个开始后的所有元素。

元组内置函数
Python元组包含了以下内置函数

序号	方法及描述	
1	len(tuple)      计算元组元素个数。	        
2	max(tuple)      返回元组中元素最大值。
3	min(tuple)      返回元组中元素最小值。
4	tuple(iterable) 将列表转换为元组。
'''
