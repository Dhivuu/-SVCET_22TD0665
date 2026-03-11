a="My favourite food is chicken noodles"
c=0  
for i in range (len(a)):
    if(a[i]==" " and a[i+1]!=""):
        c=c+1 
print("The number of  words present in the line is:",c+1)
