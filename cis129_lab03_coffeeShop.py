BFSANDWICH = 10.00
COFFEE = 5.00
MUFFIN = 4.00
CAKEPOP = 3.00
TAX = .06
print('***************************************')
print('My Coffee and Muffin Shop')
print('Number of Breakfast Sandwiches bough?')
answer1 = input()
print('Number of coffees bought?')
answer2 = input()
print('Number of muffins bought?')
answer3 = input()
print('Number of cake pop bought?')
answer4 = input()
print('***************************************')
print('   ')
print('***************************************')
print('My Coffee and Muffin Shop Receipt') 
BFSANDWICHCOST = BFSANDWICH * int(answer1)
COFFECOST = COFFEE * int(answer2)
MUFFINCOST = MUFFIN * int(answer3)
CAKEPOPCOST = CAKEPOP * int(answer4)
TOTALCOST = COFFECOST+MUFFINCOST+CAKEPOPCOST+BFSANDWICHCOST 
TAXCOST = TOTALCOST * TAX
FINALCOST = TAXCOST + TOTALCOST
print(answer2+ 'Coffee at $5 each: $' +str(COFFECOST))
print(answer3+ 'Muffins at $4 each: $' +str(MUFFINCOST))
print(answer1+ 'Breakfast Sandwich at $10 each: $' +str(BFSANDWICHCOST))
print(answer4+ 'Cakepop at $3 each: $' +str(CAKEPOPCOST))         
print('6% tax: $' +str(TAXCOST) )
print('---------')
print('Total: $' +str(FINALCOST))
print('Thank you for coming, we hope to see you again!')
print ('Thank you for coming, we hope you enjoyed your food!')
print('***************************************')
