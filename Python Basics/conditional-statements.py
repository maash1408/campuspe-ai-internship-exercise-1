#name_str = input("Hi what is your name?")
#age=input("Hi "+name_str+", what is your age?")

#password="123123123"

#IF ELSE conditions

#if password=="secret@123":
#    print("Access granted")
#else:
#    print("Access denied")

#if int(age) >= 18:
#    print("You are an adult")
#   print("You can vote!")
#else:
#   print("You are a bacha")
#    print("Go have some ice cream")


#IF ELSE IF Condition

#score = 85

#if score >= 90:
#    grade='A'
#elif score >= 80:
#    grade ='B'
#elif score >= 70:
#    grade ='C'
#elif score >= 60:
#    grade ='D'
#else:
#    grade='F'

#print("Your Grade is :", grade)


#NESTED IF ELSE

#age=25
#has_license=False

#if age >=18:
#    print("You are old enough to drive")

#    if has_license:
#        print("You can drive!")
#    else:
#        print("But you need a license")
#else:
#    print("Too young to drive")


#IF ELSE USING "AND"

#age=20
#has_ticket=False
#if age >= 18 and has_ticket:
#    print("You can enter the concert")
#else:
#    print("Cannot enter")


#IF ELSE USING "OR"

#day="monday"

#if day == "saturday" or day =="sunday":
#    print("It's the weekend! open the book")
#else:
#    print("It's a weekday")


#is_sunny =True

#if not is_sunny:
#    print("It's sunny")
#else:
#    print("It's cloudy")


#Ternary operator

age=21

#if age>=18:
#    status="adult"
#else:
#    status="minor"

status="adult" if age >= 18 else "minor"
print(status)