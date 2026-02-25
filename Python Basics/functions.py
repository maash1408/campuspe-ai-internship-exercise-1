# def iAmGroo():
#    print('I am Groot')

# for i in range(0,10):
#    iAmGroo()


#Function with Arguments/parameters and return types
#Function with no arguments/parameters and only return types 
#Function with arguments/parameters and no return types
#Functions with no argument and no return types


# name =input("Please enter your name to continue:")

# def greet_someone(name):
#    print(f"Hello,{name}!")
#    print("Welcome to my python script")

# greet_someone("Mashitha")

# def sum(*args):
#    result=0
#    for num in args:
#        result+=num
#    return result

    

# a=int(input("Please enter value A:"))
# b=int(input("Please enter value B:"))
# c=int(input("Please enter value C:"))
# d=int(input("Please enter value D:"))
# e=int(input("Please enter value E:"))
# help(sum)
# print(f"Sum of {a} + {b} =",sum(a,b,c,d,e))

def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

display_info(name="Mashitha",age=21,sex="Female",married=False)
