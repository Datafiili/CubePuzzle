Data = [4, 3, 3, 4, 0, 6, 2, 6, 6, 3, 3, 1, 4, 0, 6, 2, 2, 5, 1, 1, 1, 1, 0, 5, 2, 5, 5]
for x in range(3):
    for z in range(3):
        for y in range(3):
            a =(x) + (z * 3) + (y * 9)
            print("N:",a,"D:",Data[a],"       X",x,"Z",z,"Y",y)