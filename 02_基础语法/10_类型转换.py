#-*— coding:utf-8 -*-
#Auther: wangjiana
'''
    - 所谓的类型转换，将一个类型的对象装换为其他的对象
    - 类型转换不是改变对象的本身的类型，而是讲对象的值转换为新的对象
    - 类型转换的4个函数 int() float() str() bool()
        > int() : 可以将其他的对象转换为的整型,并不会的对原来的对象产生影响
            如果的希望修改原来的变量， 则需要对变量进行重新赋值
            规则：
                布尔值： True -> 1 False -> 0
                浮点数： 直接取整
                字符串： 合法的整数字符串，直接转换为对应的数字
                         如果不是一个合法的整数字符串，则报错
        > float() : 基本和int（）一致
        > str() :   字符串类型
        > bool() :  布尔值
                那些值表示空性 ： 0 None ' '
'''
a = True
print(type(int(a)))
b = int(123)
print(type(b))

