x = [1,2,3]

def weird(num, default_ls=None):
    default_ls = default_ls or []
    default_ls.append(num)
    print(default_ls)
    return default_ls

weird(1)
weird(2)
weird(3)
ls = list()
ls = weird(99, ls)  # [99]
print(ls)
weird(1000001, ls) # [99, 100001]    [10000001]

"""

MacBook-Pro:random_python_stuff demouser$ python data_types.py
[1]
[1, 2]
[1, 2, 3]
"""
