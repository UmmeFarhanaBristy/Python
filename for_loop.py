exp = [4124, 1243, 1424, 9875, 4567, 9875]

# total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4] + exp[5]
# instead of line 3 for loop can be used which is more user friendly

total = 0
for item in exp:                # here item works as iterator
    total = total + item

# print(total)

for i in range(1, 11):          # range(a, b) has numbers form a to b-1
    print(i)
