a = int(input("Enter the year"))
if( a % 4 == 0 & a % 100 ==0 or a % 400 == 0):
    print("It is a leap year")
else:
    print("It is not a leap year")
