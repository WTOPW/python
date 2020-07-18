#-*— coding:utf-8 -*-
#Auther: wangjiana

'''
    循环体：
        while
            语法：
                while 条件表达式 ：
                    代码块
                else :
                    代码块
        for <variable> in <sequence>:
            <statements>
        else:
            <statements>
'''
#练习1
#   100内的奇数之和
#i = 0
#sum = 0
#while i < 100 :
#    i = i + 1
#    if i % 2 != 0 :
#        sum = sum + i
#print(sum)



#执行脚本后，在循环到 "Google"时会跳出循环体：
sites = ["Baidu", "Google","Taobao"]
for site in sites:
    if site == "Google":
        print("Google!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


#range()函数

a = ['Google', 'Baidu','Taobao', 'QQ']
for i in range(len(a)):
   print(i, a[i])




#    break 和 continue 语句及循环中的 else 子句
#        break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
#        continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
#        pass   判断循环语句占位的
#        俩次循环只对最近的循环起作用

#实例一 while 中使用 break：
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')

'''
    输出结果为：
    4
    3
    循环结束。
'''

#实例二 while 中使用 continue：
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')

'''
输出的结果为：
    4
    3
    1
    0
    循环结束。
'''