import deffunction
# done = 2;
# if done == 1:
#     print("stronghwan")
# elif done == 2:
#     print("stronghwan elif")
# else:
#     print("error");

# i = 1
# while i <= 5:
#     print("stronghwan")
#     i = i + 1
# deffunction.hello(1)
# print(deffunction.hello2(1, 2))

# name_list = ["zhangsan", "stronghwan", "lisi", "hhah"]
# print(name_list.index("hhah"))

# print(name_list[0])

# print("-" * 20)

# for i in name_list:
#     print("名字是:%s"%i)
# 字典
# name_map = {"name" : "stronghwan",
#             "age"  : 18
#         }
# print(name_map["name"])


# for k in name_map:
#     print("%s - %s" %(k,name_map[k]))
# 字富春
# strname = "stronghwan"
# for s in strname:
#     print(s)

# print(len(strname))
# print(strname.count("s"))
# print(strname.index("s"))
# print(strname.isspace())

# def testi(a):
#     a= a + 1

# a = 1
# testi(a)
# print(a)
# print(id(a))


# list = list(map(str, [1,2,3]))
# for item in list:
#     print(item)

# def f(x, y):
#       result = 1
#       for i in range(1, y - x):
#             result *= i
#       return result
# x = list(map(f, (0, 2, 4), range(5, 8)))
# print(x)





def sushu():
    result_list = []
    for tar in range(3, 100):
        flag = 0
        for k in range(2,tar):
            if(tar % k == 0):
                flag = 1
        if(flag == 0):
            result_list.append(tar)

    print(max(result_list))
sushu();

def zh(a, b):
    m = max(a,b)
    n = min(a,b)
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n

    print(n)

zh(10, 15)
