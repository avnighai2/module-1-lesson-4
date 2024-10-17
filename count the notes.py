# take an input from a user. calc the number of needed for 100,50,20,10,5,2,1.

moneyneeded = int(input(" How much money do you need: "))

countof100 = moneyneeded//100
remaning100 = moneyneeded%100
countof50 = remaning100//50
remaning50 = remaning100%50
countof20 = remaning50//20
remaning20 = remaning50%20
countof10 = remaning20//10
remaning10 = remaning20%10 
countof5 = remaning10//5
remaning5 = remaning10%5 
countof2 = remaning5//2
remaning2 = remaning5%2
countof1 = remaning2//1
remaning1 = remaning2%1 

print(f" The count of 100 is {countof100}")
print(f" The count of 50 is {countof50}")
print(f" The count of 20 is {countof20}")
print(f" The count of 10  is {countof10}")
print(f" The count of 5 is {countof5}")
print(f" The count of 2 is {countof2}")
print(f" The count of 1 is {countof1}")