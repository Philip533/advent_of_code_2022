file = open("in.in","r")

counter = 0
for line in file:
    line = line.replace(",", " ")
    line = line.replace("-", " ")
    line = line.replace("\n", "")

    lst = line.split(" ")
    if(int(lst[0]) <= int(lst[2]) <= int(lst[1])):
        counter = counter + 1
    elif(int(lst[2]) <= int(lst[0]) <= int(lst[3])):
        counter = counter + 1
   
print(counter)
