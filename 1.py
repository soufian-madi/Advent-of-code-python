with open('1.txt') as f:
    lines=f.read().splitlines()
    lines=[int(i) for i in lines]
    x,y,z=0,0,0
    for i in lines:
        for j in lines:
            for t in lines:
                if i+j+t==2020:
                    x,y,z = i,j,t
    print("x = ",x ," ,y = ",y, "and z = ",z)
    print("x * y *z = ",x*y*z)
