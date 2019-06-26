# class A(): pass
#
#
# class B(): pass
#
#
# class C(A,B) : pass
#
#
# class D(B,A): pass
#
#
# class E(C,D): pass


# class A:
#     def whereiam(self):
#         print("I am in A")
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     def whereiam(self):
#         print("I am in C")
#
#
# class D(B, C):
#     pass
#
# d_obj = D()
# d_obj.whereiam()



class F(): pass


class E(): pass


class D(): pass


class C(D,F): pass


class B(D,E): pass


class A(B,C): pass
print(A.mro())