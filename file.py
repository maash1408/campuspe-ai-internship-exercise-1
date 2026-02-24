#file = open("test.txt","r")
#content=file.read()
#print(content)
#file.close()

# with open("test.txt","r") as file:
#    lines = file.readline()
#    print(lines)

# with open("test.txt","r") as file:
#    lines = file.readlines()
#    for line in lines:
#        print(line.strip())
    
with open("output.txt","w") as file:
    file.write("Hello World 2 \n")
    file.write("This is a new file\n")
    