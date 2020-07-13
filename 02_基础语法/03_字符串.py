#-*— coding:utf-8 -*-
#Auther: wangjiana

"""
    字符串：
        用来表示的一段文本信息，在python的表示字符串需要用引号引用起来
        可以是单引号，也可以使得双引号；不要混着用
        相同的引号之间不能嵌套；单引号与双引号不能的跨行使用
        长字符串：使用三重引号的来表示一个长字符串
        ''' '''
        \""" \"""

"""
str = 'hello'
test = "hello"
test_01 = '子曰："学而时习之"'
test_02 = '子曰：\
"学而时习之" \
          '
test_03= '''子曰：
"学而时习之" '''
print(str,test)
print(test_01)
print(test_02)
print(test_03)

'''
    转义字符 \ ,通过转义，可以在字符中表示一些特俗的内容
    例子：
        \' : 表示 ’ 
        \" : 表示 "
        \t ：表示制表符
        \n : 表示换行符
        \\ ：表示反斜杠
        \\uxxxx : 表示unicode的编码
    
'''
test_04 = "子曰：\"学而时习之\""
print(test_04)

"""
    占位符
        %s ： 创建字符串的表示任意长度
        %f ：浮点数的占位符
        %d ：整数占位符
"""
#俩个字符串的相加，则俩个的字符串会合并
str_01 = 'a,b'
str_02 = 'c,d'
str_03 = str_01 + str_02
print(str_03)
#占位符 %s
str_04 = "hello %s"% 'test'
str_05 = "hello %s  %s"% ('tomcat ','test')
#限制字符串的最小位数3.5字符串限制在3到5之间
str_06 = "hello %3.5s  %3s"% ('tomcar ','test')
#限制小数的长度
str_07 = "%.2f"%2.234233
'''
    格式化字符串   
        可以通过的在字符串添加一个f来创建一个格式化字符串
        在格式化字符串中可以直接嵌入变量
'''
a = 123
b = 456
str_08 = f'hello{a}{b}'
print(str_07)


Game_display = """
--------------------------------------<welcome {a} to this games>----------------------------------------------------
Choose your role : 1、唐僧 2、白骨精
""".format(a = "Game player")
print(Game_display)


Game_display01 = """
--------------------------------------<welcome %s to this games>----------------------------------------------------
Choose your role : 1、唐僧 2、白骨精
"""% ("Game player")
print(Game_display)
