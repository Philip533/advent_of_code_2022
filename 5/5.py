file = open("in.in","r")
slice = []

list_2d=[["G","D","V","Z","J","S","B"],
         ["Z","S","M","G","V","P"],
         ["C","L","B","S","W","T","Q","F"],
         ["H","J","G","W","M","R","V","Q"],
         ["C","L","S","N","F","M","D"],
         ["R","G","C","D"],
         ["H","G","T","R","J","D","S","Q"],
         ["P","F","V"],
         ["D","R","S","T","J"]]

for line in file:
    print(line)
    line = line.replace("\n", "")
    lst = line.split(" ")
    slice = list_2d[int(lst[1]) - 1][int(len(list_2d[int(lst[1]) - 1]))-int(lst[0]):]
    #slice.reverse()
    list_2d[int(lst[2]) - 1].extend(slice)
    list_2d[int(lst[1]) - 1] = list_2d[int(lst[1]) - 1][:-int(lst[0])]
for i in range(9):
    print(list_2d[i][-1])

