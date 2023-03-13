def count_args(*args):
    print(len(args))

count_args()
count_args(1)
count_args(1, True, "Hello")
count_args(1, True)
count_args(1, True, "Hello", 2.5)


"""
0
1
3
2
4
"""
