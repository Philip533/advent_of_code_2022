file = open("in.in","r").readlines()
pr = 0
array = []
counter = 0
# for line in file:

#     line = line.replace("\n", "")
#     length=int(len(line)/2)

#     found = False
#     for c in line[:length]:
#         if c in line[length:] and not found:
#             found = True
#             print(c)
#             if(c.isupper()):
#                 pr = pr + ord(c) - 64 + 26

#             else:
#                 pr = pr + ord(c) - 96 
#     counter = counter + 1


index = 0

while index < len(file) - 1:
    line1 = file[index]
    index+=1
    line2 = file[index]
    index+=1
    line3 = file[index]
    index+=1

    found = False
    for c in line1:
        if c in line2 and not found:
            if c in line3 and not found:
                found = True
                print(c)

                if(c.isupper()):
                    pr = pr + ord(c) - 64 + 26

                else:
                    pr = pr + ord(c) - 96 

print(pr)


