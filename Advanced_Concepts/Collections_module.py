# from collections import OrderedDict
#
# roll_no = OrderedDict([
#     (11, 'Shubham'),
#     (9, 'Pankaj'),
#     (17, 'JournalDev'),
# ])
#
# for key, value in roll_no.items():
#     print(key, value)



#The default dictionary can contain duplicate keys. The advantage of using default
# dictionary is that we can collect items which belong to the same key.
# Let’s look at a code snippet which demonstrates the same:
# from collections import defaultdict
#
# marks = [
#     ('Shubham', 89),
#     ('Pankaj', 92),
#     ('JournalDev', 99),
#     ('JournalDev', 98)
# ]
#
# dict_marks = defaultdict(list)
#
# for key, value in marks:
#     dict_marks[key].append(value)
#
# print(list(dict_marks.items()))


#The Counter collections allow us to keep a count of all the items which are inserted into the collection with the keys.
# Here is a sample program to show how it works:
# from collections import Counter
#
# marks_list = [
#     ('Shubham', 89),
#     ('Pankaj', 92),
#     ('JournalDev', 99),
#     ('JournalDev', 98)
# ]
#
# count = Counter(name for name, marks in marks_list)
# print(count)


# We can convert this Tuple to a Named tuple by assigning a name to all values present in this tuple.
# This will give a lot more context to the data present as well:
# Important - key names cannot be Python keywords.
# import collections
#
# User = collections.namedtuple('User', 'name age gender')
# shubham = User(name='Shubham', age=23, gender='M')
# print(shubham)
#
# print('Name of User: {0}'.format(shubham.name))


# A Deque is a double-ended queue which allows us to add and remove elements from both the ends.
# This enhances the capabilities of a stack or a queue. Here is a sample program:

# import collections
#
# name = collections.deque('Shubham')
# print('Deque       :', name)
# print('Queue Length:', len(name))
# print('Left part   :', name[0])
# print('Right part  :', name[-1])
#
# name.remove('b')
# print('remove(b):', name)

# So, the dequeueing of the elements was done automatically. We can also insert elements in a Dequeue on a specific end. Let’s try it:
# import collections
#
# name = collections.deque('Shubham')
# print('Deque       :', name)
#
# name.extendleft('...')
# name.append('-')
# print('Deque       :', name)


class Sample():

    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
obj1 = Sample()
print(dir(obj1))

