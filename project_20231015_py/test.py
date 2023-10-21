# # 这是一个简单的Python程序，演示如何使用while循环。

# # 初始化一个计数器变量
# counter = 1

# # 使用while循环来执行一段代码块，直到条件不再满足
# while counter <= 5:
#     # 在循环中输出计数器的值
#     print("这是第", counter, "次循环。")

#     # 更新计数器变量，以便逐渐增加
#     counter += 1

# # 当条件不再满足（计数器大于5），循环结束
# print("循环结束。")

# # 请注意：在这个示例中，我们使用了一个计数器变量（counter）来跟踪循环的次数。
# # while循环会不断执行循环内的代码块，直到条件（counter <= 5）不再满足。
# # 在每次循环迭代中，我们打印出当前计数器的值，然后逐渐递增计数器。
# # 循环会在计数器的值大于5时结束，然后打印出"循环结束"的消息。

# # 这是一个简单的循环示例，但很有帮助，因为循环是编程中常见的概念，它允许你重复执行一段代码，直到满足某个条件。希望这个示例有助于初学者理解while循环的基本用法。

# counter=5
# while counter<=5:
#     print("这是第",counter,"次循环。")
#     counter+=1
# if counter==5:
#     print("循环结束。")

# #下面是一个简单的猜数字游戏，演示如何使用while循环。(line34-60)
# import random

# # 生成一个随机整数，范围在1到100之间
# secret_number = random.randint(1, 100)

# # 初始化猜测次数
# guess_count = 0

# print("欢迎来到猜数字游戏！")
# print("我已经选择了一个1到100之间的秘密数字。")

# while True:
#     try:
#         # 获取玩家的猜测
#         user_guess = int(input("请猜一个数字: "))
#         guess_count += 1

#         if user_guess < secret_number:
#             print("太小了，再试试吧。")
#         elif user_guess > secret_number:
#             print("太大了，再试试吧。")
#         else:
#             print(f"恭喜你，你猜对了！答案是 {secret_number}，你用了 {guess_count} 次猜中了。")
#             break

#     except ValueError:
#         print("请输入一个有效的整数。")

# print("游戏结束。感谢参与！")

# a="++++****hello****"
# b=a.lstrip("*+")
# print(b)

# name=input("请输入名字：")
# saying="'A person who never made a mistake never tried anything new.'"
# name_saying=f"{name.strip('*')} once said,{saying}"
# print(name_saying)

# 用_分割数字
# num=100_000_000_000
# print(num)

#python没有内置常量，但是可以用大写字母表示常量
# MAX_CONNECTIONS = 5000
# print(MAX_CONNECTIONS)
# MAX_CONNECTIONS = 10000
# print(MAX_CONNECTIONS)

# import this

# from functools import reduce
# n = int(input("请输入一个整数："))
# result = reduce(lambda x, y: x + y, [reduce(lambda x, y: x * y, range(1, i + 1)) for i in range(1, n + 1)])
# print(result)

# 列表 索引从0而不是1开始 用-1表示最后一个元素，正反都可以
# names=["zhangsan","lisi","wangwu"]
# print(names[-1].upper())
# message=f"{names[0].title()},你好！"
# print(message)

# 3.2.1修改列表元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'  # 修改列表元素
# print(motorcycles)

# 3.2.2在列表中添加元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles.append('ducati')  # 在列表末尾添加元素
# print(motorcycles)

# motorcycles = []  # 创建一个空列表
# print(motorcycles)
# motorcycles.append('honda')  # 在列表末尾添加元素
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles[2].upper())

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles.insert(1, 'ducati')  # 在列表任意位置添加元素
# print(motorcycles)

# my try
# names=["zhangsan","lisi","wangwu"]
# print(names)
# names.insert(2,"mazi")
# print(names[2].title())

# 3.2.3从列表中删除元素

# print('hello world')
import this