def checkBanana(amnt_banana,amnt,b_count):
    if(amnt <1000 and amnt_banana <1000 and b_count <1000):
        b_cost=0
        for i in range(1,b_count+1):
            b_cost=b_cost+i*amnt_banana
            print(b_cost)
        if(b_cost<amnt):
            return 0
        else:
            return b_cost-amnt
    else:
        return "count exist"
str1=input('Enter the input')
x=str1.split()
if(x.__len__()==3 and str1.replace(" ","").isdigit()):
    print(checkBanana(int(x[0]),int(x[1]),int(x[2])))
else:
    print("First have not equal to 3 numbers OR the input have a string value")
