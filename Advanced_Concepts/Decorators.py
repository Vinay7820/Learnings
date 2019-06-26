# def speak():
#     def v(t):
#         return t.lower() + '...'
#     return v
#
# Devre = speak()
# print(Devre("A"))


# def null_decorator(func):
#     return func
#
#
# def greet():
#     return 'Hello!'
#
# greet = null_decorator(greet)
#
# print(greet())


# def greet():
#     return 'Hello!'.upper()
#
# def greet1():
#     return 'Hello!'.lower()
#
# print(greet())
# print(greet1())



# def uppercase(func, ):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#
#     def wrapper2():
#         original_result = func()
#         modified_result = original_result.lower()
#         return modified_result
#
#     if func == low:
#         return wrapper
#     else:
#         return wrapper2
#
# @uppercase
# def greet():
#     return 'Hello!'
#
# greet()


f = "Hello"
def outer_func():
    f = "Hi&Hello"
    message = "Devre"
    return "Hi"

v = outer_func()
print(v)
#print(v.message)
print(v.f)


