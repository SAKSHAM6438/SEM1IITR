


'''l=[1,2,5,20,20,50,100,200,500,2000]
l2=[1,2,5,20,20,50,100,200,500,2000]
l1=[0]*len(l)
def change(a,l,l1,l2):
    if a==0:
        return l1
    d=l.pop()
    l.append(d)
    if (a-d)>=0:
        l1[l2.index(d)]+=a//d
    
    l.pop()
    return change(a%d,l,l1,l2)
print(change(4556,l,l1,l2))'''
'''#######################################################
x=int(input("Enter Cost of your order"))
y=int(input("Enter amount you provided "))
a=y-x
if a==0:
    print('NO CHANGE IS REQUIRED')
elif a<0:
    print('you need to give her more money')
else:
    for i in changes(4888,d,d1):
   
    print(f'NUMBER OF NOTES/COINS OF {i} : {d[i]}')
    print()'''

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

        



       






































  

        
