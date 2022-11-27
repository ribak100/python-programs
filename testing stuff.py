


'''
x =  int(input("How many goods did you bought? : "))
sum = 0
    
for a in range(0,x):
    num = int(input("Enter the prices? :"))
    sum = sum + num
print("The total is ",sum)

'''

'''
print("Enter the 10 prices of the items : ")
sum = 0
for i in range(0,10):
    num = int(input("Enter the price "))
    sum = sum + num

print("The total sum is = ", sum)

'''

def findInverseMod(a,b):
    x = 1
    i=0
    for i in range(1,b):
        mod = (a*x)%b
        if(mod==1):
            return x
        else:
            x +=1


def gcd(c,d):
    if(c==0):
        return d
    return  gcd(d%c, c)
            
x = True
while(x== True):
     a = int(input("enter a : "))
     b = int(input("enter b : "))
        
     if(gcd(a,b)==1):
        print("INVERSE MOD = ", findInverseMod(a,b))
     else:
        print("The values are not relatively prime, hence its not having mod inverse")

     print("do you want to solve another : (y/n)")
     inp = input("Enter your choice : ")
     if((inp== 'y')or(inp== 'Y')):
        x = True
     else:
        x= False
