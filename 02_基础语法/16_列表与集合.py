#-*— coding:utf-8 -*-
#Auther: wangjiana
'''
    列表
        - 列表是Python的一个对象
        - 对象（object）就是内存中专门用来存储数据一块区域
        - 可以保存多个数据

'''


#创建列表
my_list = [ ]
#列表中所存储的数据称之为元素
my_list = [10]
#当列表中添加多个元素时，多个元素之间使用， 隔开
my_list = [1,2]
#列表中可以添加保存任意对象
my_list = [10,'hello',[1,2,3],print()]
print(my_list)
'''
    列表中的对象都会按照顺序存储到列表中
        第一个掺入的对象保存到第一位，依次而下
        通过索引来获取
'''

my_list = [10 , 20 ,30 ,40, 50]

# 访问列表中的值

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print(list1[0])
#分片的使用
print(list2[0:6])

# 更新列表

list = []          ## 空列表
list.append('Google')   ## 使用 append() 添加元素
list.append('Runoob')
print(list)

# 删除列表元素

list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2]
print(list1)


'''
Python包含以下函数:
1  cmp(list1, list2)
比较两个列表的元素
2	len(list)
列表元素个数
3	max(list)
返回列表元素最大值
4	min(list)
返回列表元素最小值
5	list(seq)
将元组转换为列表

Python包含以下方法:
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort(cmp=None, key=None, reverse=False)
对原列表进行排序
'''

print("----------------------------------")
#  集合

"""
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
    parame = {value01,value02,...}
或者
    set(value)
"""


# 去重功能
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# 快速判断元素是否在集合内

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
res='orange' in basket
print(res)

#下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')

# 集合a中包含而集合b中不包含的元素
res= a-b
print(res)

# 集合a或b中包含的所有元素
res= a|b
print(res)

# 集合a和b中都包含了的元素
res= a&b
print(res)

# 不同时包含于a和b的元素
res = a^b
print(res)

"""
集合的基本操作
1、添加元素
语法格式如下：
    s.add( x )
将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
"""
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)

# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
# s.update( x )
thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1,3})
print(thisset)

"""
2、移除元素
语法格式如下：
    s.remove( x )
将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
"""
thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset)

# 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
# s.discard( x )

thisset = set(("Google", "Runoob", "Taobao"))
thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)


"""
我们也可以设置随机删除集合中的一个元素，语法格式如下：
    s.pop() 
set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。
"""

thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()
print(x)

"""
计算集合元素个数
语法格式如下：
    len(s)
"""

thisset = set(("Google", "Runoob", "Taobao"))
res=len(thisset)
print(res)

"""
4、清空集合
语法格式如下：
    s.clear()
"""
thisset = set(("Google", "Runoob", "Taobao"))
thisset.clear()
print(thisset)
"""
判断元素是否在集合中存在
语法格式如下：
    x in s
"""
thisset = set(("Google", "Runoob", "Taobao"))
res="Runoob" in thisset
print(res)
res= "Facebook" in thisset
print(res)

"""
集合内置方法完整列表
方法	                        描述
add()	                        为集合添加元素
clear()	                        移除集合中的所有元素
copy()	                        拷贝一个集合
difference()	                返回多个集合的差集
difference_update()	            移除集合中的元素，该元素在指定的集合也存在。
discard()	                    删除集合中指定的元素
intersection()	                返回集合的交集
intersection_update()	        返回集合的交集。
isdisjoint()	                判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	                    判断指定集合是否为该方法参数集合的子集。
issuperset()	                判断该方法的参数集合是否为指定集合的子集
pop()	                        随机移除元素
remove()	                    移除指定元素
symmetric_difference()	        返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	                        返回两个集合的并集
update()	                    给集合添加元素

"""