def count_args(*args, **kwargs):
    print(len(args), len(kwargs))

count_args(True, num=1, msg="Hello")
count_args(True, 2.3, msg="Hello")
count_args(1, 2.3, False, msg="Hello", val=5E-2)
count_args(num=1)
count_args(1)


"""
1 2
2 1
3 2
0 1
1 0
"""
