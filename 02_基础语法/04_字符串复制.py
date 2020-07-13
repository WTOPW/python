#-*— coding:utf-8 -*-
#Auther: wangjiana
#使用4种方式输出，欢迎光临

name =  'wtopw'
#拼串
print('欢迎'+name+ '光临！')
#多个参数
print('欢迎',name,'光临！')
#占位符
print('欢迎 %s 光临！'%name)
#格式化字符串
print(f'欢迎{name}光临！ ')

'''
    字符串的复制
    字符串和数字相乘，则解释器会将字符串重复的次数并返回
'''

a = 'abc'
a = a * 20
print(a)