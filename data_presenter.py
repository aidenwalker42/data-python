

open_file = open("CupcakeInvoices.csv")
for x in open_file:
    print(x)

open_file.seek(0)

for x in open_file:
    x=x.strip()
    newlist = x.split(",")
    print(newlist[2: 3])
 
open_file.seek(0)
sum=0.0
for x in open_file:
    x=x.strip()
    newlist = x.split(",")
    print("total for " + newlist[0] + " " + newlist[1] + " is " )
    sum = float(newlist[3]) * float(newlist[4])
    print(round(sum, 2))

open_file.seek(0)
thesum = 0
for x in open_file:
    x=x.strip()
    newlist = x.split(",")
    thesum += float(newlist[3]) * float(newlist[4])
print(round(thesum, 2))

open_file.seek(0)
chocolate = 0
vanilla = 0
strawberry = 0

for x in open_file:
    x=x.strip()
    newlist = x.split(",")
    total = round(float(newlist[3]) * float(newlist[4]), 2)
    if newlist[2] == "Chocolate":
        chocolate += total
    if newlist[2] == "Vanilla":
        vanilla += total
    if newlist[2] == "Strawberry":
        strawberry += total
print("Chocolate total $", round(chocolate, 2), "Vanilla total $", round(vanilla, 2), "Stawberry Total $", round(strawberry, 2))
