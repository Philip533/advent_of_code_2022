file = open("in.in","r")
line = file.read()
lst = list(file.read())

counter = 0
test = 0
done = False
# while not done:
#     for i in range(int(len(line)) - 4):
#         print(line[i:i+4])
#         for c in line[i:i+4]:
#             if line[i:i+4].count(c) != 1:
#                 done = False
#             else:
#                 if(done):
#                     done = True
#                     exit

def check_unique(letters):
    for c in letters:
        if letters.count(c) != 1:
            return False
    print("DONE")
    return True

letters = line[:14]

begin = 0
end = 14

while not check_unique(letters):
    letters = line[begin:end]
    print(letters)
    counter += 1
    begin += 1
    end += 1
print(counter)
