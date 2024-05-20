# def greet_user():
#     print("hallo world")
# greet_user()
# def aoa():
#     print("aoa ,all the way from wah cantt")
# aoa()

# def aoa(name):
#     print(f"Asalam o Alikum,{name}")
# aoa('shah')

# #default parameter value
# def aoa(name="khuda ka banda"):
#     print(f"Asalam o Alikum,{name},kia hall hae")
# aoa("shah")
# # return value ko kasa use karta haen function main
# def square(number):
#     return number*number
# print(square(3))

# #same as uper wala code
# def square(number):
#     return number*number
# result=square(3)
# print(result)


#recursion function
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(6))

#lamda function in one line important function in data scince

x=lambda a: a+10
print(x(5))
#double parameter
x=lambda a,b:a*b
print(x(5,6))
#same as above
def x(a):
    return a+10
x=lambda  a,b:a*b
print(x(5,6))