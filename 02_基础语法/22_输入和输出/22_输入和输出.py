# -*— coding:utf-8 -*-
# Auther: wangjiana
"""
字符串格式化
Python两种输出值的方式: 表达式语句和 print() 函数。
    第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
    如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
    如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
        > str()： 函数返回一个用户易读的表达形式。
        > repr()： 产生一个解释器易读的表达形式。

"""
# 实例一

s = 'Hello, wtopw'
print(str(s))
print(repr(s))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

"""
注意：   > 在第一个例子中, 每列间的空格由 print() 添加。
         > 这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
         > 还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串
"""

# str.format() 的基本使用如下:
print('{}网址： "{}!"'.format('教程', 'www.wtopw.com'))

"""
    > 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
    > 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：
"""
print('{0} 和 {1}'.format('Google', 'wtopw'))

# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print('{name}网址： {site}'.format(name='教程', site='www.wtopw.com'))

# 位置及关键字参数可以任意的结合:
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'wtopw', other='Taobao'))

# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:

import math

print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))

# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
import math

print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'wtopw': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

"""
    > 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
    > 最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值 :
"""

table = {'Google': 1, 'wtopw': 2, 'Taobao': 3}
print('wtopw: {0[wtopw]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

# 也可以通过在 table 变量前使用 ** 来实现相同的功能：
table = {'Google': 1, 'wtopw': 2, 'Taobao': 3}
print('wtopw: {wtopw:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

"""
旧式字符串格式化
    % 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串. 例如:

import math
print('常量 PI 的值近似为：%5.3f。' % math.pi)
常量 PI 的值近似为：3.142。
因为 str.format() 是比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().
"""

"""
读取键盘输入
    Python提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
    input 可以接收一个Python表达式作为输入，并将运算结果返回。
"""
str = input("请输入：");
print("你输入的内容是: ", str)

"""
读和写文件
open() 将会返回一个 file 对象，基本语法格式如下:
    open(filename, mode)
    > filename：包含了你要访问的文件名称的字符串值。
    > mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
不同模式打开文件的完全列表：

模式	描述
r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	    以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
r+	    打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	    以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	    打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	    以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+	    打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	    以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	    打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""

#  详细见code
import os
with open("D:/python/python/02_基础语法/22_输入和输出/code01/open.txt","w") as f :
    f.write("hello")
    f.close()

with open("D:/python/python/02_基础语法/22_输入和输出/code01/open.txt","r") as f :
    str =f.readline()
    print(str)
    f.close()
