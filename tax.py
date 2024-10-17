
print( " Welcome to the 2024 Ontario Tax Calculator. Based on your yearly income, this program will calculate the Federal, Provincial taxes each person must pay. ")

taxpayer = int(input("Enter your yearly income: $"))

federaltaxowned = 0 
if (taxpayer > 0 and taxpayer <= 53359 ):
    federaltaxowned = 15 
elif(taxpayer > 53359 and taxpayer <= 106177 ):
    federaltaxowned = 20.5 
elif(taxpayer > 106177 and taxpayer <= 165430 ):
    federaltaxowned = 26
elif(taxpayer > 165430 and taxpayer <= 235675 ):
    federaltaxowned = 29 
else:
    federaltaxowned = 33
    
provincialtaxowned = 0 
if (taxpayer > 0 and taxpayer <= 49231 ):
    provincialtaxowned = 5.05
elif(taxpayer > 492321 and taxpayer <= 98463 ):
    provincialtaxowned = 9.15 
elif(taxpayer > 98463 and taxpayer <= 150000 ):
    provincialtaxowned = 11.16
elif(taxpayer > 150000 and taxpayer <= 220000 ):
    provincialtaxowned = 12.16 
else:
    provincialtaxowned = 13.16

federaltax = (federaltaxowned / 100)* taxpayer

provincialtax = (provincialtaxowned / 100 )* taxpayer 

total = (federaltax + provincialtax )

effective = total / taxpayer 

print( f"Federal tax owed: ${federaltax}")
print( f"Provoncial tax owed: ${provincialtax}")
print( f"Total tax owed: ${total}")
print( f"Effective tax rate: ${effective}")


