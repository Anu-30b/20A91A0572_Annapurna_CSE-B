a=int(input())
if a==1000:
    print('total amount is',a)
    print('discounton the billed amount is',(a*10)/100)
    print('paid bill is',a-((a*10)/100))
elif a>=2000:
    print('total amount is',a)
    print('discount on the billed amount is',(a*20)/100)
    print('paid bill is',a-((a*20)/100))
elif a>=3000 and a<=5000:
    print('total amount is',a)
    print('discount on the billed amount is',(a*30)/100)
    print('paid bill is',a-(a/30))
elif a>=5000:
    print('total amount is',a)
    print('discount on the billed amount is',(a*40)/100)
    print('paid bill is',a-((a*40)/100))
    
##expected output:
##    4500
##total amount is 4500
##discount on the billed amount is 900.0
##paid bill is 3600.0
##    
