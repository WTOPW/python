#-*— coding:utf-8 -*-
#Auther: wangjiana

# 以下实例将字符串写入到文件 foo.txt 中：

# 打开一个文件
#f = open("D:\\python\\python\\02_基础语法\\22_输入和输出\\code01\\open.txt", "w")
f = open("D:/python/python/02_基础语法/22_输入和输出/code01/open.txt", "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# 关闭打开的文件
f.close()



"""
f.read()
为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
以下实例假定文件 foo.txt 已存在（上面实例中已创建）：
"""

# 打开一个文件
f = open("D:/python/python/02_基础语法/22_输入和输出/code01/open.txt", "r")
str = f.read()
print(str)
# 关闭打开的文件
f.close()

"""
f.readline()
f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
"""

# 打开一个文件
f = open("D:/python/python/02_基础语法/22_输入和输出/code01/open.txt", "r")
str = f.readline()
print(str)
# 关闭打开的文件
f.close()


"""
f.readlines()
f.readlines() 将返回该文件中包含的所有行。
如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
"""
# 打开一个文件
f = open("D:/python/python/02_基础语法/22_输入和输出/code01/open.txt", "r")
str =  f.readlines()
print(str)
# 关闭打开的文件
f.close()


# 另一种方式是迭代一个文件对象然后读取每行:
# 打开一个文件
f = open("D:/python/python/02_基础语法/22_输入和输出/code01/open.txt", "r")
for line in f:
    print(line, end='')
# 关闭打开的文件
f.close()

"""
这个方法很简单, 但是并没有提供一个很好的控制。 因为两者的处理机制不同, 最好不要混用。
f.write()
f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
"""
# 打开一个文件
f = open("D:/python/python/02_基础语法/22_输入和输出/code01/open.txt", "w")
num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
# 关闭打开的文件
f.close()

"""
f.tell()
f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
    > seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
    > seek(x,1) ： 表示从当前位置往后移动x个字符
    > seek(-x,2)：表示从文件的结尾往前移动x个字符
    > from_what 值为默认为0，即文件开头。下面给出一个完整的例子：
"""
f = open("D:/python/python/02_基础语法/22_输入和输出/code01/open01.txt", 'rb+')
f.write(b'0123456789abcdef')
# 移动到文件的第六个字节
print(f.seek(5))
print(f.read(1))
# 移动到文件的倒数第三字节
print(f.seek(-3, 2))
f.close()

"""
f.close()
在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。
当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。
当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:
"""

with open('D:/python/python/02_基础语法/22_输入和输出/code01/open.txt', 'r') as f:
    read_data = f.read()
    print(read_data)
f.closed

"""
pickle 模块
    python的pickle模块实现了基本的数据序列和反序列化。
    通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
    通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
基本接口：
    pickle.dump(obj, file, [,protocol])
有了 pickle 这个对象, 就能对 file 以读取的形式打开:
    x = pickle.load(file)
    注解：从 file 中读取一个字符串，并将它重构为原来的python对象。
file: 类文件对象，有read()和readline()接口。
"""
import pickle
# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()

import pprint, pickle
#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()

"""
Python3 File(文件) 方法
open() 方法
Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
    open(file, mode='r')
完整的语法格式为：
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
参数说明:
    > file: 必需，文件路径（相对或者绝对路径）。
    > mode: 可选，文件打开模式
    > buffering: 设置缓冲
    > encoding: 一般使用utf8
    > errors: 报错级别
    > newline: 区分换行符
    > closefd: 传入的file参数类型

mode 参数有：

模式	描述
t	文本模式 (默认)。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
+	打开一个文件进行更新(可读可写)。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
【*】默认为文本模式，如果要以二进制模式打开，加上 b 。

file 对象
file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：


序号	方法及描述
1	file.close()                关闭文件。关闭后文件不能再进行读写操作。
2   file.flush()                刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
3   file.fileno()               返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
4	file.isatty()               如果文件连接到一个终端设备返回 True，否则返回 False。
5	file.next()                 Python 3 中的 File 对象不支持 next() 方法。返回文件下一行。
6	file.read([size])           从文件读取指定的字节数，如果未给定或为负则读取所有。
7	file.readline([size])       读取整行，包括 "\n" 字符。
8	file.readlines([sizeint])   读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
9	file.seek(offset[, whence]) 移动文件读取指针到指定位置
10	file.tell()                 返回文件当前位置。
11	file.truncate([size])       从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。
12	file.write(str)             将字符串写入文件，返回的是写入的字符长度。
13	file.writelines(sequence)   向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
"""