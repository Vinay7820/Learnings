# class MyClass:
#     def method(self):
#         return 'instance method called', self
#
#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls
#
#     @staticmethod
#     def staticmethod():
#         return 'static method called'
#
#
# obj = MyClass()
# obj.method()
#
# print(MyClass.method(obj))
# print(MyClass.classmethod())
# print(MyClass.staticmethod())

# class Pizza:
# #     def __init__(self, ingredients):
# #         self.ingredients = ingredients
# #
# #     def __repr__(self):
# #         return ( f'Pizza({self.ingredients!r})')
# #
# # print(Pizza(['cheese', 'tomatoes']))
# # print(Pizza(['mozzarella', 'tomatoes']))
# # print(Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms']))
# # print(Pizza(['mozzarella'] * 4))

#
# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         return f'Pizza({self.ingredients!r})'
#
#     @classmethod
#     def margherita(cls):
#         return cls(['mozzarella', 'tomatoes'])
#
#     @classmethod
#     def prosciutto(cls):
#         return cls(['mozzarella', 'tomatoes', 'ham'])


# class DecoratorExample:
#     """ Example Class """
#     Dev = 'Anjaneya'
#     def __init__(self,name):
#         """ Example Setup """
#         print('Hello, World!')
#         self.name = name
#
#     def instance_function(self):
#         """ This method is an instance method! """
#         print('I\'m an instance method!')
#         print(self.Dev)
#         Dev = "A"
#         print(Dev)
#
#         print('My name is ' + self.name)
#         j = self.Dev
#         self.some_other_function(j)
#         print('My GOD Name is  ' + self.Dev)
#         self.Dev = 'instancechangedDev'
#         print('God name is ' + self.Dev)
#
#     def example_function(cls):
#         """ This method is a class method! """
#         print(cls.Dev)
#         Dev = "A"
#         print(Dev)
#         print('I\'m a class method!')
#         f = cls.Dev
#         cls.Dev = cls.some_other_function(f)
#         print(cls.Dev)
#         print('God name is ' + cls.Dev)
#         cls.Dev = 'classchangedDev'
#         print('God name is ' + cls.Dev)
#         print('Class.Name', cls.name)
#
#     @staticmethod
#     def some_other_function(h):
#         print('Hello!')
#         h = "Changed now"
#         return h
#
#
# de = DecoratorExample('Vinay')
# de.example_function()
# de.instance_function()




