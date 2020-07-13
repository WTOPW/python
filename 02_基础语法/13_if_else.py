#-*— coding:utf-8 -*-
#Auther: wangjiana

'''
    语法：
        if  条件表达式 :
            代码块
        elif 条件表达式 :
            代码块
        elif 条件表达式 :
            代码块
        elif 条件表达式 :
            代码块
        else :
            代码块
    注意：
        只有一个代码块被执行
        dead   code : 条件执行没有必要
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




