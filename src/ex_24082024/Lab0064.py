# 1. No return type and no parameter

def greet():
    print("Hello, World")
result = greet()
print(result)

# 2. Np return type with argument

def greet_by_name(name):
    print("Hello",name)
greet_by_name("Susmi")


# 3. No return type and with Default argument

def say_hello_default_arg(name="Aarvi"):
    print("Hello",name)
say_hello_default_arg("Ivanka")
say_hello_default_arg()
say_hello_default_arg(name="Ravi")


def multiple_args(name1="Susmi", name2="Radhi", name3="Aarvi", name4="Ivanka"):
    print("Multiple Arguments", name1,name2,name3,name4)
multiple_args()
multiple_args("Susmi2","Radhi2","Aarvi2","Ivanka2")



# 4. Argument + return type

def Sum_of_two_numbers(num1,num2):
    return num1+num2
result = Sum_of_two_numbers(10,20)
print(result)

