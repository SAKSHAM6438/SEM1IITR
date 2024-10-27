

#################################################################################################################################################
def changes(a,denomination,demo_denomination):
    if a==0 or len(demo_denomination)==0:
        return d
    b=demo_denomination.popitem()
    demo_denomination[b[0]]=b[1]
    if a-b[0]>=0:
        denomination[b[0]]+=a//b[0]
    demo_denomination.popitem()
    return changes(a%b[0],denomination,demo_denomination)

d={1:0,2:0,5:0,10:0,20:0,50:0,100:0,200:0,500:0,2000:0}
d1={1:0,2:0,5:0,10:0,20:0,50:0,100:0,200:0,500:0,2000:0}
x=int(input("Enter Cost of your order"))
y=int(input("Enter amount you provided "))
a=y-x
if a==0:
     print('NO CHANGE IS REQUIRED')
elif a<0:
    print('you need to give her more money')
else:
    print("SHE HAS TO RETURN ME .........")
    print()
    for i in changes(a,d,d1):
        print(f'NUMBER OF NOTES/COINS OF {i} : {d[i]}')
        print()

##############################################################################################################################################

        



       






































  

        
