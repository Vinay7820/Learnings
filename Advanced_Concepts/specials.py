# Iterable is a “sequence” of data, you can iterate over using a loop.
# The easiest visible example of iterable can be a list of integers - [1, 2, 3, 4, 5, 6, 7].
# It’s possible to iterate over other types of data like strings, dicts, tuples, sets, etc.
# Basically, any object that has iter() method can be used as an iterable. You can check it using hasattr() function.

# print(hasattr(list, '__iter__'))


# The generator yields one item at a time — thus it is more memory efficient than a list.

# from sys import getsizeof
# my_comp = [x * 5 for x in range(1000)]
# my_gen = (x * 5 for x in range(1000))
# print(getsizeof(my_comp))
# print(getsizeof(my_gen))

# If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list.
# If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

# for num in range(10,20):     #to iterate between 10 to 20
#    for i in range(2,num):    #to iterate on the factors of the number
#       if num%i == 0:         #to determine the first factor
#          j=num/i             #to calculate the second factor
#          print ('%d equals %d * %d' % (num,i,j))
#          break #to move to the next number, the #first FOR
#    else:                  # else part of the loop
#       print (num, 'is a prime number')

# str = "this is string example....wow!!!";
# print (str.isalnum())    ####No space, special characters should be there


# tup = ('physics', 'chemistry', 1997, 2000);
# del (tup[0])   ##TypeError: 'tuple' object doesn't support item deletion
# print(tup)
# del tup;
# print(tup)


# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# del dict['Name']; # remove entry with key 'Name'
# dict.clear();     # remove all entries in dict
# del dict ;        # delete entire dictionary


# dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
# print ("dict['Name']: ", dict['Name'])

