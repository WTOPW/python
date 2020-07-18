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