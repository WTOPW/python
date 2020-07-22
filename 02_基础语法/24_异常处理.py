#-*— coding:utf-8 -*-
#Auther: wangjiana

"""
Python 有两种错误很容易辨认：语法错误和异常。
    Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
异常
    即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
    大多数的异常都不会被程序处理，都以错误信息的形式展现在这里:


try/except
异常捕捉可以使用 try/except 语句。
语法
    try:
        # 执行代码
        pass
    except  [监控的异常]:
        # 发生异常处理代码
        pass

"""

while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
        
try :
    with open("D:/python/python/02_基础语法/22_输入和输出/code01/open.txt","r") as f :
        str = f.readline()
        print(str)
        f.close()
# 文件不存在
except FileNotFoundError:
    print("error!")


"""
try 语句按照如下方式工作；
    > 首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。
    > 如果没有异常发生，忽略 except 子句，try 子句执行后结束。
    > 如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
    > 如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。

一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:

except (RuntimeError, TypeError, NameError):
    pass
最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。

"""


import os
import sys
try :
    os.rmdir("test")
except Exception as e: # 把错误存到e变量中
    print("Exception : {0}".format(e))
    # 异常在此抛出
    print("Unexpected error:", sys.exc_info()[0])
    with open("error.txt","a+",encoding="utf-8") as f:
        f.write(str(e))
        f.close()


"""
    BaseException 所有异常的基类
　　SystemExit 解释器请求退出
　　KeyboardInterrupt 用户中断执行(通常是输入^C)
　　Exception 常规错误的基类
　　StopIteration 迭代器没有更多的值
　　GeneratorExit 生成器(generator)发生异常来通知退出
　　StandardError 所有的内建标准异常的基类
　　ArithmeticError 所有数值计算错误的基类
　　FloatingPointError 浮点计算错误
　　OverflowError 数值运算超出最大限制
　　ZeroDivisionError 除(或取模)零 (所有数据类型)
　　AssertionError 断言语句失败
　　AttributeError 对象没有这个属性
　　EOFError 没有内建输入,到达EOF 标记
　　EnvironmentError 操作系统错误的基类
　　IOError 输入/输出操作失败
　　OSError 操作系统错误
　　WindowsError 系统调用失败
　　ImportError 导入模块/对象失败
　　LookupError 无效数据查询的基类
　　IndexError 序列中没有此索引(index)
　　KeyError 映射中没有这个键
　　MemoryError 内存溢出错误(对于Python 解释器不是致命的)
　　NameError 未声明/初始化对象 (没有属性)
　　UnboundLocalError 访问未初始化的本地变量
　　ReferenceError 弱引用(Weak reference)试图访问已经垃圾回收了的对象
　　RuntimeError 一般的运行时错误
　　NotImplementedError 尚未实现的方法
　　SyntaxError Python 语法错误
　　IndentationError 缩进错误
　　TabError Tab 和空格混用
　　SystemError 一般的解释器系统错误
　　TypeError 对类型无效的操作
　　ValueError 传入无效的参数
　　UnicodeError Unicode 相关的错误
　　UnicodeDecodeError Unicode 解码时的错误
　　UnicodeEncodeError Unicode 编码时错误
　　UnicodeTranslateError Unicode 转换时错误
　　Warning 警告的基类
　　DeprecationWarning 关于被弃用的特征的警告
　　FutureWarning 关于构造将来语义会有改变的警告
　　OverflowWarning 旧的关于自动提升为长整型(long)的警告
　　PendingDeprecationWarning 关于特性将会被废弃的警告
　　RuntimeWarning 可疑的运行时行为(runtime behavior)的警告
　　SyntaxWarning 可疑的语法的警告
　　UserWarning 用户代码生成的警告
"""

# try ...except..finally  强制执行的代码


import os
import sys
try :
    os.rmdir("test")
except Exception as e: # 把错误存到e变量中
    print("Exception : {0}".format(e))
    # 异常在此抛出
    print("Unexpected error:", sys.exc_info()[0])
    with open("error.txt","a+",encoding="utf-8") as f:
        f.write(str(e))
        f.close()
finally:
    print("I am best one")


"""
try/except...else
try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。



"""
import os
import sys
try :
    os.rmdir("test")
except Exception as e: # 把错误存到e变量中
    print("Exception : {0}".format(e))
    # 异常在此抛出
    print("Unexpected error:", sys.exc_info()[0])
    with open("error.txt","a+",encoding="utf-8") as f:
        f.write(str(e))
        f.close()
else: #不报错执行代码
    print("error")
finally:
    print("I am best one")


"""
    Python 使用 raise 语句抛出一个指定的异常。   
raise语法格式如下：
    raise [Exception [, args [, traceback]]]

x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
"""

# 预定义的清理行为 f.close  end=""
with open("error.txt") as f:
    for line in f:
        print(line, end="")








