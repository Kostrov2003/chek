
x = 1

while True:
    for x in range(11) :
        i = 1
        width = x+(x-1)
        for i in range(1,x+1):
            print("{0:^{1}.{2}}".format("*"*(i+(i-1)), width, width))
        x = x + 1
    if x == 11:
        break


