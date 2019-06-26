# class A:
#     def __init__(self, i = 0):
#         self.i = i
#
# class B(A):
#     super(B, self).__init__(i)
#     def __init__(self, j = 0):
#         self.j = j
#
# def main():
#     b = B()
#     print(b.i)
#     print(b.j)
#
# main()
#
#
#
#
#
# Q1. Which Of The Following Statements Are Correct About The Given Code Snippet?
# 1.	class A:
# 2.	def __init__(self, i = 0):
# 3.	self.i = i
# 4.
# 5.	class B(A):
# 6.	def __init__(self, j = 0):
# 7.	self.j = j
# 8.
# 9.	def main():
# 10.	b = B()
# 11.	print(b.i)
# 12.	print(b.j)
# 13.
# 14.	main()
# A. Class B inherits A, but the data field “i” in A is not inherited.
# B. Class B inherits A, thus automatically inherits all data fields in A.
# C. When you create an object of B, you have to pass an argument such as B(5).
# D. The data field “j” cannot be accessed by object b.
# Q2. Which Of The Following Statements Is True?
# A. By default, the __new__() method invokes the __init__ method.
# B. The __new__() method is defined in the object class.
# C. The __init__() method is defined in the object class.
# D. The __str__() method is defined in the object class.
# E. The __eq__(other) method is defined in the object class.
#
# Q3. What Will Be The Output Of The Following Code Snippet?
# class A:
#     def __init__(self):
#         self.calcI(30)
#         print("i from A is", self.i)
#     def calcI(self, i):
#         self.i = 2 * i;
# class B(A):
#     def __init__(self):
#         super().__init__()
#     def calcI(self, i):
#         self.i = 3 * i;
# b = B()
# Q4. What Will Be The Output Of The Following Code Snippet?
# class A:
#     def __init__(self):
#         self.calcI(30)
#     def calcI(self, i):
#         self.i = 2 * i;
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("i from B is", self.i)
#     def calcI(self, i):
#         self.i = 3 * i;
# b = B()
# Q5. Which Of The Following Can Be Used To Invoke The __init__ Method In B From A, Where A Is A Subclass Of B?
# A. super().__init__()
# B. super().__init__(self)
# C. B.__init__()
# D. B.__init__(self)
# Q6. Which Of The Following Statements Are Correct About The Given Code Snippet?
# class A:
#     def __init__(self, i = 0):
#         self.i = i
# class B(A):
#     def __init__(self, j = 0):
#         self.j = j
# def main():
#     b = B()
#     print(b.i)
#     print(b.j)
# main()
# A. Class B inherits A, but the data field “i” in A is not inherited.
# B. Class B inherits A, thus automatically inherits all data fields in A.
# C. When you create an object of B, you have to pass an argument such as B(5).
# D. The data field “j” cannot be accessed by object b.
# Q7. What Will Be The Output Of The Following Code Snippet?
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)
# Q8. What Will Be The Output Of The Following Code Snippet?
# arr = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(arr[i].pop())
# Q9. What Will Be The Output Of The Following Code Snippet?
# def f(i, values = []):
#     values.append(i)
#     print (values)
#     return values
# f(1)
# f(2)
# f(3)
# Q10. What Will Be The Output Of The Following Code Snippet?
# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print (sum)
#
#
#
#
#
import json
# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }
#
#
# data1= {"president": {"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}}
# # with open("data_file.json", "w") as write_file:
# #     json.dump(data, write_file)
#
# print(type(data))
# print(type(data1))

# blackjack_hand = (8, "Q")
# encoded_hand = json.dumps(blackjack_hand)
# decoded_hand = json.loads(encoded_hand)
# print(encoded_hand)
# print(decoded_hand)
#
#
# print(blackjack_hand == decoded_hand)
# print(encoded_hand == decoded_hand)
# print(type(blackjack_hand))
# print(type(encoded_hand))
# print(type(decoded_hand))
# print(blackjack_hand == tuple(decoded_hand))

# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)
#
# print(data)
# print(type(data))

import json
import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
# print(todos == response.json())
# print(type(todos))
# print(todos[:10])


todos_by_user = {}
print(todos)

# Increment complete TODOs count for each user.
for todo in todos:
    print(todo)
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1


print(todos_by_user)

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(),
                   key=lambda x: x[1], reverse=True)

print("Top_Users", top_users)

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]
print(max_complete)

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)
print("Max_Users", max_users)