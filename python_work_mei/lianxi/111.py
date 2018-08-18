for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            if a!=b and b!=c and a!=c:
                print(a*100+b*10+c)

input()