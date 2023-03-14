def count_args(**kwargs):
    print(len(kwargs))

count_args()
count_args(num=1)
count_args(num=1, state=True, msg="Hello")
count_args(num=1, state=True)
count_args(num=1, state=True, msg="Hello", val=2.5)


"""
0
1
3
2
4
"""
