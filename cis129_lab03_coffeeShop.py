COFFEE = 5.00
MUFFIN = 4.00
TAX = .06
print('***************************************')
print('My Coffee and Muffin Shop')
print('Number of coffees bought?')
answer1 = input()
print('Number of muffins bought?')
answer2 = input()
print('***************************************')
print('   ')
print('***************************************')
print('My Coffee and Muffin Shop Receipt') 
COFFECOST = COFFEE * int(answer1)
MUFFINCOST = MUFFIN * int(answer2)
TOTALCOST = COFFECOST+MUFFINCOST 
TAXCOST = TOTALCOST * TAX
FINALCOST = TAXCOST + TOTALCOST
print(answer1+ 'Coffee at $5 each: $' +str(COFFECOST))
print(answer2+ 'Muffins at $4 each: $' +str(MUFFINCOST))
print('6% tax: $' +str(TAXCOST) )
print('---------')
print('Total: $' +str(FINALCOST))
print('***************************************')
