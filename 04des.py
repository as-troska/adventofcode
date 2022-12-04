with open("04des.txt") as file:
    usable = []
    for line in file:
        line = line.replace("\n", "")
        pair = []
        splitted = line.split(",")
        for ranges in splitted:
            for i in ranges.split("-"):
                pair.append(int(i))
        usable.append(pair)

overlapping = 0
fulloverlap = 0

for pair in usable:
    elfonestart = pair[0]
    elfoneend = pair[1]
    elftwostart = pair[2]
    elftwoend = pair[3]
    
    if (elfonestart <= elftwostart and elfoneend >= elftwoend):
        fulloverlap = fulloverlap + 1
        overlapping = overlapping + 1
    elif (elftwostart <= elfonestart and elftwoend >= elfoneend):
        fulloverlap = fulloverlap + 1
        overlapping = overlapping + 1
    elif (elfonestart <= elftwostart <= elfoneend or elfonestart <= elftwoend <= elfoneend):
        overlapping = overlapping + 1
       
print("Pairs with full overlap:", fulloverlap)
print("Pairs with partial overlap:", overlapping)

