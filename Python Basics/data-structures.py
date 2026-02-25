#Lists

students = ["Mashitha","Farheen","Anshas","Rasha"]
numbers = [5,6,8,7,5,8,6]
mixed = [1,"Mashitha",25.4,True]

# students[1] = "Arun"
# students.pop()
# print(students)

#Length
# print("Length of students lists is" ,len(students))
#sum,min,max
# print("Sum of all numbers lists is" ,sum(numbers))
# print("Min no in the numbers list is" ,min(numbers))
# print("Max no in the numbers list is" ,max(numbers))
#count
# print("Total number of occurences of number 4 is" ,numbers.count(4))
#find index
# print("The index of the List item Farheen is",students.index("Farheen"))
#sort
# students.sort()
# print(students)
#reverse
# numbers.reverse()
# print(numbers)
#check membership
# print("Mm" in students)

# for name in students:
#    print(name)

# print(range(len(students)))

# for i in range(len(students)):
#    print(f"{i}: {students[i]}")

# print(enumerate(students))
# for k,v in enumerate(students):
#    print(f"{k}: {v}")

# squares = []
# for i in range(1,6):
#    squares.append(i ** 2)

# squares = [i ** 2 for i in range(1,6)]
# print(squares)

#Tuples

# coordinates = (10,20)
# person = ("Mashi", 21, "Bhadravathi")
# print(person[2])

# name, age, district = person
# print(f"I am {name}, from {district}, I am {age} years old")


#Dictionaries

mathClass = {}

student={
    "name":"Mashitha",
    "age":21,
    "grade":"A",
    "courses":["Math","Science","Social Science"]
}

# print(student["name"])
# student["phone"] = "8856479346"

# print(student.get("phone","User's phone number doesn't exist"))
# student['age']=26

# student.pop("grade")
# print(student)
# for key in student:
#    print(f"{key}: {student[key]}")

#for key, value in student.items():
#    print(f"{key}:{value}")


#Sets

empty_set=set()
numbers=[1,2,3,1,2,3,4,5,3,4,3,5,5,3]
unique_numbers=set(numbers)
print(numbers)
print(unique_numbers)
unique_numbers.discard(999)