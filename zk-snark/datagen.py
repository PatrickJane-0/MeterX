bid = [(3,10),(4,100),(5,10),(0,0),(0,0)]
offer = [(1,100),(2,30),(10,2),(0,0),(0,0)]
marginal_price = 2
print(marginal_price,len(bid),end=" ")
for b in bid:
    for e in b:
        print(e,end=" ")
print(len(offer),end=" ")
for b in offer:
    for e in b:
        print(e,end=" ")

#2 5 3 10 4 100 5 10 0 0 0 0 5 1 100 2 30 10 2 0 0 0 0