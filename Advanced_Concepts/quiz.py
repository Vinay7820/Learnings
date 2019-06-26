########Merging two dictionary##############
#  d1 = {'Name':'Vinay', 'Age':26}
# d2 = {'Address':'BTM', 'Company':'Brillio'}
# d1.update(d2)
# print(d1)

#####Looping through list of list#############
# l1 = [1,2,3,4]
# l2 = [5,6,7]
# l1.append(l2)
# print(l1)
# # print(len(l1))
# for _ in l1:
#     if type(_) == list and len(_) > 1:
#         for i in _:
#             print(i)
#     else:
#         print(_)


#########Execution time difference between lambda and normal for loop#############
# import time
# start = time.time()
# def divisible():
#     a = []
#     for x in range(0, 100000000):
#         if x % 7 == 0 and x % 5 == 0:
#             a.append(x)
#
# divisible()
# end = time.time()
# print((end - start))

###LambdaFunction###
# import time
# start = time.time()
# condition = [x for x in range(0, 100000000) if x % 7 == 0 and x % 5 == 0 ]
# end = time.time()
# print(end - start)

#####Reading a File  without loading the entire file into memory######

# with open("file.txt") as f:
#     for line in f:
#         process_line(line)
# It won't slurp the whole file into memory like read() or readlines() does.

# If for some reason you want to read the file in fixed sized chunks, then try this:
# with open("file.txt") as f:
#     for chunk in iter(lambda: f.read(128), ""):
#         process_chunk(chunk)


# def read_in_chunks(f, size=128):
#     while True:
#         chunk = f.read(size)
#         if not chunk:
#             break
#         yield chunk
#
#
# with open("file.txt") as f:
#     for chunk in read_in_chunks(f):
#         process_chunk(chunk)

#####Sort tuple/lists according to the index specified#######
# def sort(tuples):
#     return sorted(tuples, key=lambda tup: tup[2])
#
#
# a1 = [(23, 45, 20), (25, 44, 39), (89, 40, 23)]
# a = [[4,5,6],[1,2,3],[7,8,9]]
# print("Sorted:"),
# print(sort(a))


# dict1 = {'Name': 'Zara', 'Age': 7};
# dict2 = dict1.copy()
# print ("New Dictionary : %s" %  str(dict2))
# dict2['Devre'] = "Anjaneya"
# print(dict1)
# print(dict2)

# The list contains the names of all the modules, variables and functions that are defined in a module.
# Import built-in module math
# import math
# content = dir(math)
# print (content)
# print(dir.__name__)
# print(dir.__module__)
# print(dir.__doc__)
# print(dir.__init__())

# In python, dir() shows a list of attributes for the object passed in as argument ,
# without an argument it returns the list of names in the current local namespace
# print(dir)
# print(dir('acos'))

# In Python, help() is a super useful built-in function that can be used to return the Python documentation of a particular object, method, attributes, etc.
# my_list = []
# help(my_list.append)

# import sys
#
# s1 = 0
# s2 = 0
#
# n = int(input().strip())
# a = []
# for a_i in range(n):
#     a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
#     a.append(a_t)
# print(a)
#
# for i in range(n):
#     s1 += a[i][i]
#     s2 += a[-i - 1][i]
#
# print(abs(s1 - s2))
