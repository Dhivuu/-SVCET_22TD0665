a = int(input("Enter a row"))
for i in range(1, a+1):
    star = (1*i-1) * "*"
    space = (a+1) * ""
    print(star+space)