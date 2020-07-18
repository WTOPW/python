#-*— coding:utf-8 -*-
#Auther: wangjiana

'''
    语法：
    if condition_1:
        statement_block_1
    elif condition_2:
        statement_block_2
    else:
        statement_block_3
    如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
    如果 "condition_1" 为False，将判断 "condition_2"
    如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
    如果 "condition_2" 为False，将执行"statement_block_3"块语句
    注意：
        1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
        2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
        3、在Python中没有switch – case语句
'''



'''
    练习1
        编写一个程序，获取一个的用户输入的整数。然后通过程序显示这个是奇数还是偶数
'''
#num = int(input("输入一个数"))
#if num % 2 == 0 :
#    print(num ,"是偶数")

'''
    练习2
        判断一个年份可以被4整除不能被100 整除，或者可以被400整除，这个年份就是闰年
'''
#year = int(input("输入一个年份 ："))
#if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#    print(year,"这个年分是闰年")
'''
    练习3
        年龄换算
'''
num_year = int(input("狗的年龄："))
if num_year < 0 :
    print("年纪不能为负数")
elif num_year ==  1 :
    print("年纪为",10.5 )
elif num_year ==  2 :
    print("年纪为",10.5 * 2 )
elif num_year >= 3 :
    num_year = 10.5 * 2 + (num_year - 2 )* 4
    print("年纪为",num_year)



'''
操作符	    描述
<	        小于
<=	        小于或等于
>	        大于
>=	        大于或等于
==	        等于，比较两个值是否相等
!=	        不等于
'''
