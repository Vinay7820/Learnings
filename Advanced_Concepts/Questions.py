#######################################################
############Validating Credit card number##############
#######################################################
#  def isValid(x):
#     if len(x) not in [16,19]:
#         return False
#     if len(x)==19:
#         if x[4]!='-' or x[9]!='-' or x[14]!='-':
#             return False
#     if x[0] not in ['4','5','6']:
#         return False
#     if '-' in x:
#         x=''.join(x.split('-'))
#     if any(ord(x[i]) not in range(ord('0'),ord('9')+1) for i in range(16)):
#         return False
#     if any(str(i)*4 in x for i in range(10)):
#         return False
#     return True
# for _ in range(int(input())):
#     x=input()
#     if isValid(x):
#         print("Valid")
#     else:
#         print("Invalid")
######################################################
######################################################


##############################################
####Maximum Difference in a list##############
##############################################
# l = [1,2,3,4,5]
# max_diff = 0
# for i in range(0,len(l)):
#     print("I=", i)
#     for j in range(i+1, len(l)):
#         print("J=", j)
#         if l[j]-l[i] > max_diff:
#             max_diff = l[j]-l[i]
# print(max_diff)




# l = [1,2,3,4,1,55,6,100,0,100,1,0]
# max_number_in_list = max(l)
# print(max_number_in_list)
# min_number_in_list = min(l)
# print(min_number_in_list)
# print("Max Difference =", (max_number_in_list-min_number_in_list))
##############################################
##############################################
# ##############################################
##############################################


#######################################################
###############Validating Phone Number#################
#######################################################
# import re
# for i in range(int(input())):
#     print('YES' if re.search(r"^[789]\d{9}$", input()) else 'NO')
#######################################################
#######################################################

#################################################################
######Function to rotate string left and right by d length#######
#################################################################
# def rotate(input, d):
#     Lfirst = input[0: d]
#     Lsecond = input[d:]
#     Rfirst = input[0: len(input) - d]
#     Rsecond = input[len(input) - d:]
#     print("Left Rotation : ", (Lsecond + Lfirst))
#     print("Right Rotation : ", (Rsecond + Rfirst))
#
# if __name__ == "__main__":
#     input = 'GeeksforGeeks'
#     d = 2
#     rotate(input, d)
##################################################################
##################################################################

################################################
############Validating Roman Numerals###########
################################################
###link - https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html###
# import roman
# x=input()
# try:
#     if (roman.fromRoman(x)>0 and roman.fromRoman(x)<4000):
#         print("True")
#     else:
#         print("False")
# except:
#     print("False")
#################################################
#################################################



#################################################
###########Encrypt using werkzeug###############
#################################################

# pas ="abc"
# from werkzeug.security import generate_password_hash
# print (generate_password_hash(pas, "sha256"))


# from cryptography.fernet import Fernet
# key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
# cipher_suite = Fernet(key)
# ciphered_text = cipher_suite.encrypt(b"SuperSecretPassword")   #required to be bytes
# print(ciphered_text)
#
# from cryptography.fernet import Fernet
# key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
# cipher_suite = Fernet(key)
# ciphered_text = b'gAAAAABaHvk3g8IG4cln7g5HCulppy1bAPVuhtskVcgPXRyytx6RkIqjcI0mAMA7Oy_56T6J0dk-yjxI_WlZtjxnUBbR-EvoQa_oqCKoQJFbv_uc2WdXMSI='
# unciphered_text = (cipher_suite.decrypt(ciphered_text))
# print(unciphered_text)

#################################################
#################################################
#################################################


############################################################
######Python program to check validation of password########
############################################################
# # Module of regular expression is used with search()
# import re
# password = "R@m@_f0rtu9e$"
# flag = 0
# while True:
#     if (len(password)<8):
#         flag = -1
#         break
#     elif not re.search("[a-z]", password):
#         flag = -1
#         break
#     elif not re.search("[A-Z]", password):
#         flag = -1
#         break
#     elif not re.search("[0-9]", password):
#         flag = -1
#         break
#     elif not re.search("[_@$]", password):
#         flag = -1
#         break
#     elif re.search("\s", password):
#         flag = -1
#         break
#     else:
#         flag = 0
#         print("Valid Password")
#         break
#
# if flag ==-1:
#     print("Not a Valid Password")

#################################################
#################################################
#################################################



#################################################
######Progrqam to reverse a string###############
#################################################

# def reverse(s):
#     return s[::-1]

# def isPalindrome(s):
#     # Calling reverse function
#     rev = reverse(s)
#
#     # Checking if both string are equal or not
#     if (s == rev):
#         return True
#     return False

# s = "malayalam"
# ans = isPalindrome(s)

# if ans == 1:
#     print("Yes")
# else:
#     print("No")

#################################################
#################################################
#################################################


##############################################################################
###########Python program to check if given number is prime or not############
##############################################################################

# num = 11
#
# # If given number is greater than 1
# if num > 1:
#
#     # Iterate from 2 to n / 2
#     for i in range(2, num // 2):
#
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#         else:
#             print(num, "is a prime number")
#
# else:
#     print(num, "is not a prime number")

#################################################
#################################################
#################################################

#################################################
########Python code to reverse a string##########
#################################################

# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
# s = "Geeksforgeeks"
# print("The original string  is : ", end="")
# print(s)
# print("The reversed string(using loops) is : ", end="")
# print(reverse(s))


# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]

# s = "Geeksforgeeks"
# print("The original string  is : ", end="")
# print(s)
# print("The reversed string(using recursion) is : ", end="")
# print(reverse(s))

#################################################
#################################################
#################################################


#################################################
#############Reverese a number###################
#################################################
# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")

#####################################################
#####################################################
#####################################################

#####################################################
##############Swap without temp variable#############
#####################################################
# x,y = y,x
# x = x + y
# y = x - y
# x = x - y
#####################################################
#####################################################
#####################################################







