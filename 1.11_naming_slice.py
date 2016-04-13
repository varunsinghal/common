#Naming a slice

record = [23, 54, 32, 67, 56, 33]

SHARES = slice(0,3)
PRICES = slice(3,6)

print record[SHARES]
#Output: [23, 54, 32]

print record[PRICES]
#Output: [67, 56, 33]
